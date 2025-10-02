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

"""Noise region detection and confidence interval estimation for spectra.

This module provides classes for detecting signal and noise regions in spectral data,
as well as for computing confidence intervals for noise levels. The main components
include abstract and concrete detectors for identifying regions of interest and a
utility for estimating noise statistics.

Classes
-------
SignalRegionDetector : ABC
    Abstract base class for signal region detection in spectra.
IterativeThresholdingSignalRegionDetector : SignalRegionDetector
    Detects signal regions using iterative thresholding based on the spectrum's derivative.
NoiseRegionDetector : IterativeThresholdingSignalRegionDetector
    Detects noise regions as the complement of the detected signal region.
NoiseConfidenceInterval
    Computes mean, standard deviation, and confidence intervals for noise in a spectrum.

"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property

import numpy as np

from .signal import Spectrum


class SignalRegionDetector(ABC):
    """Abstract base class for signal region detection in spectra."""

    @abstractmethod
    def detect(self, s: Spectrum) -> np.ndarray:
        """Detect signal regions in a spectrum.

        Parameters
        ----------
        s : Spectrum
            The spectrum to analyze.

        Returns
        -------
        np.ndarray
            Boolean mask for detected region.
        """
        raise RuntimeError("Not meant to be instantiated!")


@dataclass(frozen=True)
class IterativeThresholdingSignalRegionDetector(SignalRegionDetector):
    """Detects signal regions in a spectrum using iterative thresholding.

    Parameters
    ----------
    sigma_factor : float, optional
        Sigma factor for thresholding (default is 3.0).
    """

    sigma_factor: float = 3.0

    __deriv_filter = np.array([-1, -8, -27, -48, -42, 0, 42, 48, 27, 8, 1]) / 512

    def detect(self, s: Spectrum) -> np.ndarray:
        smag = s.mag
        deriv = np.convolve(smag, self.__deriv_filter, mode='same')

        dmag = np.abs(deriv)
        mask = np.zeros(smag.shape, dtype=bool)

        current_size = mask[mask==True].size
        prev_size = -1

        while current_size < mask.size and current_size - prev_size > 0:
            prev_size = current_size
            mask = dmag > self.sigma_factor * deriv[mask==False].std()
            current_size = mask[mask==True].size
        
        return smag > self.sigma_factor * smag[mask==False].std()


@dataclass(frozen=True)
class NoiseRegionDetector(IterativeThresholdingSignalRegionDetector):
    """Detects noise regions in a spectrum with iterative thresholding.

    The noise region is defined as the complement of the signal region.
    The signal region is detected using the IterativeThresholdingSignalRegionDetector.

    Parameters
    ----------
    sigma_factor : float, optional
        Sigma factor for thresholding.
    """

    def detect(self, s: Spectrum) -> np.ndarray:
        """Detect noise regions in a spectrum.

        Parameters
        ----------
        s : Spectrum
            The spectrum to analyze.

        Returns
        -------
        np.ndarray
            Boolean mask for noise region.
        """
        return super().detect(s) == False


@dataclass(frozen=True)
class NoiseConfidenceInterval:
    """Computes confidence intervals for noise in a spectrum.

    Parameters
    ----------
    spectra : Spectrum
        The spectrum data.
    noise_mask : np.ndarray
        Boolean mask for noise region.
    """

    spectra: Spectrum
    noise_mask: np.ndarray

    @cached_property
    def mean(self) -> float:
        """float: Mean of the noise region."""
        return self.spectra.real[self.noise_mask].mean()

    @cached_property
    def std(self) -> float:
        """float: Standard deviation of the noise region."""
        return self.spectra.real[self.noise_mask].std()

    def level(self, sigma_factor: float) -> float:
        """Compute the threshold level for a given sigma factor.

        Parameters
        ----------
        sigma_factor : float
            Sigma factor for threshold.

        Returns
        -------
        float
            Threshold level.
        """
        return sigma_factor * self.std + self.mean
