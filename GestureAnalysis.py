
import numpy as np
import cv2 
import pyautogui, sys #Used to import support for mouse functions

#init camara
cap = cv2.VideoCapture(0)

#stores the width and height of frame
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
#stores the centre of the frame
frame_width_centre = round(frame_width/2)
frame_height_centre = round(frame_height/2)
#Stores the x and y in the middle of a 1080 x 1920p monitor
x = 960
y = 540
#pixels per frame
#Only set sensitivity to even
sensitivity = 6

while(True):
	#Stores the frame from vid
	ret, frame = cap.read()
	#flips the image 
	frame = cv2.flip(frame,1)

	# convert frame from RGB to HSV
	hsvim = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# store lowest and highest HSV values
	lower = np.array([20, 90, 160], dtype = np.uint8)
	upper = np.array([45, 255, 255], dtype = np.uint8)
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
		if M['m00'] != 0: # prevents program from crashing due to divide-by-zero error
			cX = int(M["m10"] / M["m00"])
			cY = int(M["m01"] / M["m00"])

			# draw circle in centre of the hull
			cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)

			#Creates rectangles that act as a guide
			cv2.rectangle(frame,(270,70),(370,170),(255,255,0),5)
			cv2.rectangle(frame,(270,410),(370,310),(255,255,0),5)
			cv2.rectangle(frame,(430,290),(530,190),(255,255,0),5)
			cv2.rectangle(frame,(110,290),(210,190),(255,255,0),5)

			#Top right
			cv2.rectangle(frame,(530,70),(480,120),(255,255,0),5)
			cv2.rectangle(frame,(530,170),(480,120),(255,255,0),5)
			cv2.rectangle(frame,(430,70),(480,120),(255,255,0),5)
			
			#Top left 
			cv2.rectangle(frame,(110,70),(160,120),(255,255,0),5)
			cv2.rectangle(frame,(210,70),(160,120),(255,255,0),5)
			cv2.rectangle(frame,(110,170),(160,120),(255,255,0),5)

			#Bottom right 
			cv2.rectangle(frame,(530,410),(480,360),(255,255,0),5)
			cv2.rectangle(frame,(530,310),(480,360),(255,255,0),5)
			cv2.rectangle(frame,(430,410),(480,360),(255,255,0),5)

			#Bottom left
			cv2.rectangle(frame,(110,410),(160,360),(255,255,0),5)
			cv2.rectangle(frame,(110,310),(160,360),(255,255,0),5)
			cv2.rectangle(frame,(210,410),(160,360),(255,255,0),5)

			#Checks if the hand point is in the rectangle guides set out
			#And changes x and y postions accordingly
			if 270 < cX < 370 and 170 > cY > 70:
				print("N")
				y-= sensitivity
			elif 270 < cX < 370 and 410 > cY > 310:
				print("S")
				y+= sensitivity
			elif 430 < cX < 530 and 290 > cY > 190:
				print("E")
				x+= sensitivity
			elif 110 < cX < 210 and 290 > cY > 190:
				print("W")
				x-= sensitivity
			elif 480 < cX < 530 and 120 > cY > 70:
				print("NE")
				y-= sensitivity 
				x+= sensitivity
			elif 480 < cX < 530 and 170 > cY > 120:
				print("NEE")
				x+= sensitivity
				y-= sensitivity/2
			elif 430 < cX < 480 and 120 > cY > 70:
				print("NNE")
				y-= sensitivity
				x+= sensitivity/2
			elif 110 < cX < 160 and 120 > cY > 70:
				print ("NW")
				y-= sensitivity 
				x-= sensitivity
			elif 160 < cX < 210 and 120 > cY > 70:
				print("NNW")
				y-= sensitivity 
				x-= sensitivity/2
			elif 110 < cX < 160 and 170 > cY > 120:
				print("NWW")
				y-= sensitivity/2
				x-= sensitivity
			elif 480 < cX < 530 and 410 > cY > 360:
				print("SE")
				y+= sensitivity 
				x+= sensitivity
			elif 480 < cX < 530 and 360 > cY > 310:
				print("SEE")
				y+= sensitivity/2 
				x+= sensitivity
			elif 430 < cX < 480 and 410 > cY > 360:
				print("SSE")
				y+= sensitivity 
				x+= sensitivity/2
			elif 110 < cX < 160 and 410 > cY > 360:
				print("SW")
				y+= sensitivity 
				x-= sensitivity
			elif 110 < cX < 160 and 360 > cY > 310:
				print("SWW")
				y+= sensitivity/2
				x-= sensitivity
			elif 160 < cX < 210 and 410 > cY > 360:
				print("SSW")
				y+= sensitivity 
				x-= sensitivity/2




			#Boundary to check if mouse is in boundary
			if 0 < x < 1920 and 0 < y < 1080:
				#moves mouse
				pyautogui.moveTo(x,y)


	#Shows the frame
	cv2.imshow("track", frame)

	#Used to end loop
	ch = cv2.waitKey(1)
	if ch & 0xFF == 27:
		break

cap.release()
cv2.destroyAllWindows()
