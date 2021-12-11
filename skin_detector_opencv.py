#importing packages
from cv2 import cv2
import numpy as np
import argparse

# define the upper and lower boundaries of the HSV pixel
# intensities to be considered 'skin'
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")


##Frame Maker Function##
# def frame_maker(self.test_video):
test_video = 0
camera = cv2.VideoCapture(test_video)
while True:
    success, frame = camera.read()
    #
    frame = cv2.resize(frame, (400,400))
    converted = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    skinMask = cv2.inRange(converted, lower, upper)

    # apply a series of erosions and dilations to the mask
    # using an elliptical kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    skinMask = cv2.erode(skinMask, kernel, iterations=2)
    skinMask = cv2.dilate(skinMask, kernel, iterations=2)

    # blur the mask to help remove noise, then apply the
    # mask to the frame
    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
    skin = cv2.bitwise_and(frame, frame, mask=skinMask)

    # show the skin in the image along with the mask
    cv2.imshow("images", np.hstack([frame, skin]))

    if cv2.waitKey(1) &0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()

