import numpy as np # required for cv2 library
import cv2
import pyautogui, sys, time, cv2  #Used to import support for mouse functions

from tkinter import * #required for tk library
import tkinter.font as tkFont
from tkvideo import tkvideo
from PIL import ImageTk,Image #used for importing images

#==========================================#

settings = Tk()
settings.title('Settings')
settings.iconbitmap('logobitmap.ico')
settings.geometry("450x750+30+30")
menuBar = Menu(settings)

def clickExit():
    settings.quit()

def contactusHelp():
    contactus = Tk()
    contactus.iconbitmap('logobitmap.ico') 
    conemailLabel = Label(contactus, text= "Email: example@email.com")
    conemailLabel.grid(row = 0, column = 0)
    conenumLabel = Label(contactus, text= "Number: 0111111")
    conenumLabel.grid(row = 1, column = 0)
    contactuscloseButton = Button(contactus, text= "Close", command = contactus.destroy, cursor= "tcross")
    contactuscloseButton.grid(row = 2, column = 0)


def helpindexHelp():
    helpindex = Tk()
    helpindex.iconbitmap('logobitmap.ico')
    helptitleLable = Label(helpindex, text= "Help Index:", font = titleFont)
    helptitleLable.grid(row = 0, column = 0)
    scalehelpLabel = Label(helpindex, text= "The scale slider does....", font = sliderFont)
    scalehelpLabel.grid(row = 1, column = 0)
    neighelpLabel = Label(helpindex, text= "The Neighbours slider does....", font = sliderFont)
    neighelpLabel.grid(row = 2, column = 0)
    minareahelpLabel = Label(helpindex, text= "The Min. Area slider does....", font = sliderFont)
    minareahelpLabel.grid(row = 3, column = 0)
    brightnesshelpLabel = Label(helpindex, text= "The brightness slider does....", font = sliderFont)
    brightnesshelpLabel.grid(row = 4, column = 0)
    senstivityhelpLabel = Label(helpindex, text= "The senstivity slider does....", font = sliderFont)
    senstivityhelpLabel.grid(row = 5, column = 0)
    clickwnhelpLabel = Label(helpindex, text= "The Click Cooldown slider does.....", font = sliderFont)
    clickwnhelpLabel.grid(row = 6, column = 0)
    activationhelpLabel = Label(helpindex, text= "The activation checkbox does.....", font = sliderFont)
    activationhelpLabel.grid(row = 7, column = 0)
    helpindexcloseButton = Button(helpindex, text= "Close", command = helpindex.destroy, cursor= "tcross")
    helpindexcloseButton.grid(row = 8, column = 1)


def reportissueHelp():
    reportissue = Tk()
    reportissue.iconbitmap('logobitmap.ico') # Need to add actual bitmap
    reporttitleLablel = Label(reportissue, text= "Report Issue:", font = titleFont)
    reporttitleLablel.grid(row = 0, column = 0)
    issueEntry = Entry(reportissue, bd=5, cursor = "tcross")
    issueEntry.grid(row = 0, column = 1)
    issueconfirmButton = Button(reportissue, text= "Enter",cursor= "tcross")
    issueconfirmButton.grid(row = 0, column = 2)
    reportissuecloseButton = Button(reportissue, text= "Close", command = reportissue.destroy, cursor= "tcross")
    reportissuecloseButton.grid(row = 9, column = 9)
    #entrysucLable = Label(reportissue, text= "Entry Successful", font = sliderFont).grid(row = 2, column = 0)


#Fonts
titleFont = tkFont.Font(family="comicsans", size=30)
nameFont = tkFont.Font(family="comicsans", size=15)
sliderFont = tkFont.Font(family="comicsans", size=10)

#Slider Ints
user_cooldown = IntVar()
sensitivity = IntVar()
brightness = IntVar()
minArea = IntVar()
neig = IntVar()
scale_value = IntVar()

#Checkbox Ints
check = IntVar()
fps_choice = IntVar()

#Others
slidersLabel = Label(settings, text="Sliders:", font =titleFont).grid(row=0, column=0)
exitButton = Button(settings, text="Quit", command=clickExit, cursor= "tcross").grid(row=11, column=2)
startButton = Button(settings, text="Start", command=clickExit, cursor= "tcross").grid(row=11, column=0)



