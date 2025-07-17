import cv2
import numpy as np
import matplotlib.pyplot as lt
image = cv2.imread('screw.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
