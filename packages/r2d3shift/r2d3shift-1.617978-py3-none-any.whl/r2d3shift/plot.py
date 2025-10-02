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

"""Plotting utilities for shift correction results and validation.

This module provides the `ShiftCorrectionResultsPlotter` dataclass, which offers a 
suite of plotting methods to visualize the results of spectral shift correction, including 
overlays, integrations, peak trajectories, shift maps, and changes in peak properties.

Functions
---------
- plot_results(self): 
    Plot overlays, integrations, and peak trajectories for original and corrected spectra.
- plot_shift_map(self): 
    Plot the shift map for the original spectra.
- plot_peaks_props_change(self): 
    Plot the change in peak properties (height and width) after correction.
- plot_trajectories_deviation(self): 
    Plot the deviation of peak trajectories before and after correction.

Classes
-------
ShiftCorrectionResultsPlotter
    Dataclass for plotting shift correction results and validation.

"""

from dataclasses import dataclass
import colorsys as cs

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

from .signal import Spectra
from .validation import ShiftCorrectionValidator


@dataclass(frozen=True)
class ShiftCorrectionResultsPlotter:
    """Plotting utilities for shift correction results and validation.

    Parameters
    ----------
    name : str
        Name of the dataset or experiment.
    sp : Spectra
        Original spectra.
    csp : Spectra
        Corrected spectra.
    validator : ShiftCorrectionValidator, optional
        Validator instance for shift correction (default: new instance).
    """

    name: str
    sp: Spectra
    csp: Spectra
    validator: ShiftCorrectionValidator = ShiftCorrectionValidator()

    @staticmethod
    def __plot_overlay(axe, sp):
        for s in sp:
            axe.plot(sp.freqs, s.real, '-k', alpha=0.3)
        axe.set_xlabel("Frequency [ppm]")
        axe.set_yticks([])
        axe.invert_xaxis()

    @staticmethod
    def __plot_integration(axe, sps, labels):
        scaling = sps[0][0].real.sum() / sps[0].sum().real.sum()
        for label, sp in zip(labels, sps):
            sp_int = sp.sum().real
            axe.plot(sp.freqs, sp_int * scaling, '-', label=label)
        axe.set_xlabel("Frequency [ppm]")
        axe.set_yticks([])
        axe.invert_xaxis()
        axe.legend()
        return scaling

    def __plot_peaks(self, axe, sp, ref_peaks=None, scaling=1):
        if ref_peaks is None:
            ref_peaks = self.validator.finder.find(sp[0])

        for i, p in enumerate(ref_peaks):
            idx = sp.freq(p)
            height = p.height * scaling
            axe.annotate(str(i), ha='center', xy=(idx, height),
                         xytext=(idx, height*1.02))
    
    def __plot_trajectories(self, axe, sp):
        trajectories = self.validator.validate_peaks_matching(sp)
        colors = [cs.hsv_to_rgb(h, 0.8, 0.8) 
                  for h in np.linspace(0, 1, len(trajectories), endpoint=False)]
        np.random.seed(0)
        np.random.shuffle(colors)  # to avoid close similar colors

        for trajectory, color in zip(trajectories, colors):
            axe.plot(*list(zip(*trajectory)), '.', color=color)

    def plot_results(self):
        """Plot overlay, integration, and peak trajectories for original and corrected spectra."""
        psnr = self.validator.validate_integrated_psnr(self.sp, self.csp)
        if psnr is None:
            sp_psnr, csp_psnr = None, None
        else:
            sp_psnr, csp_psnr = psnr

        fig, axes = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(15, 5))

        self.__plot_overlay(axes[0], self.sp)
        self.__plot_peaks(axes[0], self.sp)
        self.__plot_trajectories(axes[0], self.sp)
        axes[0].set_title("Original")

        self.__plot_overlay(axes[1], self.csp)
        self.__plot_peaks(axes[1], self.csp)
        self.__plot_trajectories(axes[1], self.csp)
        axes[1].set_title("Corrected")

        scaling = self.__plot_integration(axes[2], [self.sp, self.csp], ["Original", "Corrected"])
        matches = self.validator.match_integrated_peaks(self.sp, self.csp)
        self.__plot_peaks(axes[2], self.csp, ref_peaks=list(zip(*matches))[1], scaling=scaling)
        axes[2].set_title("Integration")

        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
        axes[2].text(x=0.02, y=0.95, s=f"pSNR original: {sp_psnr:.2f} dB", 
                     transform=axes[2].transAxes, color=colors[0])
        axes[2].text(x=0.02, y=0.90, s=f"pSNR corrected: {csp_psnr:.2f} dB", 
                     transform=axes[2].transAxes, color=colors[1])

        fig.suptitle(f"Shifting correction results for \"{self.name}\"")
        fig.tight_layout()
    

    def plot_shift_map(self):
        """Plot the shift map for the original spectra."""
        _, _, smaps = self.validator.corrector.estimate(self.sp)
        full_smap = smaps.complete_shift_map(self.sp[0])
        vmin, vmax = np.percentile(full_smap, [2.5, 97.5])
        amax = max(abs(vmin), abs(vmax))

        fig, axe = plt.subplots(figsize=(8, 5))
        axe.imshow(full_smap, aspect='auto', cmap='RdBu_r', vmin=-amax, vmax=amax,
                   extent=(self.sp.freqs[0], self.sp.freqs[-1], len(self.sp)-1, 0))
        axe.invert_xaxis()
        axe.set_title("Shift Map")
        axe.set_xlabel("Frequency [ppm]")
        axe.set_ylabel("Spectrum Index")
        fig.colorbar(axe.images[0], ax=axe, orientation='vertical')

        fig.suptitle(f"Shifting map for \"{self.name}\"")
        fig.tight_layout()

    def plot_peaks_props_change(self):
        """Plot the change in peak properties (height and width) after correction."""
        # display percentages so scale the change ratios by 100
        int_peaks_props = self.validator.validate_integrated_peaks(self.sp, self.csp) * 100

        g = sns.JointGrid(data=int_peaks_props, x='width', y='height', height=10)
        g.plot_joint(sns.scatterplot, alpha=0.7)

        g.plot_marginals(sns.pointplot, color='black', alpha=0.5, errorbar='ci', marker='+', 
                         markersize=15, markeredgewidth=3)
        g.plot_marginals(sns.stripplot, alpha=0.7)

        for i in int_peaks_props.index:
            row = int_peaks_props.loc[i]
            g.ax_joint.annotate(str(i), xy=(row["width"], row["height"]))

        g.refline(x=0, y=0)
        g.set_axis_labels("Width change [%]", "Height change [%]")
        g.figure.suptitle(f"Integrated peak properties change after correction for \n\"{self.name}\"")
        g.figure.tight_layout()
    
    def plot_trajectories_deviation(self):
        """Plot the deviation of peak trajectories before and after correction."""
        _, sp_df_traces, sp_df_stats = self.validator.validate_shift_tracjectories(self.sp)
        _, csp_df_traces, csp_df_stats = self.validator.validate_shift_tracjectories(self.csp)

        # rearrange the data frames
        sp_df_traces["Group"] = "Original"
        sp_df_traces["Peak"] = [f"Peak #{i}" for i in range(1, len(sp_df_traces)+1)]

        csp_df_traces["Group"] = "Corrected"
        csp_df_traces["Peak"] = [f"Peak #{i}" for i in range(1, len(csp_df_traces)+1)]

        df_traces = pd.concat((sp_df_traces, csp_df_traces), axis=0).melt(
            id_vars=["Group", "Peak"], var_name="Spectrum", value_name="Deviation")
        df_stats = pd.concat((sp_df_stats, csp_df_stats), axis=1, keys=["Original", "Corrected"]).melt()

        # start plotting
        fig, axes = plt.subplots(1, 2, figsize=(10, 6))

        # show the trajectories
        sns.lineplot(ax=axes[0], data=df_traces, x="Spectrum", y="Deviation", hue="Group", 
                     units="Peak", estimator=None, alpha=0.2)
        axes[0].hlines(y=0, xmin=0, xmax=len(self.sp), color='black', linestyle='dotted')
        axes[0].set_xlabel("Indirect dimension [spectrum index]")
        axes[0].set_ylabel("Trajectory deviation [point]")
        axes[0].set_title(f"Trajectories deviation")

        # highlight hovered trajectories
        lines_original = sp_df_traces.to_numpy()[:, :-2].tolist()

        def on_hover(event):
            if event.inaxes != axes[0]:
                return
            
            hover_lines = [line for line in axes[0].lines
                           if line.contains(event)[0]]
            other = [line for line in axes[0].lines
                     if not line.contains(event)[0]]
            
            for line in other:
                line.set_alpha(0.2)

            hovered_idx = []
            for line in hover_lines:
                values = line.get_data()[1].tolist()
                if values in lines_original:
                    idx = lines_original.index(values)
                    hovered_idx.append(idx)
                    line.set_alpha(1.0)
                    axes[0].lines[len(sp_df_traces)+idx].set_alpha(1.0)
            
            if hovered_idx:
                txt = ", ".join([str(i) for i in hovered_idx])
                axes[0].set_title(f"Trajectories deviation ({txt})")
            else:
                axes[0].set_title(f"Trajectories deviation")
            fig.canvas.draw_idle()

        fig.canvas.mpl_connect('motion_notify_event', on_hover)

        # show the stats on trajectories
        sns.stripplot(ax=axes[1], data=df_stats, x="variable_1", y="value", hue="variable_0", 
                      dodge=True, legend=False, alpha=0.2)
        sns.pointplot(ax=axes[1], data=df_stats, x="variable_1", y="value", hue="variable_0", 
                      errorbar='ci', marker='_', linestyles='none', markersize=15, markeredgewidth=3, 
                      alpha=0.7, dodge=0.4) # type: ignore
        axes[1].set_xlabel("")
        axes[1].legend(title="Group")
        axes[1].set_ylabel("Absolute trajectory deviation [point]")
        axes[1].set_title(f"Trajectories deviation statistics")

        fig.suptitle(f"Peak's trajectories deviation for\n\"{self.name}\"")
        fig.tight_layout()
