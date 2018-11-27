import numpy as np
import cv2

video = cv2.VideoCapture(0);
_, back_frame = video.read()
back_frame = np.rot90(back_frame)

def main():

    '''
    for i in range(framecount):
        _, back_frame[i] = video.read()
        ref_image = cv2.add(ref_image, back_frame[i])
        print(i)
    
    
    ref_image = ref_image / framecount
    ref_image = cv2.flip(ref_image, 1)
    '''

    # Capture video
    ret, frame = video.read()

    # Flip video frame by frame
    frame = np.rot90(frame)

    mask = cv2.subtract(back_frame, frame)

    ret, thresh1 = cv2.threshold(mask, 25, 255, cv2.THRESH_BINARY)
    thresh1 = cv2.cvtColor(thresh1, cv2.COLOR_BGR2GRAY)

    return thresh1

'''
while True:
    cv2.imshow('meh', main())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
'''

'''
# Show the video
cv2.imshow('frame', frame)
cv2.imshow('first frame', back_frame)
cv2.imshow('ref_image', ref_image)
cv2.imshow('mask', mask)
cv2.imshow('threshold', thresh1)
'''