
import numpy as np
import cv2 as cv
import pyautogui, sys


cap = cv.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

while(True):

	ret, frame = cap.read()
	#frame = cv.resize(frame, (0,0), fx=1,fy=1)
	frame = cv.flip(frame,1)
	
	hsvim = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	cv.imshow("hsv", hsvim)
	lower = np.array([21, 90, 0], dtype = np.uint8)
	upper = np.array([40, 255, 255], dtype = np.uint8)
	skinRegionHSV = cv.inRange(hsvim, lower, upper)

	blurred = cv.blur(skinRegionHSV, (2,2))
	ret,thresh = cv.threshold(blurred,0,255,cv.THRESH_BINARY)

	contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	if(contours != []):
		contours = max(contours, key=lambda x: cv.contourArea(x))
		cv.drawContours(frame, [contours], -1, (255,255,0), 2)
		cv.imshow("contours", frame)
		hull = cv.convexHull(contours)
		cv.drawContours(frame, [hull], -1, (0, 255, 255), 2)

		M = cv.moments(hull)
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])

		cv.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
	
		pyautogui.moveTo(cX, cY) 
	
	cv.imshow("track", frame)


	ch = cv.waitKey(1)
	if ch & 0xFF == ord('q'):
		break

cap.release()

cv.destroyAllWindows()

