import numpy as np
import cv2

# capture video input
cap = cv2.VideoCapture('filename') #enter file name of video

# continue to capture until exit key pressed
while(True):

	# store video in a frame
	ret, frame = cap.read()

	# resize and display video frame
	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
	cv2.imshow("Frame", frame)

	# if key 'q' pressed, video input terminates
	ch = cv2.waitKey(50)
	if ch & 0xFF == ord('q'):
		break

# release software and hardware resource
cap.release()

# close all open windows
cv2.destroyAllWindows()
