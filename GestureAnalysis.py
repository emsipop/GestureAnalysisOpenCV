import numpy as np # required for cv2 library
import pyautogui, sys, time, cv2  #Used to import support for mouse functions

#==========================================#
def empty(a):
    pass
#==========================================#
def create_squares():
		#Creates rectangles that act as a guide

	cv2.rectangle(frame,(270,70),(370,170),(255,0,0),5)
	cv2.rectangle(frame,(270,410),(370,310),(255,0,0),5)
	cv2.rectangle(frame,(430,290),(530,190),(255,0,0),5)
	cv2.rectangle(frame,(110,290),(210,190),(255,0,0),5)

					#Top right
	cv2.rectangle(frame,(530,170),(480,70),(255,255,0),5)
	cv2.rectangle(frame,(430,70),(530,120),(255,255,0),5)
			
					#Top left 
	cv2.rectangle(frame,(110,70),(160,170),(255,255,0),5)
	cv2.rectangle(frame,(110,70),(210,120),(255,255,0),5)
	
					#Bottom right 
	cv2.rectangle(frame,(530,310),(480,410),(255,255,0),5)
	cv2.rectangle(frame,(430,410),(530,360),(255,255,0),5)

					#Bottom left
	cv2.rectangle(frame,(110,310),(160,410),(255,255,0),5)
	cv2.rectangle(frame,(210,410),(110,360),(255,255,0),5)
	
# ----------------- handles the import of the cascades ----------------- #
# Imports the path to palm cascade
path_palm = 'haarscascades/palm.xml'
palm_object = 'palm'

# Imports the path to the fist Cascade
path_fist = 'haarscascades/fist.xml'
fist_object = 'fist'

# Imports the path to the fist Cascade
path_thumb = 'haarscascades/thumb.xml'
thumb_object = 'thumb'

# Imports the path to the fist Cascade
path_okay = 'haarscascades/okay.xml'
okay_object = 'okay'

# Imports the path to the fist Cascade
path_peace = 'haarscascades/peace.xml'
peace_object = 'peace'
# ---------------------------------------------------------------------- #

# sets initial values for variables used to control click cooldowns, to avoid "spamming" inputs
left_click_time = 0
right_click_time = 0 
double_click_time = 0
# rather than several variables this could be object properties if gestures are changed to objects later
prev_frame = 0
new_frame = 0

# initialises the device's camera
cap = cv2.VideoCapture(0)
# error detection needs to be added here to determine internal/external webcam

# stores the width and height of frame
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
# stores the centre point of the frame
frame_width_centre = round(frame_width/2)
frame_height_centre = round(frame_height/2)
# stores the x and y in the middle of a 1080 x 1920p monitor
sX = 960
sY = 540
# could be swapped out to win32api.GetSystemMetrics() / 2 maybe

# creates a window with sliders to control object detection parameters
cv2.namedWindow("Settings")
cv2.resizeWindow("Settings",frame_width,frame_height+100)

 # options sliders
cv2.createTrackbar("Scale","Settings",400,1000,empty)
cv2.createTrackbar("Neig","Settings",8,20,empty)
cv2.createTrackbar("Min Area", "Settings",1,100000,empty)
cv2.createTrackbar("Brightness","Settings",100,255,empty)
cv2.createTrackbar("Sensitivity","Settings",20,100,empty)
cv2.createTrackbar("Click Cooldown","Settings",5,10,empty)
cv2.createTrackbar("Activate","Settings",0,1,empty)

#==========================================#
scale_value = 400
# creates the cascade classifiers
cascade_palm = cv2.CascadeClassifier(path_palm)
cascade_fist = cv2.CascadeClassifier(path_fist)
cascade_thumb = cv2.CascadeClassifier(path_thumb)
cascade_okay = cv2.CascadeClassifier(path_okay)
cascade_peace = cv2.CascadeClassifier(path_peace)
#==========================================#

# main part of the program - runs the object detections and webcam feed
while(True):
	# Gets data from settings
	sensitivity = int(cv2.getTrackbarPos("Sensitivity","Settings"))
	brightness = cv2.getTrackbarPos("Brightness","Settings")
	check = cv2.getTrackbarPos("Activate","Settings")
	user_cooldown = cv2.getTrackbarPos("Click Cooldown","Settings") # individual cooldowns could be created per gesture if these were objects

	# Updates the frames brightness
	cap.set(10, brightness)

	# Stores the frame from webcam
	reg, frame = cap.read()

	# flips the image 
	frame = cv2.flip(frame,1)
	

	# the opencv trackbar does not allow for a minimum value, so this if statement controls it to avoid a crash
	if cv2.getTrackbarPos("Scale","Settings")/1000 == 0:
		scale_value = 30 # not an optimal value but avoids a crash - if the scale is too low it blitzes the screen with false positives
	else:
		scale_value = 1 +(cv2.getTrackbarPos("Scale","Settings")/1000) # sets the value to what the user has chosen

    # gets neighbours value 
	neig = cv2.getTrackbarPos("Neig", "Settings")

	# Creates the objects for the gestures from the cascades
	objs_palm = cascade_palm.detectMultiScale(frame,scale_value,neig)
	objs_fist = cascade_fist.detectMultiScale(frame,scale_value,neig)
	objs_thumb = cascade_thumb.detectMultiScale(frame,scale_value,neig)
	objs_okay = cascade_okay.detectMultiScale(frame,scale_value,neig)
	objs_peace = cascade_peace.detectMultiScale(frame,scale_value,neig)

