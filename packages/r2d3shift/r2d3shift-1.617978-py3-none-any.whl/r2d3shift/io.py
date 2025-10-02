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

"""Input/Output for 1.5D Spectra

Module for reading and writing 2D spectra data in CSV format, including support for zipped archives.
This module provides abstract base classes and concrete implementations for reading and writing
2D spectra data, specifically in CSV format. It also includes functionality to handle zipped
archives containing multiple spectra files. The spectra data is represented using the `Spectrum`
and `Spectra` classes from the `.signal` module.

Classes
-------
SpectraReader2D
    Abstract base class for reading 2D spectra from file-like objects.
CSVSpectraReader2D
    Concrete implementation for reading 2D spectra from CSV files.
SpectraWriter2D
    Abstract base class for writing 2D spectra to file-like objects.
CSVSpectraWriter2D
    Concrete implementation for writing 2D spectra to CSV files.
SpectraArchiveIOHandler2D
    Handles reading and writing zipped archives of spectra files.

Notes
-----
- The CSV format expects the first column to be frequency values and the subsequent columns to
  represent the real and imaginary parts of the spectra data.
- The zipped archive handler supports reading and writing multiple spectra files with a specified
  file extension (default is '.csv').

"""

import csv
import zipfile
from pathlib import Path
from abc import ABC, abstractmethod
from typing import Any
import io

import numpy as np

from .signal import Spectrum, Spectra


def _is_number(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


class SpectraReader2D(ABC):
    """Abstract base class for reading 2D spectra."""

    @abstractmethod
    def read(self, file_obj) -> Spectra:
        """Read spectra from a file-like object.

        Parameters
        ----------
        file_obj : file-like
            File object to read from.

        Returns
        -------
        Spectra
            Read spectra.
        """
        pass


class CSVSpectraReader2D(SpectraReader2D):
    """Reads spectra from a CSV file."""

    def read(self, file_obj) -> Spectra:
        reader = csv.reader((line.decode('utf-8') for line in file_obj), delimiter=';')

        freqs = []
        vals = []
        for row in reader:
            if row:
                if _is_number(row[0]):
                    # first column is the frequency, others are complex components
                    freqs.append(float(row[0]))
                    vals.append(row[1:])
                # else:  # skip header elements

        # group real and imaginary parts into complex numbers
        vals = np.array(vals, dtype=float)
        vals = vals[:, ::2] + 1j * vals[:, 1::2]

        return Spectra(freqs=freqs, spectra=[Spectrum(s) for s in vals.T])


class SpectraWriter2D(ABC):
    """Abstract base class for writing 2D spectra."""

    @abstractmethod
    def write(self, file_obj, sp: Spectra):
        """Write spectra to a file-like object.

        Parameters
        ----------
        file_obj : file-like
            File object to write to.
        sp : Spectra
            Spectra to write.
        """
        pass


class CSVSpectraWriter2D(SpectraWriter2D):
    """Writes spectra to a CSV file."""

    def write(self, file_obj, sp: Spectra):
        with io.TextIOWrapper(file_obj, encoding='utf-8') as txt_file_obj:
            writer = csv.writer(txt_file_obj, delimiter=';')

            freqs = sp.freqs

            data = np.array([s.data for s in sp]).T
            vals = np.zeros((data.shape[0], data.shape[1]*2))
            vals[:, ::2] = np.real(data)
            vals[:, 1::2] = np.imag(data)

            rows = [(f, *v) for f, v in zip(freqs, vals)]
            writer.writerows(rows)


class SpectraArchiveIOHandler2D:
    """Handles reading and writing zipped archives of spectra files."""

    def __init__(self):
        self._delegates = {
            '.csv': (CSVSpectraReader2D(), CSVSpectraWriter2D()),
        }

    def read(self, archive: Path, filetype: str = '.csv') -> dict[str, Spectra]:
        """Read all spectra from a zipped archive.

        Parameters
        ----------
        archive : Path
            Path to the archive.
        filetype : str, optional
            File extension to read (default is '.csv').

        Returns
        -------
        dict of str to Spectra
            Dictionary mapping names to Spectra objects.
        """
        if not filetype in self._delegates:
            raise ValueError(f"No reader registered for extension '{filetype}'")
        
        with zipfile.ZipFile(archive, 'r') as zf:
            reader = self._delegates[filetype][0]
            data = {}
            for filename in zf.namelist():
                if self._get_extension(filename) == filetype:
                    with zf.open(filename) as file_obj:
                        name = self._get_name(filename, filetype)
                        data[name] = reader.read(file_obj)
            return data
    
    def write(self, archive: Path, data: dict[str, Spectra], filetype: str = '.csv') -> None:
        """Write all spectra to a zipped archive.

        Parameters
        ----------
        archive : Path
            Path to the archive.
        data : dict of str to Spectra
            Data to write.
        filetype : str, optional
            File extension to write (default is '.csv').
        """
        if not filetype in self._delegates:
            raise ValueError(f"No writer registered for extension '{filetype}'")
        
        with zipfile.ZipFile(archive, 'w') as zf:
            writer = self._delegates[filetype][1]
            for name in data:
                with zf.open(f"{name}.csv", 'w') as file_obj:
                    writer.write(file_obj, data[name])

    @staticmethod
    def _get_extension(filename: str) -> str:
        return '.' + filename.split('.')[-1].lower()
    
    @staticmethod
    def _get_name(filename: str, filetype: str) -> str:
        return filename.split(filetype)[0]
