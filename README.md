# decon
some scripts for GPU-accelerated deconvolution of microscopy data using pycudadecon library

---

attempts to run gpu-accelerated deconvolution (Richardson-lucy) using two libraries:
 - Flowdec (https://github.com/hammerlab/flowdec)
 - pycudadecon (https://github.com/tlambert03/pycudadecon)

---

experimental PSF
 - run code in "extract_psf".  read the header
 
---

deconvolution
 - I found that only pycudadecon produced tunable results
 - convert data into .tif stack files using "convert_to_tiffstack" first
 - modify "decon_data" to reflect your file paths
 - run "decon_data" from command line
