import numpy as np # required for cv2 library
import cv2
import pyautogui, sys, time, cv2  #Used to import support for mouse functions

from tkinter import * #required for tk library
import tkinter.font as tkFont
from tkvideo import tkvideo
from PIL import ImageTk,Image #used for importing images

#==========================================#
#Window
video = Tk()  #Makes main window
video.title("Only hands")
video.iconbitmap('bitmaplogo.ico')
video.config(bg="#F1D93E")
video.geometry("875x925+30+30")
video.resizable(False,False)

imageFrame = Frame(video, width = 600, height = 400)
imageFrame.place(x=0,y=0)

lmain = Label(imageFrame)
lmain.place(x=0,y=0)

def clickExit():
	video.quit()

def contactusHelp():
   contactus = Tk()
   contactus.title("Contact Us")
   contactus.config(bg="#F1D93E")
   contactus.geometry("160x75+30+30")
   contactus.resizable(False,False)
   contactus.iconbitmap('bitmaplogo.ico') 
   conemailLabel = Label(contactus, text= "Email: help@onlyhands.com",bg="#F1D93E")
   conemailLabel.grid(row = 0, column = 0)
   conenumLabel = Label(contactus, text= "Number: 08081 960082",bg="#F1D93E")
   conenumLabel.grid(row = 1, column = 0)
   contactuscloseButton = Button(contactus, text= "Close", command = contactus.destroy, cursor= "tcross",bg="#F1D93E", activebackground = "lightgray", activeforeground = "white")
   contactuscloseButton.grid(row = 2, column = 0)


def helpindexHelp():
   helpindex = Tk()
   helpindex.title("Help Index")
   helpindex.iconbitmap('bitmaplogo.ico')
   helpindex.config(bg="#F1D93E")
   helpindex.geometry("600x850+30+30")
   helptitleFont = tkFont.Font(family="verdana", size = 30, weight = "bold")
   helpbodyFont = tkFont.Font(family="verdana", size = 15)
   helpindex.resizable(False,False)
   helptitleLable = Label(helpindex, font = helptitleFont, text= "Help Index:", bg="#F1D93E", width =10, height = 2)
   helptitleLable.grid(row = 0, column = 0)
   neighelpLabel = Label(helpindex, text= "Neighbours is used in the program to specify how many neighbours each\n canditate needs to retain it,\n The parameter effects the quanitity of gestures ", font = helpbodyFont, bg="#F1D93E", bd =1, anchor = W, justify = LEFT, width =60, height = 5)
   neighelpLabel.grid(row = 1, column = 0)
   scalehelpLabel = Label(helpindex, text= "Scale is a paramater that specifies how much the image size is reduced,\nif no gestures are being detected reduce this number", font = helpbodyFont, bg="#F1D93E", anchor = W, justify = LEFT, width =60, height = 5)
   scalehelpLabel.grid(row = 2, column = 0)
   minareahelpLabel = Label(helpindex, text= "The Min. Area slider acts as a way to reduce false gestures", font = helpbodyFont, bg="#F1D93E", bd =1, anchor = W, justify = LEFT, width =60, height = 5)
   minareahelpLabel.grid(row = 3, column = 0)
   brightnesshelpLabel = Label(helpindex, text= "The brightness slider changes the brightness of the frame.", font = helpbodyFont, bg="#F1D93E", bd =1, anchor = W, justify = LEFT, width =60, height = 5)
   brightnesshelpLabel.grid(row = 4, column = 0)
   senstivityhelpLabel = Label(helpindex, text= "The senstivity slider is to increase or decrease\n how fast the cursour moves", font = helpbodyFont, bg="#F1D93E", bd =1, anchor = W, justify = LEFT, width =60, height = 5)
   senstivityhelpLabel.grid(row = 5, column = 0)
   clickwnhelpLabel = Label(helpindex, text= "The Click Cooldown slider is to increase or decrease time\n between clicking the same button", font = helpbodyFont, bg="#F1D93E", bd =1, anchor = W, justify = LEFT, width =60, height = 5)
   clickwnhelpLabel.grid(row = 6, column = 0)
   activationhelpLabel = Label(helpindex, text= "The activation checkbox when selected allows the\n program to take control of the mouse", font = helpbodyFont, bg="#F1D93E", bd =1, anchor = W, justify = LEFT, width =60, height = 5)
   activationhelpLabel.grid(row = 7, column = 0)
   showfpshelpLabel = Label(helpindex, text= "The FPS checkbox when selected shows the FPS within the frame", font = helpbodyFont, bg="#F1D93E", bd =1, anchor = W, justify = LEFT, width =60, height = 5)
   showfpshelpLabel.grid(row = 8, column = 0)
   helpindexcloseButton = Button(helpindex, text= "Close", command = helpindex.destroy, cursor= "tcross", bg="#F1D93E", activebackground = "lightgray", activeforeground = "white", bd =1)
   helpindexcloseButton.grid(row = 9, column = 1)

