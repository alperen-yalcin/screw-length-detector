import cv2
import math
def distance_measure():
    img = cv2.imread('assets/screw.png')

    points = []
    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            points.append((x, y))
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow('image', img)
            if len(points) == 2:
                x1, y1 = points[0]
                x2, y2 = points[1]
                distance = math.dist(points[0], points[1])
                print(f'Distance: {distance}')
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
