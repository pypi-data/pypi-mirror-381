#!python

import numpy as np
import matplotlib.pyplot as plt
import sys, os

import cellconstructor as CC, cellconstructor.Units


DESCRIPTION = '''
This program plots the results of a SSCHA minimization 
saved with the Utilities.IOInfo class.

It plots both frequencies and the free energy minimization.

Many files can be specified, in this case, they are plotted one after the other,
separated by vertical dashed lines.

Usage:
 
 >>> sscha-plot-data.py  file1  ...

The code looks for data file called file.dat and file.freqs, 
containing, respectively, the minimization data and the auxiliary frequencies.

These files are generated only by python-sscha >= 1.2.

'''


def main():
    print(DESCRIPTION)

    if len(sys.argv) < 2:
        ERROR_MSG = '''
Error, you need to specify at least one file.
Exit failure!
'''
        print(ERROR_MSG)
        raise ValueError(ERROR_MSG)
    
    plt.rcParams["font.family"] = "Liberation Serif"
    LBL_FS = 12
    DPI = 120
    TITLE_FS = 15

    freqs_files = [sys.argv[x] + '.freqs' for x in range(1, len(sys.argv))]
    minim_files = [sys.argv[x] + '.dat' for x in range(1, len(sys.argv))]

    # Check if all the files exist
    plot_frequencies = None
    plot_minim = None
    for f, m in zip(freqs_files, minim_files):
        if os.path.exists(f):
            if plot_frequencies is None:
                plot_frequencies = True
            if not plot_frequencies:
                raise IOError("Error, file {} found, but not others .freqs".format(f))
        else:
            if plot_frequencies:
                raise IOError("Error, file {} not found.".format(f))
            plot_frequencies = False


        if os.path.exists(m):
            if plot_minim is None:
                plot_minim = True
            if not plot_minim:
                raise IOError("Error, file {} found, but not others .freqs".format(m))
        else:
            if plot_minim:
                raise IOError("Error, file {} not found.".format(m))
            plot_minim = False

    if not plot_frequencies and not plot_minim:
        print("Nothing to plot, check if the .dat and .freqs files exist.")
        exit()

    if plot_minim:
        print("Preparing the minimization data...") 
        minim_data = np.concatenate([np.loadtxt(f) for f in minim_files])

        # Insert the x axis in the plotting data
        xsteps = np.arange(minim_data.shape[0])
        new_data = np.zeros(( len(xsteps), 8), dtype = np.double)
        new_data[:,0] = xsteps
        new_data[:, 1:] = minim_data
        minim_data = new_data
        
        fig_data, axarr = plt.subplots(nrows=2, ncols = 2, sharex = True, dpi = DPI)
        
        # Plot the data
        axarr[0,0].fill_between(minim_data[:,0], minim_data[:,1] - minim_data[:, 2]*.5 ,
                                minim_data[:, 1] + minim_data[:, 2] * .5, color = "aquamarine")
        axarr[0,0].plot(minim_data[:,0], minim_data[:,1], color = "k")
        axarr[0,0].set_ylabel("Free energy / unit cell [meV]", fontsize = LBL_FS)


        axarr[0,1].fill_between(minim_data[:,0], minim_data[:,3] - minim_data[:, 4]*.5 ,
                                minim_data[:, 3] + minim_data[:, 4] * .5, color = "aquamarine")
        axarr[0,1].plot(minim_data[:,0], minim_data[:,3], color = "k")
        axarr[0,1].set_ylabel("FC gradient", fontsize = LBL_FS)

        axarr[1,1].fill_between(minim_data[:,0], minim_data[:,5] - minim_data[:, 6]*.5 ,
                                minim_data[:, 5] + minim_data[:, 6] * .5, color = "aquamarine")
        axarr[1,1].plot(minim_data[:,0], minim_data[:,5], color = "k")
        axarr[1,1].set_ylabel("Structure gradient", fontsize = LBL_FS)
        axarr[1,1].set_xlabel("Good minimization steps", fontsize = LBL_FS)


        axarr[1,0].plot(minim_data[:,0], minim_data[:,7], color = "k")
        axarr[1,0].set_ylabel("Effective sample size", fontsize = LBL_FS)
        axarr[1,0].set_xlabel("Good minimization steps", fontsize = LBL_FS)
        fig_data.tight_layout()
    



    if plot_frequencies:
        print("Plotting the frequencies")

        # Load all the data
        freqs_data = np.concatenate([np.loadtxt(f) for f in freqs_files])
        # Now plot the frequencies
        fig_freqs = plt.figure(dpi = DPI)
        ax = plt.gca()

        N_points, Nw = np.shape(freqs_data)

        for i in range(Nw):
            ax.plot(freqs_data[:, i] * CC.Units.RY_TO_CM)

        ax.set_xlabel("Good minimization steps", fontsize = LBL_FS)
        ax.set_ylabel("Frequency [cm-1]", fontsize = LBL_FS)
        ax.set_title("Frequcency evolution", fontsize = TITLE_FS)
        fig_freqs.tight_layout()

    plt.show()
    
if __name__ == "__main__":
    main()