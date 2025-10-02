# Copyright ICube Laboratory (2025)
# contributor: Julien PONTABRY (jpontabry at unistra dot fr)

# This software is a computer program whose purpose is to correct thermally-shifted 
# spectra acquired with the R2D3 sequence.

# This software is governed by the CeCILL license under French law and
# abiding by the rules of distribution of free software. You can use, 
# modify and/or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info". 

# As a counterpart to the access to the source code and rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty and the software's author, the holder of the
# economic rights, and the successive licensors have only limited
# liability. 

# In this respect, the user's attention is drawn to the risks associated
# with loading, using, modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean that it is complicated to manipulate, and that also
# therefore means that it is reserved for developers and experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or 
# data to be ensured and, more generally, to use and operate it in the 
# same conditions as regards security. 

# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

# For more information, see the LICENSE file.

"""Definitions for peak detection, refinement, and matching.

This module provides classes and functions for detecting, refining, and matching peaks 
in spectral data.

Classes
-------
- PeakRefiner
    Refines the position and height of detected peaks using quadratic fitting for sub-resolution accuracy.
- PeaksFinder (abstract)
    Abstract base class for peak finding algorithms.
- NoiseStatisticsPeaksFinder
    Peak finder implementation using noise statistics for filtering and thresholding.
- PeaksMatcher (abstract)
    Abstract base class for peak matching algorithms.
- NaiveStablePeaksTopMatcher
    Naive matcher for peaks based on an adaptive stable matching algorithm (Gale-Shapley variant).

"""

from typing import Optional
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property

import scipy as sc
import numpy as np

from .peaks_core import Peak
from .signal import Spectrum
from .noise import NoiseConfidenceInterval, NoiseRegionDetector


@dataclass(frozen=True)
class PeakRefiner:
    """Refines the position and height of a peak using quadratic fitting.

    This help to improve the precision of peak detection to sub-resolution level.

    Parameters
    ----------
    nb_points : int, optional
        Number of points to use for fitting (default is 4).
    """

    nb_points: int = 4

    @cached_property
    def x(self) -> list[int]:
        """list of int: Relative positions for fitting."""
        return [i-self.nb_points//2
                for i in range(self.nb_points + 1)]
    
    @cached_property
    def __A(self) -> np.ndarray:
        return np.vstack((np.power(self.x, 2), 
                          self.x, 
                          np.ones(len(self.x)))).T

    def refine(self, p: Peak, s: Spectrum) -> Peak:
        """Refine the peak position and height.

        Parameters
        ----------
        p : Peak
            The peak to refine.
        s : Spectrum
            The spectrum containing the peak.

        Returns
        -------
        Peak
            Refined peak.
        """
        y = s.real[[p.index + i for i in self.x]]
        X = np.linalg.pinv(self.__A.T @ self.__A) @ self.__A.T @ np.array([y]).T
        imax = float((-X[1]/(2*X[0]))[0])
        return Peak(p.index, (X[0]*imax**2 + X[1]*imax + X[2])[0], imax)


class PeaksFinder(ABC):
    """Abstract base class for peak finding algorithms."""

    @abstractmethod
    def find(self, s: Spectrum) -> list[Peak]:
        """Find peaks in a spectrum.

        Parameters
        ----------
        s : Spectrum
            The spectrum to search.

        Returns
        -------
        list of Peak
            List of found peaks.
        """
        raise RuntimeError("Not meant to be instantiated!")


@dataclass(frozen=True)
class NoiseStatisticsPeaksFinder(PeaksFinder):
    """Peak finder using noise statistics for filtering

    Parameters
    ----------
    noise_detector : NoiseRegionDetector, optional
        Detector for noise regions.
    prominence_sigma_factor : float, optional
        Sigma factor for peak prominence threshold.
    thresh_sigma_factor : float, optional
        Sigma factor for peak height threshold.
    refiner : PeakRefiner or None, optional
        Refiner for peak positions.
    """

    noise_detector: NoiseRegionDetector = NoiseRegionDetector()
    prominence_sigma_factor: float = 5
    thresh_sigma_factor: float = 6
    refiner: Optional[PeakRefiner] = PeakRefiner()

    def find(self, s: Spectrum) -> list[Peak]:
        mask = self.noise_detector.detect(s)
        noise_ci = NoiseConfidenceInterval(s, mask)

        peaks, _ = sc.signal.find_peaks(s.real,
                                        prominence=noise_ci.level(self.prominence_sigma_factor),
                                        height=noise_ci.level(self.thresh_sigma_factor))
        peaks = [Peak(p, float(s.real[p])) for p in peaks]

        if self.refiner:
            peaks = [self.refiner.refine(p, s) for p in peaks]

        return peaks


class PeaksMatcher(ABC):
    """Abstract base class for peak matching algorithms."""

    @abstractmethod
    def match(self, peaksA: list[Peak], peaksB: list[Peak], resolution: float = 2e-5) -> list[tuple[Peak, Peak]]:
        """Match peaks between two lists.

        Parameters
        ----------
        peaksA : list of Peak
            First list of peaks.
        peaksB : list of Peak
            Second list of peaks.
        resolution : float, optional
            Frequency resolution.

        Returns
        -------
        list of tuple of Peak
            List of matched peaks.
        """
        raise RuntimeError("Not meant to be instantiated!")


@dataclass(frozen=True)
class NaiveStablePeaksTopMatcher(PeaksMatcher):
    """Naive matcher for peaks based on adaptive stable matching.

    It is based on the Gale-Shapley algorithm with some adaptations
    to filter out non-relevant matches. In particular, a maximum
    frequency difference threshold is used to discard irrelevant matches
    in the context of shift correction for the R2D3 sequence.

    Parameters
    ----------
    freq_upper_threshold : float, optional
        Maximum allowed frequency difference for matching (in ppm).
    """

    freq_upper_threshold: float = 0.02  # in ppm

    def __create_prefs(self, idx: list[int], distances: np.ndarray, resolution: float) -> Optional[int]:
        filtered = [k for k in idx if distances[k] < self.freq_upper_threshold/resolution]
        prefs_list = sorted(filtered, key=lambda k: distances[k])
        return prefs_list[0] if prefs_list else None

    def match(self, peaksA: list[Peak], peaksB: list[Peak], resolution: float = 2e-5) -> list[tuple[Peak, Peak]]:
        n, m = len(peaksA), len(peaksB)
        remIdxA = list(range(n))
        remIdxB = list(range(m))

        # calculate the distance matrix
        idxA = np.array([p.index for p in peaksA]).reshape(n, 1)
        idxB = np.array([p.index for p in peaksB]).reshape(m, 1)
        distances = sc.spatial.distance_matrix(idxA, idxB)

        # calculate the preferences lists
        prefsA = [self.__create_prefs(remIdxB, distances[i], resolution) for i in remIdxA]
        prefsB = [self.__create_prefs(remIdxA, distances[:, j], resolution) for j in remIdxB]

        # matching
        matches = {}

        while remIdxA and remIdxB:
            a = remIdxA.pop(0)
            b = prefsA[a]

            if b in remIdxB and prefsB[b] == a:
                matches[b] = a
                remIdxB.remove(b)
        
        return [(peaksA[a], peaksB[b]) for b, a in matches.items()]
