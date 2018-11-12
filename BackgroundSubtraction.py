import numpy as np
import cv2

# Get the capture device
video = cv2.VideoCapture(0);

framecount = 50

ret, frame = video.read()
ref_image = frame
w = frame.shape[0]
h = frame.shape[1]
d = frame.shape[2]
back_frame = np.empty((framecount, w, h, d), dtype=frame.dtype)


for i in range(framecount):
    _, back_frame[i] = video.read()
    ref_image = cv2.add(ref_image, back_frame[i])
    print(i)

ref_image = ref_image / framecount
ref_image = cv2.flip(ref_image, 1)
back_frame[0] = cv2.flip(back_frame[0], 1)

while True:
    # Capture video
    ret, frame = video.read()

    # Flip video frame by frame
    frame = cv2.flip(frame, 1)

    mask = cv2.subtract(back_frame[0], frame)

    median = cv2.medianBlur(mask, 5)

    ret, thresh1 = cv2.threshold(mask, 25, 255, cv2.THRESH_BINARY)
    thresh1 = cv2.cvtColor(thresh1, cv2.COLOR_BGR2GRAY)

    # Show the video
    cv2.imshow('frame', frame)
    cv2.imshow('first frame', back_frame[0])
    cv2.imshow('ref_image', ref_image)
    cv2.imshow('mask', mask)
    cv2.imshow('threshold', thresh1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()