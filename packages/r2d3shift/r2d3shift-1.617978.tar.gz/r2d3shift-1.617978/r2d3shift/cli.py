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

"""R2D3Shift command line interface (CLI)"""

from pathlib import Path

import click
from rich_click import RichGroup
from rich.console import Console
from rich.table import Table
from rich import box
from matplotlib import pyplot as plt

from .version import __version__
from .signal import Spectra
from .io import SpectraArchiveIOHandler2D
from .peaks import NoiseRegionDetector, NoiseStatisticsPeaksFinder, NaiveStablePeaksTopMatcher, PeakRefiner
from .shift import SparsePeaksShiftCorrector
from .validation import ShiftCorrectionValidator
from .plot import ShiftCorrectionResultsPlotter
from .simulation import GeneralExponentialShiftModel, ShiftedSpectraSimulator


def __load_archive(archive: Path) -> dict[str, Spectra]:
    console = Console()

    console.rule("Dataset reading")
    console.print(f"Using archive: \"{archive}\".")

    with console.status("[bold green]Reading archive") as _:
        try:
            handler = SpectraArchiveIOHandler2D()
            data = handler.read(archive, '.csv')
        except IOError as ex:
            console.print(f"[red]An error occurted while reading: {ex}")
            exit(1)
    
    console.print(f"[green]:heavy_check_mark: Red {len(data)} spectra from the archive.")

    table = Table(box=box.SIMPLE_HEAD)
    table.add_column("Name", justify='left', style='dim')
    table.add_column("Shape", justify='center')

    for name in data:
        table.add_row(name, ' x '.join(str(e) for e in data[name].shape))
        
    console.print(table)

    return data


@click.group(cls=RichGroup)
@click.version_option(__version__, '--version', '-v', 
                      message="R2D3Shift version: %(version)s", 
                      help="Show the version and exit.")
@click.help_option('--help', '-h', help="Show this message and exit.")
def cli():
    """R2D3Shift is a tool to fix the misalignments of spectra from R2D3 sequence
    due to varying thermal conditions.
    """

    console = Console()

    console.print("[bold]Welcome to R2D3-Shift CLI!", justify='center')


@cli.group(cls=RichGroup)
@click.help_option('--help', '-h', help="Show this message and exit.")
@click.argument('archive', required=True,
                type=click.Path(exists=True, dir_okay=False, readable=True, path_type=Path))
@click.option('--iterative-signal-detector-sigma', '-s', type=click.FloatRange(2, 5), default=3, show_default=True,
              help="The sigma factor parameter of the iterative thresholding algorithm that split noise and signal regions.")
@click.option('--peak-prominence', '-pp', type=click.FloatRange(1, 10), default=5, show_default=True,
              help="Minimal prominence of detected peaks in terms of factor of noise's standard deviation.")
@click.option('--peak-height', '-ph', type=click.FloatRange(1, 10), default=6, show_default=True,
              help="Minimal height of detected peaks in terms of factor of noise's standard deviation.")
@click.option('--max-matching-distance', '-m', type=click.FloatRange(min=0, min_open=True), default=0.02, show_default=True,
              help="Maximal distance in ppm between peaks of two successive spectra to be matchable.")
@click.option('--fine-precision/--rough-precision', '-f/-r', is_flag=True, default=True, show_default=True,
              help="Use fine or rough precision in peak localization.")
@click.pass_context
def process(ctx: click.core.Context, archive: Path, iterative_signal_detector_sigma: float, peak_prominence: float, 
        peak_height: float, max_matching_distance: float, fine_precision: bool):
    """Commands to fix shifted datasets and save or show the results.
    
    ARCHIVE is the path to an existing (zip) archive file that contains csv files
    of drifted spectra to correct.
    """
    ctx.obj = {'archive': archive, 
               'sigma_factor': iterative_signal_detector_sigma,
               'peak-prominence': peak_prominence, 
               'peak-height': peak_height,
               'max-matching-distance': max_matching_distance,
               'fine-precision': fine_precision}


