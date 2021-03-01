
import numpy as np
import cv2, sys, pyautogui # import mouse & keyboard control

# capture video input
cap = cv2.VideoCapture(0)

while(True):

	# store video frame, flip, resize, and set resolution
	ret, frame = cap.read()
	frame = cv2.flip(frame,1)
	frame = cv2.resize(frame,(1920,1080), fx=0,fy=0, interpolation= cv2.INTER_CUBIC)
	
	# convert frame from RGB to HSV
	hsvim = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# store lowest and highest HSV values
	lower = np.array([21, 79, 0], dtype = np.uint8)
	upper = np.array([70, 135, 242], dtype = np.uint8)
	skinRegionHSV = cv2.inRange(hsvim, lower, upper)

	# blur image & set threshold
	blurred = cv2.GaussianBlur(skinRegionHSV,(5,5),0)
	ret,thresh = cv2.threshold(blurred,240,255,cv2.THRESH_BINARY)
	
	# store image if it's within the HSV range - if no contour is present then skip if statement
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	if(contours != []):

		# draw contours around the selected HSV values
		contours = max(contours, key=lambda x: cv2.contourArea(x))
		cv2.drawContours(frame, [contours], -1, (255,255,0), 2)

		# draw a hull around the contour previosuly created
		hull = cv2.convexHull(contours)
		cv2.drawContours(frame, [hull], -1, (0, 255, 255), 2)

		# store the values for the centre of the hull
		M = cv2.moments(hull)
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])

		# draw circle in centre of the hull
		cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)

		# move cursor to points
		pyautogui.moveTo(cX, cY) 

		# pyautogui.move(oldX - newX, oldY - newY, duration=1)  # move mouse relative to its current position

	# show the frame
	cv2.imshow("Frame", frame)

	# end loop on 'esc'
	ch = cv2.waitKey(1)
	if ch & 0xFF == 27:
		break

# release resources and destroy open windows
cap.release()
cv2.destroyAllWindows()

