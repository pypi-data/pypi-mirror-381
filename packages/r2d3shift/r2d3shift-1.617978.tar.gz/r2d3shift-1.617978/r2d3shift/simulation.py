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

"""Tools for FID and frequency-domain spectra simulation.

This module provides lightweight simulators to generate FIDs (free induction
decays) from sums of exponential isochromats, apply degradations (for example
Gaussian noise in the time domain), compute FFT-based spectra, and simulate
frequency shifts across multiple indirect scans using shift models.

Isochromat representation
-------------------------
Each isochromat is represented as a 3-tuple (T1, T2, frequency) where:
- T1 : longitudinal relaxation time (seconds)
- T2 : transverse relaxation time (seconds)
- frequency : resonance frequency (ppm)

The FID contribution from a single isochromat uses both T1 and T2: the
transverse signal is weighted by the nutation/recovery factor
(1 - exp(-TR / T1)) and decays as exp(-t / T2) * exp(2j*pi*frequency*t).

Key classes and helpers
-----------------------
- FIDSignalDegradation: abstract base for time-domain degradations.
- GaussianNoiseDegradation: additive Gaussian noise model; construct via
  GaussianNoiseDegradation(sigma) or use the helper
  GaussianNoiseDegradation.from_pSNR(pSNR, fid) to derive a sigma from a
  pseudo-SNR and an example fid.
- FIDSignalSimulator: builds a complex FID from a list of isochromats
  (T1, T2, frequency) and accounts for repetition time (TR) when generating
  the signal amplitude.
- SpectrumSimulator: converts a FID into a frequency-domain Spectra object.
- ShiftModel: abstract base for generating per-scan frequency shifts.
- GeneralExponentialShiftModel: generates monotonic exponential-like shifts.
- RepetitionTimeEvolutionModel and implementations (e.g. GaussianRepetitionTimeEvolution)
  can be used to vary TR across indirect scans.
- ShiftedSpectraSimulator: synthesizes many shifted spectra using a shift
  model and an optional TR evolution model; it uses GaussianNoiseDegradation.from_pSNR
  to make noise consistent across scans.

Examples
--------
Create a simple FID from two isochromats (frequencies given in ppm) and obtain
the spectrum (freq axis returned in ppm):

>>> from r2d3shift.simulation import FIDSignalSimulator, SpectrumSimulator
>>> iso = [(1.2, 0.5, 0.01), (1.0, 0.3, -0.25)]  # (T1, T2, frequency) in seconds and ppm
>>> fid_sim = FIDSignalSimulator(isochromats=iso)
>>> t, fid = fid_sim(acq_time=0.5, bw=1024.0, TR=1.0, factor=1.0, magnet_freq=400e6)

Note: examples here are minimal; full downstream usage relies on the project's
Spectrum and Spectra datatypes for further processing and plotting.
"""

from dataclasses import dataclass, field
from typing import Optional, TypeVar
from abc import ABC, abstractmethod

import numpy as np

from .signal import Spectrum, Spectra


type IsochromatProperties = tuple[float, float, float]


class FIDSignalDegradation(ABC):
    """Abstract base class for time-domain FID degradations.

    Subclasses must implement the apply(s: np.ndarray) -> np.ndarray method to
    transform a complex-valued FID (1D numpy array) and return the degraded
    FID of the same shape.

    Notes
    -----
    Implementations should preserve dtype and shape of the input signal.
    """
    @abstractmethod
    def apply(self, s: np.ndarray) -> np.ndarray:
        """Apply the degradation to a complex FID.

        Parameters
        ----------
        s : numpy.ndarray
            Complex-valued 1D array representing the FID signal.

        Returns
        -------
        numpy.ndarray
            Degraded complex-valued FID array (same shape as `s`).
        """
        raise RuntimeError("Not meant to be instantiated!")


@dataclass(frozen=True)
class GaussianNoiseDegradation(FIDSignalDegradation):
    """Additive Gaussian white noise in the time domain.

    This class stores a noise standard deviation `sigma`. For convenience a
    factory method from_pSNR(pSNR, fid) computes an appropriate sigma from a
    pseudo-SNR (in dB) and an example FID amplitude.

    Parameters
    ----------
    sigma : float
        Standard deviation of the Gaussian noise to be added to both real and
        imaginary parts of the complex FID.

    Methods
    -------
    from_pSNR(pSNR, fid)
        Compute sigma from a pseudo-SNR (dB) and an example fid array.

    Examples
    --------
    >>> import numpy as np
    >>> from r2d3shift.simulation import GaussianNoiseDegradation
    >>> sig = np.ones(8, dtype=np.complex128)
    >>> noisy = GaussianNoiseDegradation.from_pSNR(40, sig).apply(sig)
    """
    sigma: float

    @staticmethod
    def from_pSNR(pSNR: float, fid: np.ndarray) -> 'GaussianNoiseDegradation':
        sigma_factor = 1 / 10**(pSNR / 20)
        sigma = sigma_factor * np.abs(np.fft.fft(fid, norm='ortho')).max()
        return GaussianNoiseDegradation(sigma)

    def apply(self, s: np.ndarray) -> np.ndarray:
        noise = np.random.normal(0, self.sigma, (2, len(s)))
        return s + noise[0] + 1j*noise[1]


