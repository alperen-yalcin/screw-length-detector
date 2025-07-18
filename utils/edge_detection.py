import cv2
import numpy as np
import matplotlib.pyplot as plt
def edge_detection():
    image = cv2.imread('assets/screw.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_contour = max(contours, key = cv2.contourArea)

    leftmost = tuple(largest_contour[largest_contour[:, :, 0].argmin()][0])
    rightmost= tuple(largest_contour[largest_contour[:, :, 0].argmax()][0])

    screw_length = np.linalg.norm(np.array(rightmost) - np.array(leftmost))

    output = image.copy()
    cv2.circle(output, leftmost, 5, (0, 255, 0), -1)
    cv2.circle(output, rightmost, 5, (0, 0, 255), -1)
    cv2.line(output, leftmost, rightmost, (255, 0, 0), 2)

    print(f'Length of the screw (pixel): {screw_length:.2f}')
    print(f'Rightmost point coordinate: {rightmost}')

    plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
    plt.title('Measurement On The Screw')
    plt.axis('off')
    plt.show()