@process.command
@click.help_option('--help', '-h', help="Show this message and exit.")
@click.pass_context
def show(ctx: click.core.Context):
    """Show the results of the shift correction and their validation."""

    data = __load_archive(ctx.obj['archive'])

    console = Console()
    console.rule("Results and validation showing")

    noise_detector = NoiseRegionDetector(sigma_factor=ctx.obj['sigma_factor'])
    peaks_finder = NoiseStatisticsPeaksFinder(
        noise_detector=noise_detector,
        prominence_sigma_factor=ctx.obj['peak-prominence'],
        thresh_sigma_factor=ctx.obj['peak-height'],
        refiner=PeakRefiner() if ctx.obj['fine-precision'] else None)
    peaks_matcher = NaiveStablePeaksTopMatcher(
        freq_upper_threshold=ctx.obj['max-matching-distance'])
    corrector = SparsePeaksShiftCorrector(
        peaks_finder=peaks_finder,
        peaks_matcher=peaks_matcher)
    validator = ShiftCorrectionValidator(
        finder=corrector.peaks_finder, 
        matcher=corrector.peaks_matcher, 
        corrector=corrector)

    for name in data:
        with console.status(f"[bold green]Working on \"{name}\"..."):
            sp = data[name]
            csp = corrector.correct(sp)
            console.print(":heavy_check_mark: Shift correction done")

            plotter = ShiftCorrectionResultsPlotter(name, sp, csp, validator)
            
            plotter.plot_results()
            console.print(":heavy_check_mark: Results validation done")

            plotter.plot_shift_map()
            console.print(":heavy_check_mark: Shift map done")

            plotter.plot_trajectories_deviation()
            console.print(":heavy_check_mark: Trajectories deviation done")

            plotter.plot_peaks_props_change()
            console.print(":heavy_check_mark: Peaks properties change done")
        
        console.print(f"[green]:heavy_check_mark: \"{name}\" processed.")

        plt.show()


@process.command
@click.help_option('--help', '-h', help="Show this message and exit.")
@click.pass_context
@click.argument('output', type=click.Path(dir_okay=False, writable=True, path_type=Path))
def save(ctx: click.core.Context, output: Path):
    """Batch-process input dataset and save the results.
    
    OUTPUT is the path to the archive in which the corrected dataset will be saved.
    """

    data = __load_archive(ctx.obj['archive'])
    cdata = {}

    console = Console()
    console.rule("Data processing")

    noise_detector = NoiseRegionDetector(sigma_factor=ctx.obj['sigma_factor'])
    peaks_finder = NoiseStatisticsPeaksFinder(
        noise_detector=noise_detector,
        prominence_sigma_factor=ctx.obj['peak-prominence'],
        thresh_sigma_factor=ctx.obj['peak-height'],
        refiner=PeakRefiner() if ctx.obj['fine-precision'] else None)
    peaks_matcher = NaiveStablePeaksTopMatcher(
        freq_upper_threshold=ctx.obj['max-matching-distance'])
    corrector = SparsePeaksShiftCorrector(
        peaks_finder=peaks_finder,
        peaks_matcher=peaks_matcher)

    with console.status("[bold green]Processing..."):
        for name in data:
            try:
                cdata[name] = corrector.correct(data[name])
                console.print(f":heavy_check_mark: \"{name}\" done")
            except Exception as ex:
                console.print(f":cross_mark: error with \"{name}\": {ex}")
    
    with console.status("[bold green]Writing archive"):
        try:
            handler = SpectraArchiveIOHandler2D()
            handler.write(output, cdata)
        except IOError as ex:
            console.print(f"[red]An error occurred while writing file: {ex}")
            exit(1)
    
    console.print(f"[green]:heavy_check_mark: All spectra processed and saved.")