def ppm_factor(magnet_freq: float) -> float:
    """Return the scaling factor (Hz per ppm) for a given magnet frequency.

    Parameters
    ----------
    magnet_freq : float
        Magnet's frequency in Hz (e.g. 400e6 for 400 MHz).

    Returns
    -------
    float
        Number of Hz corresponding to 1 ppm at the provided magnet frequency.
    """
    return magnet_freq / 1e6


T = TypeVar('T', float, np.ndarray)


def hz2ppm(hz: T, magnet_freq: float) -> T:
    """Convert frequencies in Hz to chemical shift in ppm.

    Parameters
    ----------
    hz : float or numpy.ndarray
        Frequency value(s) in Hz.
    magnet_freq : float
        Magnet's frequency in Hz used for the conversion.

    Returns
    -------
    float or numpy.ndarray
        Corresponding value(s) in ppm.
    """
    return hz / ppm_factor(magnet_freq)


def ppm2hz(ppm: T, magnet_freq: float) -> T:
    """Convert chemical shift in ppm to frequency in Hz.

    Parameters
    ----------
    ppm : float or numpy.ndarray
        Chemical shift value(s) in ppm.
    magnet_freq : float
        Magnet's frequency in Hz used for the conversion.

    Returns
    -------
    float or numpy.ndarray
        Corresponding value(s) in Hz.
    """
    return ppm * ppm_factor(magnet_freq)


@dataclass(frozen=True)
class FIDSignalSimulator:
    """Simulate a complex FID from a set of isochromats.

    Isochromat format
    -----------------
    Each isochromat is a tuple (T1, T2, frequency):
    - T1 : longitudinal relaxation time (s)
    - T2 : transverse relaxation time (s)
    - frequency : resonance frequency (ppm)

    Signal model
    ------------
    The transverse contribution of an isochromat at time t is:
        (1 - exp(-TR / T1)) * exp(-t / T2) * exp(2j * pi * f * t)
    where f is obtained from frequency via ppm2hz(frequency, magnet_freq).
    """
    isochromats: list[IsochromatProperties] = field(default_factory=lambda: [])
    degradations: list[FIDSignalDegradation] = field(default_factory=lambda: [])

    def add_isochromat(self, isochromat: IsochromatProperties) -> None:
        self.isochromats.append(isochromat)
    
    def add_degratation(self, degradation: FIDSignalDegradation) -> None:
        self.degradations.append(degradation)

    @staticmethod
    def __isofid(t: np.ndarray | float, T2: float, w: float) -> np.ndarray:
        return np.exp(-t/T2) * np.exp(2j*np.pi*w*t)

    def __fid(self, t: np.ndarray | float, TR: float, magnet_freq: float) -> np.ndarray:
        return np.array([(1-np.exp(-TR/T1)) * self.__isofid(t, T2, ppm2hz(w, magnet_freq)) 
                         for T1, T2, w in self.isochromats]).sum(axis=0)

    def __call__(self, acq_time: float, bw: float, TR: float = 1, factor: float = 1, 
                 magnet_freq: float = 400e6) -> tuple[np.ndarray, np.ndarray]:
        """Generate time axis and complex FID.

        Parameters
        ----------
        acq_time : float
            Total acquisition time in seconds.
        bw : float
            Bandwidth in Hz (samples per second).
        factor : float, optional
            Global amplitude scaling factor applied to the generated FID.
        TR : float, optional
            Repetition time in seconds used in the signal model.
        magnet_freq : float, optional
            Magnet's frequency (Hz) used to convert ppm to Hz.

        Returns
        -------
        t : numpy.ndarray
            1D array of time points.
        signal : numpy.ndarray
            Complex-valued FID sampled at `t`.
        """
        t = np.linspace(0, acq_time, int(np.floor(acq_time * bw)))
        signal = factor * self.__fid(t, TR, magnet_freq)

        for degradation in self.degradations:
            signal = degradation.apply(signal)

        return t, signal


