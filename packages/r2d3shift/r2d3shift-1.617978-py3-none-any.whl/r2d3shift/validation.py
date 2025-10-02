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

"""Tools for validating shift correction in spectra.

This module provides tools for validating shift correction in spectral data. 
It includes classes and methods for comparing peak properties, matching peaks, 
evaluating shift trajectories, and computing signal-to-noise ratios before and 
after correction.

Classes
-------
PeakProps
    Calculates properties (height, width at half height) of a peak in a spectrum.

ShiftCorrectionValidator
    Provides methods to validate shift correction qualitatively and quantitatively, 
    including peak matching, trajectory analysis, and pSNR computation.

"""

from dataclasses import dataclass
from functools import cached_property
from typing import Optional

import numpy as np
import pandas as pd

from .signal import Spectrum, Spectra
from .noise import NoiseRegionDetector
from .peaks import Peak, PeaksFinder, NoiseStatisticsPeaksFinder, PeaksMatcher, NaiveStablePeaksTopMatcher
from .shift import SparsePeaksShiftCorrector


@dataclass(frozen=True)
class PeakProps:
    """Calculated properties of a peak in a spectrum.

    In addition to standard real/height, the with at half 
    height is computed.

    Parameters
    ----------
    peak : Peak
        The peak object.
    data : Spectrum
        The spectrum data.
    """

    peak: Peak
    data: Spectrum

    @cached_property
    def real(self) -> np.ndarray:
        """np.ndarray: Real part of the spectrum data."""
        return self.data.real

    @cached_property
    def height(self) -> float:
        """float: Height of the peak."""
        return self.peak.height
    
    @cached_property
    def width(self) -> float:
        """float: Width of the peak at half height."""
        half_height = self.height / 2

        # left descent
        lindex = self.peak.index
        while self.real[lindex] > half_height:
            lindex -= 1
        
        # right descent
        rindex = self.peak.index
        while self.real[rindex] > half_height:
            rindex += 1
        
        # calculate width at half height
        return float(abs(rindex - lindex))