@cli.command
@click.help_option('--help', '-h', help="Show this message and exit.")
@click.argument('output', type=click.Path(dir_okay=False, writable=True, path_type=Path))
@click.argument('isochromats_desc', nargs=-1, type=click.STRING, metavar='[T1,T2,w]...', required=True)
@click.option('--beta', '-b', type=click.FloatRange(min=0), default=0.7, show_default=True,
              help="Beta parameter of the general exponential shift model.")
@click.option('--beta-std', '-bs', type=click.FloatRange(min=0, min_open=True), default=0.5, show_default=True,
              help="Standard deviation of the beta parameter of the general exponential shift model.")
@click.option('--max-shift', '-ms', type=click.FLOAT, default=0.001, show_default=True,
              help="Maximum shift value for the general exponential shift model.")
@click.option('--max-shift-std', '-mss', type=click.FloatRange(min=0, min_open=True), default=0.01, show_default=True,
              help="Standard deviation of the maximum shift value for the general exponential shift model.")
@click.option('--nb-indirect', '-n', type=click.IntRange(min=2, max=100), default=10, show_default=True,
              help="Number of indirect shifts to simulate.")
@click.option('--acq-time', '-t', type=click.FloatRange(min=0, max_open=True), default=60, show_default=True,
              help="Acquisition time of each FID in seconds.")
@click.option('--bandwidth', '-bw', type=click.FloatRange(min=0, min_open=True), default=1_000, show_default=True,
              help="Acquisition bandwidth in Hz.")
@click.option('--pSNR', '-ps', type=click.FloatRange(min=0), default=60, show_default=True,
              help="Peak signal to noise ratio of the simulated spectra in dB.")
@click.option('--TR-min', '-tri', type=click.FloatRange(min=0, min_open=True), default=0.2, show_default=True,
              help="Minimum repetition time in seconds.")
@click.option('--TR-max', '-tra', type=click.FloatRange(min=0, min_open=True), default=2, show_default=True,
              help="Maximum repetition time in seconds.")
@click.option('--magnet-freq', '-mf', type=click.FloatRange(min=0, min_open=True), default=400, show_default=True,
              help="Magnet main frequency in MHz.")
def simulate(output: Path, isochromats_desc: list[str], beta: float, beta_std: float, max_shift: float, 
             max_shift_std: float, nb_indirect: int, acq_time: float, bandwidth: float, psnr: float,
             tr_min: float, tr_max: float, magnet_freq: float):
    """Commands to generate synthetic shifted spectra.
    
    OUTPUT is the path to the archive in which the simulated dataset will be saved.

    T1,T2,w are the properties of each isochromat to simulate: T1 is longitudinal relaxation 
    in seconds, T2 is the transversal relaxation time in seconds and w is the frequency in ppm. 
    For example for two isochromats: 2,0.1,0.025 1,1.2,-0.35 5,0.5,1
    """
    console = Console()

    try:
        isochromats = [(float(T1), float(T2), float(w)) 
                       for T1, T2, w in (s.split(',') for s in isochromats_desc)]
    except Exception:
        console.print(f":cross_mark: unable to read the isochromats description; did you write it correctly?: {isochromats_desc}")
        exit(1)

    console.rule("Data simulating")

    with console.status("[bold green]Simulating..."):
        shift_model = GeneralExponentialShiftModel(beta=beta, beta_std=beta_std, max_shift=max_shift, max_shift_std=max_shift_std)
        ssim = ShiftedSpectraSimulator(shift_model)
        spectra = ssim(isochromats=isochromats, nb_indirect=nb_indirect, acq_time=acq_time, bw=bandwidth, pSNR=psnr,
                       TR_min=tr_min, TR_max=tr_max, magnet_freq=magnet_freq*1e6)
    console.print(f"[green]:heavy_check_mark: Synthetic data has been generated.")

    with console.status("[bold green]Writing archive"):
        try:
            handler = SpectraArchiveIOHandler2D()
            handler.write(output, {'simulated': spectra})
        except IOError as ex:
            console.print(f"[red]An error occurred while writing file: {ex}")
            exit(1)
    console.print(f"[green]:heavy_check_mark: Synthetic data has been saved.")
