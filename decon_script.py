from pycudadecon import decon
import matplotlib.pyplot as plt
import numpy as np
import tifffile

dir = "Z:\\ComputationalMicroscopy\\SpinningDisk\\Processed\\Decon_raw"
experiment = "\\2019_04_08_U2OS_plin2_Lipid_MT_Actin_3"
kernel = {'405': "405_PSF_avg.tif",
          '488': "488_PSF_avg.tif",
          '561': "561_PSF_avg.tif",
          '637': "637_PSF_avg.tif"}

outdir = "Z:\\ComputationalMicroscopy\\SpinningDisk\\Processed\\Decon_processed\\testdecon.tif"

# not used
# datadir = "4-Pos_000_000_561\\"
# data = "4-Pos_000_000_561_STACK.tif"
# data_crop = "561_STACK_CROP4.tif"

channels = ['\\Zyla_488_Widefield_tiffstack.tif', '\\Zyla_561_Widefield_tiffstack.tif', '\\Zyla_637_Widefield_tiffstack.tif']

data = dir+experiment+"\\2-Pos_000_000"+channels[0]
psf = dir+"\\"+kernel['488']

result = decon(data, psf, n_iter=30)

tifffile.imsave(outdir, result)
# metadata:
# objective: 63x, 1.47
# camera: andor Zyla (6.5 um pixels)
# pixel size: 103 nm
# wavelength: 561 nm
# z- step = 250 nm

# kernel = tifffile.imread(dir+kernel)
# im = tifffile.imread(dir+datadir+data)
# im_crop = im[:, 896:1152, 896:1152]
#
# tifffile.imsave(dir+datadir+"561_STACK_CROP.tif", im_crop)
#
# im_crop = im[:, 128:384, 972:1228]
# tifffile.imsave(dir+datadir+"561_STACK_CROP.tif", im_crop)

# im_crop = im[:, 1100, 256]
