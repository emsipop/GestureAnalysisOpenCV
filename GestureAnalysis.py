
import numpy as np, cv2, sys, pyautogui


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
		hull = cv2.convexHull(contours, returnPoints= False)
		hullPoints = cv2.convexHull(contours)
		cv2.drawContours(frame, [hullPoints], -1, (0, 255, 255), 2)

		# gets the defects within the hull
		defects = cv2.convexityDefects(contours, hull)

		if defects is not None:
			raisedFingers = 0

		for i in range(defects.shape[0]):

			# get 3 points to form triangle between fingers
			s, e, f, _ = defects[i][0]
			start = tuple(contours[s][0])
			end = tuple(contours[e][0])
			far = tuple(contours[f][0])

			# get length of sides for cosine rule
			a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
			b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
			c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)

			# cosine rule to get angle between fingers
			theta = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))

			# if the angle is less than 90 degrees (1.571 rad) it is a finger
			if theta <= np.pi / 2: 
				raisedFingers += 1
				cv2.circle(frame, far, 5, [0, 0, 255], -1)

			if raisedFingers > 0:
				raisedFingers += 1
			print(raisedFingers)
			cv2.putText(frame, str(raisedFingers), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

		# code for handling gestures
#		pyautogui.mouseUp()
#		if raisedFingers == 5: 
#			pyautogui.click(button = "left")
#		
#		elif raisedFingers == 4:
#			pyautogui.click(button = "right")
#		
#		elif raisedFingers == 2:
#			pyautogui.mouseDown() # should drag across screen ?? not sure, lazy implementation
			

		# store the values for the centre of the hull
		M = cv2.moments(hullPoints)
		if M['m00'] != 0: # prevents program from crashing due to divide-by-zero error
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

