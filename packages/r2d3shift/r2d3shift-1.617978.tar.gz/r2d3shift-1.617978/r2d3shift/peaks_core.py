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

"""Core definitions for representing peaks in a spectrum.

This module provides the `Peak` dataclass, which encapsulates the properties
and comparison logic for a peak detected in a spectral dataset. It supports
refined sub-index positioning and comparison operations.

Classes
-------
Peak
    Represents a peak in a spectrum with index, height, and optional offset.

"""

from dataclasses import dataclass
from functools import cached_property

@dataclass(frozen=True)
class Peak:
    """Represents a peak in a spectrum.

    Parameters
    ----------
    index : int
        Index of the peak in the spectrum.
    height : float
        Height of the peak.
    offset : float, optional
        Sub-index offset for refined peak position (default is 0).
    """
    index: int
    height: float
    offset: float = 0

    def __sub__(self, other: 'Peak') -> float:
        """Compute the difference between peak indices.

        Parameters
        ----------
        other : Peak
            The other peak.

        Returns
        -------
        float
            Difference between indices.
        """
        return self.index - other.index

    def __lt__(self, other: 'Peak') -> bool:
        """Compare peaks by index.

        Parameters
        ----------
        other : Peak
            The other peak.

        Returns
        -------
        bool
            True if this peak's index is less than the other's.
        """
        return self.index < other.index
    
    @cached_property
    def refined_index(self) -> float:
        """Refined index of the peak (index + offset).

        This refined index accounts for sub-index precision.

        Returns
        -------
        float
            Refined index.
        """
        return self.index + self.offset
