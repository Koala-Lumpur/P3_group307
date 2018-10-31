import numpy as np
import cv2

# Get the capture device
video = cv2.VideoCapture('stock.mp4');

ret, firstframe = video.read()
firstframe = cv2.flip(firstframe, 1)

# Define the mask to be used for background subtraction
sub = cv2.createBackgroundSubtractorMOG2()

while (True):
    # Capture video
    ret, frame = video.read()

    # Flip video frame by frame
    frame = cv2.flip(frame, 1)

    # Apply mask to video capture
    bgmask = sub.apply(frame)

    median = cv2.medianBlur(bgmask,5)

    diff = cv2.absdiff(firstframe, frame)

    # Show the video
    #cv2.imshow('frame', frame)
    cv2.imshow('Background sub', bgmask)
    cv2.imshow('Median', median)
    #cv2.imshow('Difference', diff)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()