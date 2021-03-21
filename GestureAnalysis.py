

import numpy as np
import cv2 
import pyautogui, sys #Used to import support for mouse functions

def empty(a):
    pass

#Imports the path to the cascade
path = 'haarcascades/open_Palm.xml'
objname = 'HAND'

#init camara
cap = cv2.VideoCapture(0)

#stores the width and height of frame
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
#stores the centre of the frame
frame_width_centre = round(frame_width/2)
frame_height_centre = round(frame_height/2)
#Stores the x and y in the middle of a 1080 x 1920p monitor
sX = 960
sY = 540

#Loads a new window with sliders to gather info
cv2.namedWindow("Settings")
cv2.resizeWindow("Settings",frame_width,frame_height+100)
cv2.createTrackbar("Scale","Settings",400,1000,empty)
cv2.createTrackbar("Neig","Settings",8,20,empty)
cv2.createTrackbar("Min Area", "Settings",1,100000,empty)
cv2.createTrackbar("Brightness","Settings",100,255,empty)
cv2.createTrackbar("Sensitivity","Settings",20,100,empty)
cv2.createTrackbar("Check","Settings",0,1,empty)
#Loads the cascade
cascade = cv2.CascadeClassifier(path)

while(True):
	#Gets data from settings
	sensitivity = int(cv2.getTrackbarPos("Sensitivity","Settings"))
	brightness = cv2.getTrackbarPos("Brightness","Settings")
	check= cv2.getTrackbarPos("Check","Settings")
	#Updates the frames brightness
	cap.set(10, brightness)
	#Stores the frame from vid
	reg, frame = cap.read()
	#flips the image 
	frame = cv2.flip(frame,1)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#Gets data from settings
	scaleVal = 1 +(cv2.getTrackbarPos("Scale","Settings")/1000)
	neig = cv2.getTrackbarPos("Neig", "Settings")
	# Creates the openPalm cascade
	objs = cascade.detectMultiScale(gray,scaleVal,neig)

	#Goes through the patterns within the cascade
	for(x,y,w,h) in objs:
		#Object detection
		area = w*h
		minArea = cv2.getTrackbarPos("Min Area", "Settings")
		if area > minArea:
	
				# store the values for the centre of the hull
				cX = int(x+(w/2))
				cY = int(y+(h/2))
				cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
				if check == 1:
					# draw circle in centre of the hull
					

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
						sY-= sensitivity
					elif 270 < cX < 370 and 410 > cY > 310:
						print("S")
						sY+= sensitivity
					elif 430 < cX < 530 and 290 > cY > 190:
						print("E")
						sX+= sensitivity
					elif 110 < cX < 210 and 290 > cY > 190:
						print("W")
						sX-= sensitivity
					elif 480 < cX < 530 and 120 > cY > 70:
						print("NE")
						sY-= sensitivity 
						sX+= sensitivity
					elif 480 < cX < 530 and 170 > cY > 120:
						print("NEE")
						sX+= sensitivity
						sY-= sensitivity/2
					elif 430 < cX < 480 and 120 > cY > 70:
						print("NNE")
						sY-= sensitivity
						sX+= sensitivity/2
					elif 110 < cX < 160 and 120 > cY > 70:
						print ("NW")
						sY-= sensitivity 
						sX-= sensitivity
					elif 160 < cX < 210 and 120 > cY > 70:
						print("NNW")
						sY-= sensitivity 
						sX-= sensitivity/2
					elif 110 < cX < 160 and 170 > cY > 120:
						print("NWW")
						sY-= sensitivity/2
						sX-= sensitivity
					elif 480 < cX < 530 and 410 > cY > 360:
						print("SE")
						sY+= sensitivity 
						sX+= sensitivity
					elif 480 < cX < 530 and 360 > cY > 310:
						print("SEE")
						sY+= sensitivity/2 
						sX+= sensitivity
					elif 430 < cX < 480 and 410 > cY > 360:
						print("SSE")
						sY+= sensitivity 
						sX+= sensitivity/2
					elif 110 < cX < 160 and 410 > cY > 360:
						print("SW")
						sY+= sensitivity 
						sX-= sensitivity
					elif 110 < cX < 160 and 360 > cY > 310:
						print("SWW")
						sY+= sensitivity/2
						sX-= sensitivity
					elif 160 < cX < 210 and 410 > cY > 360:
						print("SSW")
						sY+= sensitivity 
						sX-= sensitivity/2




			#Boundary to check if mouse is in boundary
					if 0 < x < 1920 and 0 < y < 1080:
				#moves mouse
						pyautogui.moveTo(sX,sY)


	#Shows the frame
	cv2.imshow("track", frame)

	#Used to end loop
	ch = cv2.waitKey(1)
	if ch & 0xFF == 27:
		break

cap.release()
cv2.destroyAllWindows()