#==========================================#

	# Palm Cascade
	for (x,y,w,h) in objs_palm:
		# Object detection
		area = w*h 
		minArea = cv2.getTrackbarPos("Min Area", "Settings") # gets the user set Area

		if area > minArea:
	
			# store the values for the centre of the object 
			cX = int(x+(w/2))
			cY = int(y+(h/2))

			# draws and labels the gesture it has recognised
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 0, 255),3)
			cv2.putText(frame,palm_object,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255, 0, 255),2)
			cv2.circle(frame, (cX, cY), 5, (255, 0, 255), -1) # centre circle
			if check == 1:
				create_squares() # draws the squares for cursor control

				# big ass if statement for each direction the mouse can move - maybe we should clean it up
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

			# if statement to check if mouse is inside the monitor window size
				if 0 < x < 1920 and 0 < y < 1080:
				#moves mouse
					pyautogui.moveTo(sX,sY)
			
#==========================================#
	# Fist Cascade
	for (x,y,w,h) in objs_fist:
		area = w*h
		minArea = cv2.getTrackbarPos("Min Area", "Settings") # user set min area
		if area > minArea:
			# labels the gesture
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 0, 255),3)
			cv2.putText(frame,fist_object,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255, 0, 255),2)
			if check == 1:
				# handles the cooldown to avoid spamming inputs
				left_click_current_time = time.time()
				diff = left_click_current_time - left_click_time # current duration for cooldown 

				if (diff > user_cooldown): 
					print("Left click")
					pyautogui.click(button = "left", clicks = 1)
					left_click_time = left_click_current_time
				else:
					print("Please wait, left click is on a cooldown")

#==========================================#
	# Thumb Cascade
	for (x,y,w,h) in objs_thumb:
		area = w*h
		minArea = cv2.getTrackbarPos("Min Area", "Settings") # user set min area
		if area > minArea:
			# labels the gesture			
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 0, 255),3)
			cv2.putText(frame,thumb_object,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255, 0, 255),2)
			if check == 1:
				# handles the click cooldown
				right_click_current_time = time.time()
				diff = right_click_current_time - right_click_time
				if (diff > user_cooldown): 
					print("Right click")
					pyautogui.click(button = 'right', clicks = 1)
					right_click_time = right_click_current_time
				else:
					print("Please wait, right click is on a cooldown")

#==========================================#
	# Okay Cascade
	#for (x,y,w,h) in objs_okay:
		#area = w*h
		#minArea = cv2.getTrackbarPos("Min Area", "Settings")
		#if area > minArea:
			# labels okay gesture
			#cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 0, 255),3)
			#cv2.putText(frame,okay_object,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255, 0, 255),2)

			# OKAY GESTURE FUNCTION GOES HERE
			#
			#
			#

#==========================================#

	# Peace Cascade
	for(x,y,w,h) in objs_peace:
		area = w*h
		minArea = cv2.getTrackbarPos("Min Area", "Settings")
		if area > minArea:
			# labels the peace gesture
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 0, 255),3)
			cv2.putText(frame,peace_object,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255, 0, 255),2)
			if check == 1:
				# handles the cooldown for the click
				double_click_current_time = time.time()
				diff = double_click_current_time - double_click_time

				if (diff > user_cooldown):
					print("Double click")
					pyautogui.click(button = "left" , clicks = 2)
					double_click_time = double_click_current_time
				else:
					print("Please wait, Double click is on a cooldown")
#==========================================#
	new_frame = time.time()
	fps = 1/(new_frame-prev_frame)
	prev_frame = new_frame
	fps = int(fps)
	fps = str(fps)
	cv2.putText(frame, "FPS = "+fps,(1,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255, 0, 255),2)
#==========================================#
	#Shows the frame
	cv2.imshow("OnlyHands Gesture Control System", frame)

#==========================================#
	#Used to end loop
	ch = cv2.waitKey(1)
	if ch & 0xFF == 27:
		break
#==========================================#
cap.release()
cv2.destroyAllWindows()
#==========================================#
