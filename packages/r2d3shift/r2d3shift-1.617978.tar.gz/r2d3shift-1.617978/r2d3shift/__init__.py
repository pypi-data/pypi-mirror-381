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

"""A package for spectral shift correction with R2D3 sequence.

This package provides tools for handling spectra, performing shift correction using 
sparse peaks, and managing spectral archives.

Modules
-------
- signal: Contains classes for representing and manipulating spectra.
- io: Provides handlers for reading and writing spectral archives.
- peaks_core: Core representations and operations for spectral peaks.
- peaks: High-level peak detection and matching operations.
- noise: Operations for noise estimation in spectral data.
- shift: Implements shift correction algorithms.
- cli: Command-line interface for interacting with the package.
- plot: Visualization tools for spectra and shifts correction results.
- validation: Tools for validating shift correction results.
- version: Contains the package version information.

Classes
-------
Spectrum
    Represents a single spectrum.
Spectra
    Represents a collection of spectra.
SpectraArchiveIOHandler2D
    Handler for reading and writing 2D spectral archives.
SparsePeaksShiftCorrector
    Performs shift correction using sparse peaks.

Examples
--------

To process and correct a single spectrum loaded as a numpy array and put
the corrected spectrum in a new numpy array:

>>> # assume `data` is a 2D numpy array and `freqs` is a 1D numpy array of frequencies
>>> from r2d3shift import Spectrum, Spectra, SparsePeaksShiftCorrector
>>> sp = Spectra(freqs, [Spectrum(row) for row in data])
>>> corrector = SparsePeaksShiftCorrector()
>>> csp = corrector.correct(sp)
>>> cdata = np.array([s.data for s in csp.spectra])

To process and correct all the spectra contained in an archive and save the 
corrected spectra in a new archive:

>>> from r2d3shift import SpectraArchiveIOHandler2D, SparsePeaksShiftCorrector
>>> handler = SpectraArchiveIOHandler2D()
>>> data = handler.load('path/to/archive.zip', '.csv')
>>> corrector = SparsePeaksShiftCorrector()
>>> corrected = {name: corrector.correct(sp) for name, sp in data.items()}
>>> handler.write('path/to/corrected_archive.zip', corrected)

"""

from .signal import Spectrum, Spectra
from .io import SpectraArchiveIOHandler2D
from .shift import SparsePeaksShiftCorrector
from .simulation import GeneralExponentialShiftModel, ShiftedSpectraSimulator
from .version import __version__


__all__ = [
    'Spectrum',
    'Spectra',
    'SpectraArchiveIOHandler2D',
    'SparsePeaksShiftCorrector',
    'GeneralExponentialShiftModel',
    'ShiftedSpectraSimulator'
]
