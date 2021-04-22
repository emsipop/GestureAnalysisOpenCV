import numpy as np
import cv2 
import pyautogui, sys #Used to import support for mouse functions

#==========================================#
def empty(a):
    pass
#==========================================#

#==========================================#
#Imports the path to palm cascade
path_palm = 'haarscascades/palm.xml'
objName_palm = 'palm'
#==========================================#

#==========================================#
#Imports the path to the fist Cascade
path_fist = 'haarscascades/fist.xml'
objName_fist = 'fist'
#==========================================#

#==========================================#
#Imports the path to the fist Cascade
path_thumb = 'haarscascades/thumb.xml'
objName_thumb = 'thumb'
#==========================================#

#==========================================#
#Imports the path to the fist Cascade
path_okay = 'haarscascades/okay.xml'
objName_okay = 'okay'
#==========================================#

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
#pixels per frame
#Only set sensitivity to even

#Loads a new window with sliders to gather info
cv2.namedWindow("Settings")
cv2.resizeWindow("Settings",frame_width,frame_height+100)
cv2.createTrackbar("Scale","Settings",400,1000,empty)
cv2.createTrackbar("Neig","Settings",8,20,empty)
cv2.createTrackbar("Min Area", "Settings",1,100000,empty)
cv2.createTrackbar("Brightness","Settings",100,255,empty)
cv2.createTrackbar("Sensitivity","Settings",20,100,empty)
cv2.createTrackbar("Check","Settings",0,1,empty)

#==========================================#
cascade_palm = cv2.CascadeClassifier(path_palm)
cascade_fist = cv2.CascadeClassifier(path_fist)
cascade_thumb = cv2.CascadeClassifier(path_thumb)
cascade_okay = cv2.CascadeClassifier(path_okay)
#==========================================#

#==========================================#
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
	objs_palm = cascade_palm.detectMultiScale(gray,scaleVal,neig)
	objs_fist = cascade_fist.detectMultiScale(gray,scaleVal,neig)
	objs_thumb = cascade_thumb.detectMultiScale(gray,scaleVal,neig)
	objs_okay = cascade_okay.detectMultiScale(gray,scaleVal,neig)

#==========================================#
	#Palm Cascade
	for(x,y,w,h) in objs_palm:
		#Object detection
		area = w*h
		minArea = cv2.getTrackbarPos("Min Area", "Settings")
		if area > minArea:
	
			# store the values for the centre of the hull
			cX = int(x+(w/2))
			cY = int(y+(h/2))
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 0, 255),3)
			cv2.putText(frame,objName_palm,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255, 0, 255),2)
			cv2.circle(frame, (cX, cY), 5, (255, 0, 255), -1)
#==========================================#

#==========================================#
	#Fist Cascade
	for(x,y,w,h) in objs_fist:
		area = w*h
		minArea = cv2.getTrackbarPos("Min Area", "Settings")
		if area > minArea:
		# store the values for the centre of the hull
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 0, 255),3)
			cv2.putText(frame,objName_fist,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255, 0, 255),2)
#==========================================#

#==========================================#
	#Thumb Cascade
	for(x,y,w,h) in objs_thumb:
		area = w*h
		minArea = cv2.getTrackbarPos("Min Area", "Settings")
		if area > minArea:
		# store the values for the centre of the hull
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 0, 255),3)
			cv2.putText(frame,objName_thumb,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255, 0, 255),2)
#==========================================#

#==========================================#
	#Okay Cascade
	for(x,y,w,h) in objs_okay:
		area = w*h
		minArea = cv2.getTrackbarPos("Min Area", "Settings")
		if area > minArea:
		# store the values for the centre of the hull
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 0, 255),3)
			cv2.putText(frame,objName_okay,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255, 0, 255),2)
#==========================================#

#==========================================#
	#Shows the frame
	cv2.imshow("track", frame)
#==========================================#


	#Used to end loop
	ch = cv2.waitKey(1)
	if ch & 0xFF == 27:
		break
#==========================================#

#==========================================#
cap.release()
cv2.destroyAllWindows()
#==========================================#
