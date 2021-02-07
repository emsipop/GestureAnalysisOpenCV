import numpy as np
import cv2

# capture video input
cap = cv2.VideoCapture(0)

# retrieve frame resolutions and convert to int
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# write video output
out = cv2.VideoWriter('testvideo.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (frame_width, frame_height))

# continue to capture until exit key pressed
while(True):

	# store video in a frame
	ret, frame = cap.read()

	# write frame to file 'testvideo.mp4'
	out.write(frame)

	# resize and display video frame
	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
	cv2.imshow("Frame", frame)

	# if key 'q' pressed, video input terminates
	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break

# release software and hardware resources
cap.release()
out.release()

# close all open windows
cv2.destroyAllWindows()
