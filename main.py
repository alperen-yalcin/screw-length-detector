import cv2
import numpy as np
import matplotlib.pyplot as lt
image = cv2.imread('screw.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)

contours, _ = cv2.findContours(edges.copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

largest_contour = max(contours, key = cv2.contourArea)

leftmost = tuple(largest_contour[largest_contour[:, :, 0].argmin()][0])
rightmost= tuple(largest_contour[largest_contour[:, :, 0].argmax()][0])

screw_length = np.linalg.norm(np.array(rightmost) - np.array(leftmost))

output = image.copy()
cv2.circle(output, leftmost, 5, (0, 255, 0), -1)
cv2.circle(output, rightmost, 5 (0, 0, 255), -1)
cv2.line(output, leftmost, rightmost, (255, 0, 0), 2)