@dataclass(frozen=True)
class SpectrumSimulator:
    """Convert a simulated FID into a frequency-domain Spectra object.

    Parameters
    ----------
    fid_simulator : FIDSignalSimulator
        Underlying FID simulator used to create the time-domain signal.

    Notes
    -----
    The simulator uses numpy.fft (with fftshift and norm='ortho') to compute
    frequency axis and complex spectrum. The returned Spectra object contains
    one Spectrum corresponding to the FFT of the simulated FID.
    """
    fid_simulator: FIDSignalSimulator

    def __call__(self, acq_time: float, bw: float, TR: float = 1, factor: float = 1,
                 magnet_freq: float = 400e6) -> Spectra:
        """Generate a Spectra object from FID simulation parameters.

        Parameters
        ----------
        acq_time : float
            Acquisition time in seconds.
        bw : float
            Bandwidth in Hertz.
        factor : float, optional
            Amplitude scaling factor passed to the underlying FID simulator.
        TR : float, optional
            Repetition time in seconds passed to the underlying FID simulator.
        magnet_freq : float, optional
            Magnet's frequency (Hz) used to convert ppm to Hz and for the
            underlying FID simulator.

        Returns
        -------
        Spectra
            Spectra dataclass with frequency axis and one Spectrum entry.
        """
        _, fid = self.fid_simulator(acq_time=acq_time, bw=bw, TR=TR, 
                                    factor=factor, magnet_freq=magnet_freq)
        freqs = hz2ppm(np.fft.fftshift(np.fft.fftfreq(len(fid)) * bw), magnet_freq)
        spect = np.fft.fftshift(np.fft.fft(fid, norm='ortho'))
        return Spectra(freqs=freqs.tolist(), spectra=[Spectrum(spect)])


class ShiftModel(ABC):
    """Abstract base for models that generate per-scan frequency shifts.

    Implementations must return a list of shifts (floats) of length `nb_scans`
    when called with the number of indirect scans to simulate.
    """
    @abstractmethod
    def __call__(self, nb_scans: int) -> list[float]:
        """Return a sequence of length `nb_scans` containing frequency shifts (offsets in Hertz)."""
        raise RuntimeError("Not meant to be instantiated!")


@dataclass(frozen=True)
class GeneralExponentialShiftModel(ShiftModel):
    """Generate monotonic exponential-like frequency shifts across scans.

    The model produces a sequence that starts at zero and approaches `max_shift`
    following an exponential-like law controlled by `beta`.

    Parameters
    ----------
    beta : float, optional
        Shape parameter. beta == 0 yields a linear ramp; beta == 1 yields an 
        exponential curve. Default is 0.8.
    max_shift : float, optional
        Final (maximum) shift in the same units as frequencies (Hz). Default 15.
    beta_std : float or None, optional
        Optional standard deviation for sampling beta from a normal
        distribution (stochastic shifting trajectories).
    max_shift_std : float or None, optional
        Optional standard deviation for sampling max_shift from a normal
        distribution (stochastic shifting trajectories).

    Examples
    --------
    For deterministic shifts:
    >>> model = GeneralExponentialShiftModel(beta=0.5, max_shift=10.0)
    >>> shifts = model(10)
    For stochastic shifts:
    >>> model = GeneralExponentialShiftModel(beta=0.5, max_shift=10.0, beta_std=0.1, max_shift_std=2.0)
    >>> shifts = model(10)
    """
    beta: float = 0.8
    max_shift: float = 15
    beta_std: Optional[float] = None
    max_shift_std: Optional[float] = None

    @staticmethod
    def __func(k: int, K: int, beta: float, max_shift: float) -> float:
        if beta == 0:
            return max_shift * k / K
        else:

            return max_shift * ((abs(max_shift) + 1)**(beta*k/K) - 1) / \
                  ((abs(max_shift) + 1)**beta - 1)

    @staticmethod
    def __sample_normal(param: float, param_std: Optional[float]) -> float:
        return np.random.normal(param, param_std) if param_std else param

    def __call__(self, nb_scans: int) -> list[float]:
        beta = max(self.__sample_normal(self.beta, self.beta_std), 0)
        max_shift = self.__sample_normal(self.max_shift, self.max_shift_std)
        return [self.__func(k, nb_scans-1, beta, max_shift) for k in range(nb_scans)]


