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

"""NMR spectra representations

This module provides classes for representing and manipulating NMR spectra and 
collections of spectra.

Classes
-------
Spectrum
    Represents a single NMR spectrum, providing access to its data, shape, and 
    properties such as real, imaginary, and magnitude components.

Spectra
    Represents a collection of Spectrum objects, typically acquired under different
    experimental conditions (e.g., relaxation times). Provides methods for accessing, 
    slicing, and integrating spectra, as well as retrieving frequency information for peaks.

"""

from dataclasses import dataclass
from typing import Iterator, overload

import numpy as np

from .peaks_core import Peak


@dataclass(frozen=True)
class Spectrum:
    """Represents a single spectrum.

    Parameters
    ----------
    data : np.ndarray
        The spectrum data as a numpy array.
    """

    data: np.ndarray

    @property
    def shape(self) -> tuple[int, ...]:
        """tuple of int: Shape of the spectrum data."""
        return self.data.shape
    
    @property
    def size(self) -> int:
        """int: Number of points in the spectrum data."""
        return self.data.size
    
    @property
    def dtype(self):
        """data-type: Data type of the spectrum (most-likely complex for NMR)."""
        return self.data.dtype
    
    @property
    def real(self) -> np.ndarray:
        """np.ndarray: Real part of the spectrum."""
        return np.real(self.data)
    
    @property
    def imag(self) -> np.ndarray:
        """np.ndarray: Imaginary part of the spectrum."""
        return np.imag(self.data)
    
    @property
    def mag(self) -> np.ndarray:
        """np.ndarray: Magnitude of the spectrum."""
        return np.abs(self.data)
    
    def __getitem__(self, idx):
        """Get spectrum value at given point index."""
        return self.data[idx]
    
    def __repr__(self) -> str:
        """str: String representation of the Spectrum."""
        return f"Spectrum(size={self.size}, dtype={self.dtype})"


@dataclass(frozen=True)
class Spectra:
    """Represents a collection of spectra.

    The collection usually contains multiple spectra acquired under different 
    conditions. For the purpose of this project, the condition is about relaxation time.

    Parameters
    ----------
    freqs : list of float
        List of frequency values.
    spectra : list of Spectrum
        List of Spectrum objects.
    """

    freqs: list[float]
    spectra: list[Spectrum]

    @property
    def resolution(self) -> float:
        """float: Frequency resolution."""
        return self.freqs[1] - self.freqs[0]

    @property
    def shape(self) -> tuple[int, int]:
        """tuple of int: Shape of the spectra (number of spectra, spectrum size)."""
        return len(self.spectra), self.spectra[0].size if self.spectra else 0
    
    @property
    def dtype(self):
        """data-type: Data type of the spectra (most-likely complex for NMR)."""
        return self.spectra[0].dtype if self.spectra else None
    
    @property
    def real(self) -> np.ndarray:
        """np.ndarray: Real part of all spectra."""
        return np.array([s.real for s in self.spectra])
    
    @property
    def imag(self) -> np.ndarray:
        """np.ndarray: Imaginary part of all spectra."""
        return np.array([s.imag for s in self.spectra])
    
    @property
    def mag(self) -> np.ndarray:
        """np.ndarray: Magnitude of all spectra."""
        return np.array([s.mag for s in self.spectra])
    
    @overload
    def __getitem__(self, index: int) -> Spectrum: ...
    @overload
    def __getitem__(self, index: slice) -> 'Spectra': ...

    def __getitem__(self, index: int | slice) -> 'Spectrum | Spectra':
        """Select a Spectrum or a slice of Spectra.

        Parameters
        ----------
        index : int or slice
            Index or slice to access spectra.

        Returns
        -------
        Spectrum or Spectra
            The selected Spectrum or a new Spectra object.
        """
        if isinstance(index, slice):
            return Spectra(self.freqs, self.spectra[index])
        return self.spectra[index]
    
    def __iter__(self) -> Iterator[Spectrum]:
        """Iterator over Spectrum objects."""
        return iter(self.spectra)
    
    def __len__(self) -> int:
        """int: Number of spectra."""
        return len(self.spectra)
    
    def __repr__(self) -> str:
        """str: String representation of the Spectra."""
        return f"Spectra(shape={self.shape}, dtype={self.dtype})"
    
    def sum(self) -> Spectrum:
        """Integrate all spectra.

        Returns
        -------
        Spectrum
            The sum of all spectra as a Spectrum object.
        """
        return Spectrum(np.array([s.data for s in self.spectra]).sum(axis=0))
    
    def freq(self, p: Peak) -> float:
        """Get the frequency value for a given refined peak.

        Note that the refined index of the peak is taken into account.
        That means the frequency has a sub-resolution precision.

        Parameters
        ----------
        p : Peak
            The peak for which to get the frequency.

        Returns
        -------
        float
            The frequency value.
        """
        return self.freqs[p.index] + self.resolution*p.offset
