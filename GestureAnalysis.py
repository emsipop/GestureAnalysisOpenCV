
import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv.VideoWriter('testvideo.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (frame_width, frame_height))

while(True):
	# reads webcam feed and flips horizontally
	ret, frame = cap.read()
	frame = cv.flip(frame, 1)

	out.write(frame)
	frame = cv.resize(frame, (0,0), fx=0.5,fy=0.5)
	
	# sets colour range to help determine hand mask
	hsvim = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	lower = np.array([0, 48, 80], dtype = "uint8")
	upper = np.array([20, 255, 255], dtype = "uint8")
	skinRegionHSV = cv.inRange(hsvim, lower, upper)
	
	# blurs video to help find contours
	blurred = cv.blur(skinRegionHSV, (2,2))
	ret,thresh = cv.threshold(blurred,0,255,cv.THRESH_BINARY)
	
	# finds the contours and saves to array
	contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	contours = max(contours, key=lambda x: cv.contourArea(x))
	
	# draws the data to the screen
	cv.drawContours(frame, [contours], -1, (255,255,0), 2)
	cv.imshow("contours", frame)
	
	hull = cv.convexHull(contours)
	cv.drawContours(frame, [hull], -1, (0, 255, 255), 2)
	cv.imshow("hull", frame)

	ch = cv.waitKey(1)
	if ch & 0xFF == ord('q'):
		break

cap.release()
out.release()

cv.destroyAllWindows()
