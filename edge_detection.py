import numpy as np
import cv2

# Get the capture device
video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


def main():

    # Capture video
    ret, frame = video.read()

    frame = frame[0:700, 50:1200]

    # Flip video frame by frame
    #frame = cv2.flip(frame, 1)

    frame = np.rot90(frame)

    canny = cv2.Canny(frame, 50, 128)

    #canny = cv2.medianBlur(canny, 1)

    return canny
