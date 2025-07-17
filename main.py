import cv2
import numpy as np
import matplotlib.pyplot as lt
image = cv2.imread('screw.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)

contours, _ = cv2.findContours(edges.copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

largest_contours = max(contours, key = cv2.contourArea)