@dataclass(frozen=True)
class RepetitionTimeEvolutionModel(ABC):
    """Abstract base for models that generate a sequence of TR values.

    Implementations must return a list of TR values (floats, in seconds) of
    length `nb_scans` given TR_min and TR_max bounds.
    """
    @abstractmethod
    def __call__(self, TR_min: float, TR_max: float, nb_scans: int) -> list[float]:
        """Return nb_scans repetition times between TR_min and TR_max."""
        raise RuntimeError("Not meant to be instantiated!")


@dataclass(frozen=True)
class GaussianRepetitionTimeEvolution(RepetitionTimeEvolutionModel):
    """Simple Gaussian-shaped evolution of TR across scans.

    Parameters
    ----------
    slope : float, optional
        Controls the width/decay of the Gaussian envelope applied to the
        TR progression. The returned TR values interpolate between TR_min and
        TR_max according to a Gaussian-shaped curve.
    """
    slope: float = -0.06

    def __call__(self, TR_min: float, TR_max: float, nb_scans: int) -> list[float]:
        return ((TR_max - TR_min) * np.exp(-0.06*np.arange(nb_scans)**2) + TR_min).tolist()


@dataclass(frozen=True)
class ShiftedSpectraSimulator:
    """Create a set of shifted spectra using a shift model and FID simulator.

    The simulator constructs per-scan isochromat lists by adding the shift
    produced by `shift_model` to each isochromat frequency, simulates the FID
    (with degradations such as Gaussian noise derived from pSNR) and returns a
    single Spectra object containing the stack of shifted spectra.

    Parameters
    ----------
    shift_model : ShiftModel
        Model used to produce per-scan frequency shifts.
    TR_model : RepetitionTimeEvolutionModel, optional
        Model used to produce repetition time (TR) values across the indirect
        scans. Defaults to GaussianRepetitionTimeEvolution().

    Examples
    --------
    >>> model = GeneralExponentialShiftModel(beta=0.5, max_shift=5.0)
    >>> ssim = ShiftedSpectraSimulator(shift_model=model)
    >>> ssim(isochromats=[(1.0, 0.4, 0.0)], nb_indirect=4, acq_time=0.1, bw=256.0, TR_min=0.8, TR_max=1.2, pSNR=40)
    """
    shift_model: ShiftModel
    TR_model: RepetitionTimeEvolutionModel = GaussianRepetitionTimeEvolution()

    def __call__(self, isochromats: list[IsochromatProperties], nb_indirect: int, 
                 acq_time: float, bw: float, TR_min: float, TR_max: float, factor: float = 1, 
                 pSNR: float = 40, magnet_freq: float = 400e6) -> Spectra:
        """Simulate shifted spectra.

        Parameters
        ----------
        isochromats : list of (T1, T2, frequency_ppm) tuples
            Isochromat frequencies are expected in ppm.
        nb_indirect : int
            Number of indirect scans (number of shifted spectra to simulate).
        acq_time : float
            Acquisition time in seconds.
        bw : float
            Bandwidth in Hertz.
        TR_min : float
            Minimum repetition time in seconds used by the TR_model.
        TR_max : float
            Maximum repetition time in seconds used by the TR_model.
        factor : float, optional
            Amplitude scaling factor passed to the underlying FID simulator.
        pSNR : float, optional
            Pseudo-SNR in dB used to compute a noise sigma via
            GaussianNoiseDegradation.from_pSNR(pSNR, fid).
        magnet_freq : float, optional
            Magnet Larmor frequency in Hz used to convert ppm to Hz and to
            express output frequencies in ppm.
        """
        shifts = {(T2, w): self.shift_model(nb_indirect) for _, T2, w in isochromats}
        shifted_isochromats_list = [[(T1, T2, w+shifts[T2, w][i]) for T1, T2, w in isochromats]
                                    for i in range(nb_indirect)]
        rep_times = self.TR_model(TR_min, TR_max, len(shifted_isochromats_list))

        sim_fid = FIDSignalSimulator(isochromats=isochromats)
        _, fid = sim_fid(acq_time=acq_time, bw=bw, TR=TR_max)
        degradations: list[FIDSignalDegradation] = [GaussianNoiseDegradation.from_pSNR(pSNR, fid)]

        shifted_spectra = []
        for shifted_isochromats, TR in zip(shifted_isochromats_list, rep_times):
            sim_fid = FIDSignalSimulator(isochromats=shifted_isochromats, degradations=degradations)
            sim = SpectrumSimulator(sim_fid)
            shifted_spectra.append(sim(acq_time=acq_time, bw=bw, TR=TR, factor=factor, magnet_freq=magnet_freq))

        return Spectra(freqs=shifted_spectra[0].freqs, 
                       spectra=[s.spectra[0] for s in shifted_spectra])