#Scale Slider
scaleLabel = Label(settings, text="Scale:", font =nameFont, ).grid(row=1, column =0)
scaleSlider = Scale(settings, from_=0, to=1000,tickinterval=500, orient=HORIZONTAL,variable = scale_value, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = sliderFont,  relief = "flat", repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
scaleSlider.set(400)
scaleSlider.grid(row=1, column=1)

#Neigbour Slider
neigLabel = Label(settings, text="Neighbours:", font =nameFont).grid(row=2, column=0)
neigSlider = Scale(settings, from_=0, to=20,tickinterval=10,orient=HORIZONTAL,variable = neig, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = sliderFont,  relief = "flat", repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
neigSlider.set(8)
neigSlider.grid(row=2, column=1)

#Minarea Slider
minareaLabel = Label(settings, text="Min. Area:", font =nameFont).grid(row=3, column=0)
minareaSlider = Scale(settings, from_=0, to=100000,tickinterval=50000, orient=HORIZONTAL, variable = minArea, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = sliderFont,  relief = "flat", repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
minareaSlider.set(1)
minareaSlider.grid(row=3, column=1)

#Brightness Slider
brightnesLabel = Label(settings, text="Brightness:", font =nameFont).grid(row=4, column=0)
brightnessSlider = Scale(settings, from_=0, to=255,tickinterval=127, orient=HORIZONTAL, variable = brightness, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = sliderFont,  relief = "flat", repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
brightnessSlider.set(100)
brightnessSlider.grid(row=4, column=1)

#Senstivity Slider
senstivityLabel = Label(settings, text="Sensitivity:", font =nameFont).grid(row=5, column=0)
senstivitySlider = Scale(settings, from_=0, to=100,tickinterval=50, orient=HORIZONTAL, variable = sensitivity, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = sliderFont,  relief = "flat", repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
senstivitySlider.set(20)
senstivitySlider.grid(row=5, column=1)

#Click Cooldown SLider
clickwnLabel = Label(settings, text="Click Cooldown:", font =nameFont).grid(row=6, column=0)
clickwnSlider = Scale(settings, from_=0, to=10,tickinterval=5, orient=HORIZONTAL, variable = user_cooldown, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = sliderFont,  relief = "flat", repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
clickwnSlider.set(5)
clickwnSlider.grid(row=6, column=1)

#Activation Checkbox
activationCheck = Checkbutton(settings, cursor= "tcross", variable = check, onvalue = 1, offvalue = 0, height=3, width = 20, text = "Activation", font =nameFont, justify = "center", selectcolor = "lightgray",  relief = "flat")
activationCheck.grid(row = 7, column = 1)


#Show FPS Checkbox
showfpsCheck = Checkbutton(settings, cursor= "tcross", variable = fps_choice, onvalue = 1, offvalue = 0, height=3, width = 20, text = "Show FPS", font =nameFont, justify = "center", selectcolor = "lightgray",  relief = "flat")
showfpsCheck.grid(row = 8, column = 1)

#Help Menubar
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="Help Index", command=helpindexHelp)
helpMenu.add_command(label="Report Issue", command=reportissueHelp)
menuBar.add_cascade(label="Help", menu=helpMenu)


#Other Menubar
otherMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Other", menu=otherMenu)
otherMenu.add_command(label="Contact us", command=contactusHelp)
otherMenu.add_command(label="Quit", command=clickExit)


settings.config(menu=menuBar)
mainloop()

#==========================================#
def empty(a):
    pass
#==========================================#
def create_squares():
		#Creates rectangles that act as a guide

	cv2.rectangle(frame,(270,70),(370,170),(255,255,0),5)
	cv2.rectangle(frame,(270,410),(370,310),(255,255,0),5)
	cv2.rectangle(frame,(430,290),(530,190),(255,255,0),5)
	cv2.rectangle(frame,(110,290),(210,190),(255,255,0),5)

					#Top right
	cv2.rectangle(frame,(530,170),(480,70),(255,255,0),5)
	cv2.rectangle(frame,(430,70),(530,120),(255,255,0),5)
			
					#Top left 
	cv2.rectangle(frame,(110,70),(160,170),(colour2),5)
	cv2.rectangle(frame,(110,70),(210,120),(colour2),5)
	
					#Bottom right 
	cv2.rectangle(frame,(530,310),(480,410),(colour2),5)
	cv2.rectangle(frame,(430,410),(530,360),(colour2),5)

					#Bottom left
	cv2.rectangle(frame,(110,310),(160,410),(colour2),5)
	cv2.rectangle(frame,(210,410),(110,360),(colour2),5)
	
pyautogui.FAILSAFE = False
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

#Used when measuring fps
prev_frame = 0
new_frame = 0

#Standardising the colour scheme
colour1 = (255,0,255)
colour2 = (255,255,0)
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

## creates a window with sliders to control object detection parameters
# cv2.namedWindow("Settings")
# cv2.resizeWindow("Settings",frame_width,frame_height+100)

##  options sliders
# cv2.createTrackbar("Scale","Settings",400,1000,empty)
# cv2.createTrackbar("Neig","Settings",8,20,empty)
# cv2.createTrackbar("Min Area", "Settings",1,100000,empty)
# cv2.createTrackbar("Brightness","Settings",100,255,empty)
# cv2.createTrackbar("Sensitivity","Settings",20,100,empty)
# cv2.createTrackbar("Click Cooldown","Settings",5,10,empty)
# cv2.createTrackbar("Activate","Settings",0,1,empty) 
# cv2.createTrackbar("Show FPS","Settings",0,1,empty) 


#==========================================#
# initialises variable for error checking later
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
	#sensitivity = int(cv2.getTrackbarPos("Sensitivity","Settings"))
	#brightness = cv2.getTrackbarPos("Brightness","Settings")
	#check = cv2.getTrackbarPos("Check","Settings")
	#fps_choice = cv2.getTrackbarPos("Activate", "Settings")
	#user_cooldown = cv2.getTrackbarPos("Click Cooldwon", "Settings")
	# Updates the frames brightness
	cap.set(10, brightness)
	# Stores the frame from webcam
	reg, frame = cap.read()
	# flips the image 
	frame = cv2.flip(frame,1)
	

	# #the opencv trackbar does not allow for a minimum value, so this if statement controls it to avoid a crash
	# if cv2.getTrackbarPos("Scale","Settings")/1000 == 0:
	# 	scale_value = 30 # not an optimal value but avoids a crash - if the scale is too low it blitzes the screen with false positives
	# else:
	# 	scale_value = 1 +(cv2.getTrackbarPos("Scale","Settings")/1000) # sets the value to what the user has chosen

    ## gets neighbours value 
	#neig = cv2.getTrackbarPos("Neig", "Settings")

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
		#minArea = cv2.getTrackbarPos("Min Area", "Settings") # gets the user set Area

		if area > minArea:
	
			# store the values for the centre of the object 
			cX = int(x+(w/2))
			cY = int(y+(h/2))

			# draws and labels the gesture it has recognised
			cv2.rectangle(frame,(x,y),(x+w,y+h),(colour1),3)
			cv2.putText(frame,palm_object,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(colour1),2)
			cv2.circle(frame, (cX, cY), 5, (colour2), -1) # centre circle
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
		#minArea = cv2.getTrackbarPos("Min Area", "Settings") # user set min area
		if area > minArea:
			# labels the gesture
			cv2.rectangle(frame,(x,y),(x+w,y+h),(colour1),3)
			cv2.putText(frame,fist_object,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(colour1),2)
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
		#minArea = cv2.getTrackbarPos("Min Area", "Settings") # user set min area
		if area > minArea:
			# labels the gesture			
			cv2.rectangle(frame,(x,y),(x+w,y+h),(colour1),3)
			cv2.putText(frame,thumb_object,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(colour1),2)
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
		#minArea = cv2.getTrackbarPos("Min Area", "Settings")
		if area > minArea:
			# labels the peace gesture
			cv2.rectangle(frame,(x,y),(x+w,y+h),(colour1),3)
			cv2.putText(frame,peace_object,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(colour1),2)
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
	# Creates an FPS counter for user feedback
	# only if the user wishes to see the FPS
	if fps_choice == 1:
		new_frame = time.time()
		fps = str(int(1/(new_frame-prev_frame)))
		prev_frame = new_frame
		cv2.putText(frame, "FPS: "+ fps,(1,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(colour2),2)
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