@dataclass(frozen=True)
class ShiftCorrectionValidator:
    """Validator for shift correction in spectra.

    This class provides methods to validate qualitatively and 
    quantitatively the shift correction.

    Parameters
    ----------
    finder : PeaksFinder, optional
        Peaks finder instance.
    matcher : PeaksMatcher, optional
        Peaks matcher instance.
    detector : NoiseRegionDetector, optional
        Noise region detector instance.
    corrector : SparsePeaksShiftCorrector, optional
        Shift corrector instance.
    """

    finder: PeaksFinder = NoiseStatisticsPeaksFinder()
    matcher: PeaksMatcher = NaiveStablePeaksTopMatcher()
    detector: NoiseRegionDetector = NoiseRegionDetector()
    corrector: SparsePeaksShiftCorrector = SparsePeaksShiftCorrector()

    def match_integrated_peaks(self, sp: Spectra, csp: Spectra) -> list[tuple[Peak, Peak]]:
        """Match peaks between integrated original and corrected spectra.

        Parameters
        ----------
        sp : Spectra
            Original spectra.
        csp : Spectra
            Corrected spectra.

        Returns
        -------
        list of tuple of Peak
            List of matched peaks.
        """
        sp_int = sp.sum()
        sp_peaks = self.finder.find(sp_int)

        csp_int = csp.sum()
        csp_peaks = self.finder.find(csp_int)

        return self.matcher.match(sp_peaks, csp_peaks)

    def validate_integrated_peaks(self, sp: Spectra, csp: Spectra) -> pd.DataFrame:
        """Validate peak properties between integrated original and corrected spectra.

        Parameters
        ----------
        sp : Spectra
            Original spectra.
        csp : Spectra
            Corrected spectra.

        Returns
        -------
        pd.DataFrame
            DataFrame with height and width change ratios.
        """
        sp_int = sp.sum()
        csp_int = csp.sum()
        matches = self.match_integrated_peaks(sp, csp)
        pprops = [(PeakProps(p1, sp_int), PeakProps(p2, csp_int)) for p1, p2 in matches]
        heights, widths = list(zip(*[(p2.height/p1.height - 1, p2.width/p1.width - 1) 
                                    for p1, p2 in pprops]))
        
        return pd.DataFrame({'height': heights, 'width': widths})

    def validate_shift_tracjectories(self, sp: Spectra) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """Validate shift trajectories for a set of spectra.

        Parameters
        ----------
        sp : Spectra
            Spectra to validate.

        Returns
        -------
        tuple of pd.DataFrame
            (trajectories, normalized trajectories, statistics)
        """
        _, _, smaps = self.corrector.estimate(sp)

        # calculate trajectories from shift maps and initial peaks
        ref = sp[0]
        traces = []
        idx = np.array([p.refined_index for p in self.finder.find(ref)])
        traces.append(idx)

        for smap in smaps:
            idx = idx + smap(idx)
            traces.append(idx)

        # calculate deviation from perfect trajectories
        traces = np.array(traces)
        df_traces = pd.DataFrame(traces.T, columns=[f"#{i}" for i in range(1, len(sp)+1)])
        diff = traces - traces[0]
        df_norm_traces = pd.DataFrame(diff.T, columns=[f"#{i}" for i in range(1, len(sp)+1)])

        # calculate first-order statistics on deviation from perfect trajectories
        diff = np.abs(diff)
        df_stats = pd.DataFrame(np.vstack((diff.mean(axis=0), diff.sum(axis=0))).T,
                                columns=["Average deviation", "Total deviation"])

        return df_traces, df_norm_traces, df_stats
    
    @staticmethod
    def __pSNR(m: float, s: float) -> float:
        return 20 * np.log10(m/s)

    def validate_integrated_psnr(self, sp: Spectra, csp: Spectra) -> Optional[tuple[float, float]]:
        """Validate by computing the pSNR for integrated original and corrected spectra.

        Parameters
        ----------
        sp : Spectra
            Original spectra.
        csp : Spectra
            Corrected spectra.

        Returns
        -------
        tuple of float or None
            (pSNR original, pSNR corrected) or None if not computable.
        """
        # find reference peak
        sp_int = sp.sum()
        sp_peaks = sorted(self.finder.find(sp_int), key=lambda p: p.height, reverse=True)
        sp_max_peak = sp_peaks[0] if sp_peaks else None

        if sp_max_peak is None:
            return None
        
        # match with peak in corrected
        csp_int = csp.sum()
        csp_peaks = self.finder.find(csp_int)
        matches = self.matcher.match([sp_max_peak], csp_peaks)
        csp_max_peak = matches[0][1] if matches else None

        if csp_max_peak is None:
            return None
        
        # measure noise stats
        sp_noise = self.detector.detect(sp_int)
        sp_noise_mu = sp_int.real[sp_noise].mean()
        sp_noise_std = sp_int.real[sp_noise].std()

        csp_noise = self.detector.detect(csp_int)
        csp_noise_mu = sp_int.real[csp_noise].mean()
        csp_noise_std = sp_int.real[csp_noise].std()

        # calculate both pSNR
        return  (self.__pSNR(sp_max_peak.height-sp_noise_mu, sp_noise_std), 
                 self.__pSNR(csp_max_peak.height-csp_noise_mu, csp_noise_std))
    
    @staticmethod
    def __build_traj_recur(t, m):
        if m and m[0]:
            peaks = [p2 for p1, p2 in m[0] if p1 == t[-1]]
            if peaks:
                t.append(peaks[0])
                return ShiftCorrectionValidator.__build_traj_recur(t, m[1:])
        return t
    
    @staticmethod
    def __build_traj(m):
        return [ShiftCorrectionValidator.__build_traj_recur([p1, p2], m[1:]) 
                for p1, p2 in m[0]]
    
    def validate_peaks_matching(self, sp: Spectra) -> list[list[tuple[float, float]]]:
        """Validate matched peaks for a set of spectra.

        Parameters
        ----------
        sp : Spectra
            Spectra to validate.

        Returns
        -------
        list of list of tuple of float
            List of trajectories as (frequency, height) tuples.
        """
        _, matches, _ = self.corrector.estimate(sp)
        return [[(sp.freq(p), p.height) for p in t] for t in self.__build_traj(matches)]
