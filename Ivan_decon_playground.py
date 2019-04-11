from pycudadecon import decon
import matplotlib.pyplot as plt
import numpy as np
import tifffile

filedir = "C:\\Data\\Ivan_decontests\\2019-4-2-U2OS_plin2_DS2_1\\"
kerneldir = "561_PSF_64x64.tif"
datadir = "4-Pos_000_000_561\\"
data = "4-Pos_000_000_561_STACK.tif"
data_crop = "561_STACK_CROP4.tif"

result = decon(data, kernel, n_iter=30)


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