# def reportissueHelp():
#    reportissue = Tk()
#    reportissue.iconbitmap('bitmaplogo.ico') # Need to add actual bitmap
#    reporttitleLablel = Label(reportissue, text= "Report Issue:", font = titleFont)
#    reporttitleLablel.grid(row = 0, column = 0)
#    issueEntry = Entry(reportissue, bd=5, cursor = "tcross")
#    issueEntry.grid(row = 0, column = 1)
#    issueconfirmButton = Button(reportissue, text= "Enter",cursor= "tcross")
#    issueconfirmButton.grid(row = 0, column = 2)
#    reportissuecloseButton = Button(reportissue, text= "Close", command = reportissue.destroy, cursor= "tcross")
#    reportissuecloseButton.grid(row = 9, column = 9)
#    #entrysucLable = Label(reportissue, text= "Entry Successful", font = sliderFont).grid(row = 2, column = 0)


#Fonts
titleFont = tkFont.Font(family="verdana", size=30, weight = "bold")
nameFont = tkFont.Font(family="verdana", size=15, weight = "bold", slant = "italic")
sliderFont = tkFont.Font(family="verdana", size=10)
quitFont = tkFont.Font(family="verdana", size=35)

#Intvars
user_cooldown_Intvar = IntVar()
sensitivity_Intvar = IntVar()
brightness_Intvar = IntVar()
minArea_Intvar = IntVar()
neig_Intvar = IntVar()
scale_value_Intvar = IntVar()
check_Intvar = IntVar()
fps_choice_Intvar = IntVar()

#image
onwindowlogo = Image.open("logo.png")
tkLogo = ImageTk.PhotoImage(onwindowlogo)

#Others
logoLabel = Label(video, image=tkLogo, bg ="#F1D93E")
logoLabel.image = tkLogo
logoLabel.place(x=600, y= 20)
slidersLabel = Label(video, text="Sliders:", font =titleFont,bg="#F1D93E").place(x=0,y=400)
quitButton = Button(video, text=" Quit ", command=clickExit, cursor= "tcross",bg="#F1D93E", activebackground = "lightgray", activeforeground = "white", font=quitFont, relief =RIDGE)
quitButton.place(x=625,y=150)



