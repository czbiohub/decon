from py4j.java_gateway import JavaGateway
from napari import ViewerApp
from napari.util import app_context
import cv2
import time
import numpy as np
from copy import deepcopy
from skimage import data

def cv2_sobel_edge_with_binary(image):

    k=3
    t=5000
    blur = cv2.GaussianBlur(image, (k,k),0)

    (t, binary) = cv2.threshold(blur,t, 65534, cv2.THRESH_BINARY_INV)

    grad_x = cv2.Sobel(binary, cv2.CV_16U, 2, 0)
    grad_y = cv2.Sobel(binary, cv2.CV_16U, 0, 2)

    edge = cv2.bitwise_or(grad_x, grad_y)
    return edge

gate = JavaGateway()
with app_context():
    viewer = ViewerApp()

    layer1 = viewer.add_image(np.memmap('Q:\Snap-Live-Stream.dat',
                                      dtype=np.uint16, offset=0,
                                      shape=(2048, 2048)))



