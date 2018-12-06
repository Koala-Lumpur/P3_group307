import numpy as np
import cv2

# Get the capture device
video = cv2.VideoCapture(0)


def main():

    # Capture video
    ret, frame = video.read()

    # Flip video frame by frame
    #frame = cv2.flip(frame, 1)

    frame = np.rot90(frame)

    canny = cv2.Canny(frame, 50, 128)

    canny = cv2.medianBlur(canny, 9)

    return canny
