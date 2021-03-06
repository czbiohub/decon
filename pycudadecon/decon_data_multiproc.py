"""
READ THIS FIRST

Code must be run from command line
After modifying paths below, type:
"python decon_data.py" to execute

This is a multiprocessing version of "decon_data"
# https://stackoverflow.com/questions/20887555/dead-simple-example-of-using-multiprocessing-queue-pool-and-locking
    using default pool = 3 processes, we can measure a speedup of almost 3x
    (this is GPU accelerated not CPU, so multiproc shouldn't scale 1:1 with # processes)

"""
from pycudadecon import decon
import tifffile
import os
import numpy as np

import multiprocessing
num_pools = 3

dir = "Z:\\ComputationalMicroscopy\\SpinningDisk\\Processed\\Decon_raw"
experiment = "\\2019_04_08_U2OS_plin2_Lipid_MT_Actin_3"
# experiment = "\\2019_04_08_U2OS_plin2_Lipid_MT_Actin_Slide2_2"
outdir = "Z:\\ComputationalMicroscopy\\SpinningDisk\\Processed\\Decon_processed\\SIM_PSF"+experiment
if not os.path.exists(outdir):
    os.mkdir(outdir)

kernels = {'405': "405_64x64_SIM.tif",
          '488': "488_64x64_SIM.tif",
          '561': "561_64x64_SIM.tif",
          '637': "637_64x64_SIM.tif"}

channels = {'488': '\\Zyla_488_Widefield_tiffstack.tif',
            '561': '\\Zyla_561_Widefield_tiffstack.tif',
            '637': '\\Zyla_637_Widefield_tiffstack.tif'}

positions = ['\\'+name for name in os.listdir(dir+experiment)
              if os.path.isdir(os.path.join(dir+experiment, name))]
positions_set = {'\\'+name for name in os.listdir(dir+experiment)
              if os.path.isdir(os.path.join(dir+experiment, name))}

wavelengths = {'405': 430,
               '488': 515,
               '561': 585,
               '637': 655}


def proc_channel(pos):
    for chan in channels:
        data = dir+experiment+pos+channels[chan]
        psf = dir+"\\"+kernels[chan]

        if not os.path.isfile(data):
            print("bad file path: "+data)
        if not os.path.isfile(psf):
            print('bad file path: '+psf)

        result = decon(data, psf, cleanup_otf=True, wavelength=wavelengths[chan], na=1.47, nimm=1.515)

        # to output full zstack
        # tifffile.imsave(outdir+pos+"\\testthing%s.tif" % chan, result.astype(dtype=np.uint16))

        # to output individual z-planes in the format generated by micromanager
        for zIdx in range(0, len(result)):
            out_filename = '\\img_000000000_Zyla_%s_Widefield_%03d.tif' % (chan, zIdx)
            tifffile.imsave(outdir+pos+out_filename, result[zIdx].astype(dtype=np.uint16))


def mp_worker(pos):
    print('========== processing position %s ==========' % pos)
    if not os.path.exists(outdir + pos):
        os.mkdir(outdir + pos)
    proc_channel(pos)
    print("========== Process \tDONE ==========")


# subset positions if you want to try on only a few
def mp_handler():
    p = multiprocessing.Pool(num_pools)
    p.map(mp_worker, positions[:])


if __name__ == '__main__':
    mp_handler()
