
import numpy as np
import cv2 as cv
import pyautogui, sys #Used to import support for mouse functions


cap = cv.VideoCapture(0)

#frame_width = int(cap.get(3))
#frame_height = int(cap.get(4))

while(True):
	#Stores the frame from vid
	ret, frame = cap.read()
	#flips the image 
	frame = cv.flip(frame,1)
	#Sets screen to full res
	frame = cv.resize(frame,(1920,1080), fx=0,fy=0, interpolation= cv.INTER_CUBIC)
	
	
	#Converts image from RGB to HSV
	hsvim = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	#Stores the lowest and highest HSV values
	lower = np.array([21, 79, 0], dtype = np.uint8)
	upper = np.array([70, 135, 242], dtype = np.uint8)
	skinRegionHSV = cv.inRange(hsvim, lower, upper)

	#blurs the image and thresholding
	blurred = cv.GaussianBlur(skinRegionHSV,(5,5),0)
	ret,thresh = cv.threshold(blurred,240,255,cv.THRESH_BINARY)
	
	#Stores the image if image is within the HSV range if no contour is present the if statement is skipped
	contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	if(contours != []):

		#Draws the contours around the selected HSV values
		contours = max(contours, key=lambda x: cv.contourArea(x))
		cv.drawContours(frame, [contours], -1, (255,255,0), 2)

		#Draws a hull around the contour previosuly created
		hull = cv.convexHull(contours)
		cv.drawContours(frame, [hull], -1, (0, 255, 255), 2)
		#Stores the values for the centre of the Hull
		M = cv.moments(hull)
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])

		#Draws the circle in the middle
		cv.circle(frame, (cX, cY), 5, (255, 255, 255), -1)

		#Used to control mouse functions
		pyautogui.moveTo(cX, cY) 

	#Shows the frame
	cv.imshow("track", frame)

	#Used to end loop
	ch = cv.waitKey(1)
	if ch & 0xFF == ord('q'):
		break

cap.release()
cv.destroyAllWindows()