#Scale Slider
scaleLabel = Label(video, text="Scale:", font =nameFont,bg="#F1D93E" ).place(x=25,y=475)
scaleSlider = Scale(video, from_=0, to=1000,tickinterval=500, orient=HORIZONTAL,variable = scale_value_Intvar, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = sliderFont,  relief = RIDGE, repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
scaleSlider.set(400)
scaleSlider.place(x=130,y=475)

#Neigbour Slider
neigLabel = Label(video, text="Neighbours:", font =nameFont,bg="#F1D93E").place(x=430,y=475)
neigSlider = Scale(video, from_=0, to=20,tickinterval=10,orient=HORIZONTAL,variable = neig_Intvar, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = sliderFont,  relief = RIDGE, repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
neigSlider.set(8)
neigSlider.place(x=600,y=475)

#Minarea Slider
minareaLabel = Label(video, text="Min. Area:", font =nameFont,bg="#F1D93E").place(x=5,y=600)
minareaSlider = Scale(video, from_=0, to=100000,tickinterval=50000, orient=HORIZONTAL, variable = minArea_Intvar, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = sliderFont,  relief = RIDGE, repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
minareaSlider.set(1)
minareaSlider.place(x=130,y=600)

#Brightness Slider
brightnesLabel = Label(video, text="Brightness:", font =nameFont,bg="#F1D93E").place(x=430,y=600)
brightnessSlider = Scale(video, from_=0, to=255,tickinterval=127, orient=HORIZONTAL, variable = brightness_Intvar, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = sliderFont,  relief = RIDGE, repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
brightnessSlider.set(100)
brightnessSlider.place(x=600,y=600)

#Senstivity Slider
senstivityLabel = Label(video, text="Sensitivity:", font =nameFont,bg="#F1D93E").place(x=0,y=725)
senstivitySlider = Scale(video, from_=0, to=100,tickinterval=50, orient=HORIZONTAL, variable = sensitivity_Intvar, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = sliderFont,  relief = RIDGE, repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
senstivitySlider.set(20)
senstivitySlider.place(x=130,y=725)

#Click Cooldown SLider
clickwnLabel = Label(video, text="Click Cooldown:", font =nameFont,bg="#F1D93E").place(x=415,y=725)
clickwnSlider = Scale(video, from_=0, to=10,tickinterval=5, orient=HORIZONTAL, variable = user_cooldown_Intvar, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = sliderFont,  relief = RIDGE, repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
clickwnSlider.set(5)
clickwnSlider.place(x=600,y=725)

#Activation Checkbox
activationCheck = Checkbutton(video, cursor= "tcross", variable = check_Intvar, onvalue = 1, offvalue = 0, height=3, width = 20, text = "Activation", font =nameFont, justify = "center", selectcolor = "lightgray",bg="#F1D93E",activebackground="#F1D93E")
activationCheck.place(x=100,y=820)


#Show FPS Checkbox
showfpsCheck = Checkbutton(video, cursor= "tcross", variable = fps_choice_Intvar, onvalue = 1, offvalue = 0, height=3, width = 20, text = "Show FPS", font =nameFont, justify = "center", selectcolor = "lightgray",bg="#F1D93E",activebackground="#F1D93E")
showfpsCheck.place(x=580,y=820)


#Help Menubar for settings
menuBar = Menu(video)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="Help Index", command=helpindexHelp)
#helpMenu.add_command(label="Report Issue", command=reportissueHelp)
menuBar.add_cascade(label="Help", menu=helpMenu)

#Other Menubar for settings
otherMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Other", menu=otherMenu)
otherMenu.add_command(label="Contact us", command=contactusHelp)
otherMenu.add_command(label="Quit", command=clickExit)

video.config(menu=menuBar)

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


#==========================================#
# initialises variable for error checking later
#scale_value = 400
# creates the cascade classifiers
cascade_palm = cv2.CascadeClassifier(path_palm)
cascade_fist = cv2.CascadeClassifier(path_fist)
cascade_thumb = cv2.CascadeClassifier(path_thumb)
cascade_okay = cv2.CascadeClassifier(path_okay)
cascade_peace = cv2.CascadeClassifier(path_peace)
#==========================================#

# main part of the program - runs the object detections and webcam feed
def show_frame():	

	user_cooldown = user_cooldown_Intvar.get()
	sensitivity = sensitivity_Intvar.get()
	brightness = brightness_Intvar.get()
	minArea = minArea_Intvar.get()
	neig = neig_Intvar.get()
	check = check_Intvar.get()
	fps_choice = fps_choice_Intvar.get()
	if scale_value_Intvar.get()/1000 == 0:
		scale_value = 30 # not an optimal value but avoids a crash - if the scale is too low it blitzes the screen with false positives
	else:
		scale_value = 1 +scale_value_Intvar.get()/1000 # sets the value to what the user has chosen
	# Updates the frames brightness
	cap.set(10, brightness)
	# Stores the frame from webcam
	reg, frame = cap.read()
	# flips the image 
	frame = cv2.flip(frame,1)

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
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
	img = Image.fromarray(frame)
	imgtk = ImageTk.PhotoImage(image=img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, show_frame) 

#==========================================#

#==========================================#
#sliderFrame = Frame(video, width=600, height=100)
#sliderFrame.grid(row = 9, column=1, padx=10, pady=2)

show_frame()  #Display 2
video.mainloop()  #Starts GUI
#==========================================#
