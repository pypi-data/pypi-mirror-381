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

"""Spectral Shift Correction

This module provides classes and functions for correcting spectral shifts in a set of spectra.
It uses peak detection and matching to estimate the shifts between spectra and applies
radial basis function (RBF) interpolation to compute smooth shift maps.

Classes
-------
ShiftMap
    Represents a shift map using RBF interpolation.
ShiftMapsList
    Wrapper for a list of ShiftMap objects and utilities to apply them.
SparsePeaksShiftMapCalculator
    Calculates a shift map from matched peaks using RBF interpolation.
SparsePeaksShiftCorrector
    Corrects spectral shifts using detected peaks and shift maps.

Type Aliases
------------
PeaksList
    Alias for list of Peak objects.
MatchesList
    Alias for list of matched Peak pairs.

"""

from dataclasses import dataclass
from typing import Iterator

from scipy.interpolate import RBFInterpolator
import numpy as np

from .signal import Spectrum, Spectra
from .peaks import Peak, PeaksFinder, NoiseStatisticsPeaksFinder
from .peaks import PeaksMatcher, NaiveStablePeaksTopMatcher


@dataclass(frozen=True)
class ShiftMap:
    """Represents a shift map using RBF interpolation.

    Parameters
    ----------
    interpolator : RBFInterpolator
        Interpolator for shift values.
    """

    interpolator: RBFInterpolator
    
    def __call__(self, indexes: np.ndarray) -> np.ndarray:
        """Apply the shift map to given indices.

        Parameters
        ----------
        indexes : np.ndarray
            Indices to shift.

        Returns
        -------
        np.ndarray
            Shifted indices.
        """
        return self.interpolator(indexes.reshape(-1, 1)).flatten()


@dataclass(frozen=True)
class ShiftMapsList:
    """Wrapper for list of ShiftMap objects.

    Parameters
    ----------
    maps : list of ShiftMap
        List of shift maps.
    """

    maps: list[ShiftMap]

    def __iter__(self) -> Iterator[ShiftMap]:
        """Iterator over ShiftMap objects."""
        return iter(self.maps)
    
    def __len__(self) -> int:
        """int: Number of shift maps."""
        return len(self.maps)
    
    def complete_shift_map(self, ref: Spectrum) -> np.ndarray:
        """Compute the complete shift map for a reference spectrum.

        Parameters
        ----------
        ref : Spectrum
            Reference spectrum.

        Returns
        -------
        np.ndarray
            Array of shift values for each map.
        """
        indexes = np.arange(ref.size)
        return np.array([m(indexes) for m in self])

    def apply(self, sp: Spectra) -> Spectra:
        """Apply the shift maps to a set of spectra.

        Parameters
        ----------
        sp : Spectra
            Spectra to correct.

        Returns
        -------
        Spectra
            Corrected spectra.
        """
        if len(self) != len(sp) - 1:
            raise ValueError(f"Expecting {len(self)} spectra; received {len(sp)}.")
        
        ref = sp[0]
        indexes = np.arange(ref.size)
        shifts = np.zeros(ref.size)
        shifted: list[Spectrum] = []
        
        for m, s in zip(self, sp[1:]):
            shifts += m(indexes)
            shifted.append(Spectrum(np.interp(indexes, indexes - shifts, s.data)))
        
        return Spectra(freqs=sp.freqs, spectra=[ref] + shifted)


@dataclass(frozen=True)
class SparsePeaksShiftMapCalculator:
    """Calculates a shift map from matched peaks using RBF interpolation."""

    def calculate(self, size: int, matches: list[tuple[Peak, Peak]]) -> ShiftMap:
        """Calculate a shift map from matched peaks.

        Parameters
        ----------
        size : int
            Size of the spectrum.
        matches : list of tuple of Peak
            List of matched peaks.

        Returns
        -------
        ShiftMap
            Calculated shift map.
        """
        # prepare control points and specify zero shift on borders
        points = np.array([pr.refined_index for pr, _ in matches] + [0, size-1]).reshape(-1, 1)
        values = np.array([pc.refined_index - pr.refined_index for pr, pc in matches] + [0, 0]).reshape(-1, 1)

        # interpolate/extrapolate using radial basis functions
        rbf = RBFInterpolator(points, values, kernel='linear')
        return ShiftMap(rbf)


type PeaksList = list[Peak]
type MatchesList = list[tuple[Peak, Peak]]


@dataclass(frozen=True)
class SparsePeaksShiftCorrector:
    """Corrects spectral shifts using detected peaks and shift maps.

    The detected peaks are matched between consecutive spectra and the matched
    pairs are used to compute shift maps.

    Parameters
    ----------
    peaks_finder : PeaksFinder, optional
        Peaks finder instance.
    peaks_matcher : PeaksMatcher, optional
        Peaks matcher instance.
    shift_map_calc : SparsePeaksShiftMapCalculator, optional
        Shift map calculator instance.
    """

    peaks_finder: PeaksFinder = NoiseStatisticsPeaksFinder()
    peaks_matcher: PeaksMatcher = NaiveStablePeaksTopMatcher()
    shift_map_calc: SparsePeaksShiftMapCalculator = SparsePeaksShiftMapCalculator()

    def estimate(self, sp: Spectra) -> tuple[list[PeaksList], list[MatchesList], ShiftMapsList]:
        """Estimate peaks, matches, and shift maps for a set of spectra.

        Parameters
        ----------
        sp : Spectra
            Spectra to process.

        Returns
        -------
        tuple
            (list of peaks, list of matches, ShiftMapsList)
        """
        peaks = [self.peaks_finder.find(s) for s in sp]

        matches = []
        smaps: list[ShiftMap] = []
        n = len(sp)
        
        for i, j in zip(range(0, n-1), range(1, n)):
            match = self.peaks_matcher.match(peaks[i], peaks[j], sp.resolution)
            matches.append(match)
            smap = self.shift_map_calc.calculate(sp[i].size, match)
            smaps.append(smap)

        return peaks, matches, ShiftMapsList(smaps)
    
    def correct(self, sp: Spectra) -> Spectra:
        """Correct a set of spectra for shifts.

        Parameters
        ----------
        sp : Spectra
            Spectra to correct.

        Returns
        -------
        Spectra
            Corrected spectra.
        """
        _, _, smaps = self.estimate(sp)
        return smaps.apply(sp)
