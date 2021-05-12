import numpy as np # required for cv2 library
import pyautogui, sys, time, cv2  #Used to import support for mouse functions

from tkinter import * #required for tk library
import tkinter.font as tkFont
from tkvideo import tkvideo
from PIL import ImageTk,Image #used for importing images

#==========================================#
# class to set and get the cooldown between clicks
class clickTime:
	def __init__(self):
		self.previous_click = time.time()
	def setPrevious(self,_time):
		self.previous_click = _time
	def getPrevious(self):
		return self.previous_click

# class to control the cursor position
class mousePosition:
	def __init__(self):
		self.s_x = 960
		self.s_y = 540
	def increases_x(self,sens):
		self.s_x += sens
	def decreases_x(self,sens):
		self.s_x -= sens
	def increases_y(self,sens):
		self.s_y += sens
	def decreases_y(self,sens):
		self.s_y -= sens
	def gets_x(self):
		return self.s_x
	def gets_y(self):
		return self.s_y

# function to control the mouse functionality and control cooldowns 
def clickCooldown(click_time, cooldown, button_type, click_num):
	click_current_time = time.time()
	diff = click_current_time - click_time # diff is difference in time since first click
	if (diff > cooldown):
		if (click_num == 2):
			print("Double click")
		else:
			print(button_type + "click")
		pyautogui.click(button = button_type, clicks = click_num)
		return click_current_time

	else:
		if (click_num == 2):
			print("Please wait, double click is on a cooldown")
		else:
			print("Please wait, " + button_type + " click is on a cooldown")
		return click_time

def calcArea(height, width):
	return height * width

def empty(a):
    pass

# ========================================================= GUI METHODS ========================================================= #

# method to close the window - will be called when user clicks exit
def clickExit():
	video.quit()

# method to create the contact us window - called when user clicks contact us on the window label
def createContactUsWindow():
   contact_us_window = Tk()
   contact_us_window.title("Contact Us") # set title
   contact_us_window.config(bg="#F1D93E") # sets background colour
   contact_us_window.geometry("260x75+30+30") # sets resolution size
   contact_us_window.resizable(False,False)
   contact_us_window.iconbitmap('media/bitmaplogo.ico') 

   contact_email_label = Label(contact_us_window, text= "Email: onlyhands.uol@gmail.com",bg="#F1D93E") # contact details
   contact_email_label.grid(row = 0, column = 0) # places email text

   contact_us_close_button = Button(contact_us_window, text= "Close", command = contact_us_window.destroy, cursor= "tcross",bg="#F1D93E", activebackground = "lightgray", activeforeground = "white")
   contact_us_close_button.grid(row = 2, column = 0)

# method to create the help window - called when user clicks help on the window label
def createHelpWindow():
   help_index_window = Tk()
   help_index_window.title("Help Index")
   help_index_window.iconbitmap('media/bitmaplogo.ico')
   help_index_window.config(bg="#F1D93E")
   help_index_window.geometry("600x850+30+30")

   help_title_font = tkFont.Font(family="verdana", size = 30, weight = "bold")
   help_body_font = tkFont.Font(family="verdana", size = 15)
   help_index_window.resizable(False,False)

   help_title_label = Label(help_index_window, font = help_title_font, text= "Help Index:", bg="#F1D93E", width =10, height = 2)
   help_title_label.grid(row = 0, column = 0)

   neighbour_help_label = Label(help_index_window, text= "Neighbours is used in the program to specify how many neighbours each\n candidate needs to retain it,\nThe parameter effects the quantity of gestures recognised ", font = help_body_font, bg="#F1D93E", bd =1, anchor = W, justify = LEFT, width =60, height = 5)
   neighbour_help_label.grid(row = 1, column = 0)

   scale_help_label = Label(help_index_window, text= "Scale is a paramater that specifies how much the image size is reduced,\nif no gestures are being detected reduce this number", font = help_body_font, bg="#F1D93E", anchor = W, justify = LEFT, width =60, height = 5)
   scale_help_label.grid(row = 2, column = 0)

   min_area_help_label = Label(help_index_window, text= "The Min. Area slider acts as a way to reduce false recognition of gestures", font = help_body_font, bg="#F1D93E", bd =1, anchor = W, justify = LEFT, width =60, height = 5)
   min_area_help_label.grid(row = 3, column = 0)

   brightness_help_label = Label(help_index_window, text= "The brightness slider changes the brightness of the frame.", font = help_body_font, bg="#F1D93E", bd =1, anchor = W, justify = LEFT, width =60, height = 5)
   brightness_help_label.grid(row = 4, column = 0)

   sensitivity_help_label = Label(help_index_window, text= "The senstivity slider is to increase or decrease\n how fast the cursour moves", font = help_body_font, bg="#F1D93E", bd =1, anchor = W, justify = LEFT, width =60, height = 5)
   sensitivity_help_label.grid(row = 5, column = 0)

   cooldown_help_label = Label(help_index_window, text= "The Click Cooldown slider is to increase or decrease time\n between clicking the same button", font = help_body_font, bg="#F1D93E", bd =1, anchor = W, justify = LEFT, width =60, height = 5)
   cooldown_help_label.grid(row = 6, column = 0)

   activation_help_label = Label(help_index_window, text= "The activation checkbox when selected allows the\n program to take control of the mouse", font = help_body_font, bg="#F1D93E", bd =1, anchor = W, justify = LEFT, width =60, height = 5)
   activation_help_label.grid(row = 7, column = 0)

   fps_help_label = Label(help_index_window, text= "The FPS checkbox when selected shows the FPS within the frame", font = help_body_font, bg="#F1D93E", bd =1, anchor = W, justify = LEFT, width =60, height = 5)
   fps_help_label.grid(row = 8, column = 0)

   help_close_button = Button(help_index_window, text= "Close", command = help_index_window.destroy, cursor= "tcross", bg="#F1D93E", activebackground = "lightgray", activeforeground = "white", bd =1)
   help_close_button.grid(row = 9, column = 1)

# ========================================================= IMAGE PROCESSING METHOD ========================================================= #

# main part of the program - runs the object detections and webcam feed
def gestureHandling():	

	user_cooldown = user_cooldown_Intvar.get()
	sensitivity = sensitivity_Intvar.get()
	brightness = brightness_Intvar.get()
	min_area = min_area_Intvar.get()
	neig = neighbour_Intvar.get()
	check = check_Intvar.get()
	fps_choice = fps_choice_Intvar.get()

	if scale_value_Intvar.get()/1000 == 0:
		scale_value = 50 # not an optimal value but avoids a crash - if the scale is too low it blitzes the screen with false positives
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
	objs_peace = cascade_peace.detectMultiScale(frame,scale_value,neig)

	#==========================================#

	# Palm Cascade
	for (x,y,w,h) in objs_palm:
		# Object detection
		if calcArea(h,w) > min_area:
	
			# store the values for the centre of the object 
			centre_x = int(x+(w/2))
			centre_y = int(y+(h/2))

			# draws and labels the gesture it has recognised
			cv2.rectangle(frame,(x,y),(x+w,y+h),(colour1),3)
			cv2.putText(frame,palm_object,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(colour1),2)
			cv2.circle(frame, (centre_x, centre_y), 5, (colour2), -1) # centre circle
			if check == 1:
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

				# big ass if statement for each direction the mouse can move - maybe we should clean it up
				if 270 < centre_x < 370 and 170 > centre_y > 70:
						print("N")
						mouse_position.decreases_y(sensitivity)
				elif 270 < centre_x < 370 and 410 > centre_y > 310:
						print("S")
						mouse_position.increases_y(sensitivity)
				elif 430 < centre_x < 530 and 290 > centre_y > 190:
						print("E")
						mouse_position.increases_x(sensitivity)
				elif 110 < centre_x < 210 and 290 > centre_y > 190:
						print("W")
						mouse_position.decreases_x(sensitivity)
				elif 480 < centre_x < 530 and 120 > centre_y > 70:
						print("NE")
						mouse_position.decreases_y(sensitivity)
						mouse_position.increases_x(sensitivity)
				elif 480 < centre_x < 530 and 170 > centre_y > 120:
						print("NEE")
						mouse_position.increases_x(sensitivity)
						mouse_position.decreases_y(sensitivity/2)
				elif 430 < centre_x < 480 and 120 > centre_y > 70:
						print("NNE")
						mouse_position.decreases_y(sensitivity)
						mouse_position.increases_x(sensitivity/2)
				elif 110 < centre_x < 160 and 120 > centre_y > 70:
						print ("NW")
						mouse_position.decreases_y(sensitivity)
						mouse_position.decreases_x(sensitivity)
				elif 160 < centre_x < 210 and 120 > centre_y > 70:
						print("NNW")
						mouse_position.decreases_y(sensitivity)
						mouse_position.decreases_x(sensitivity/2)
				elif 110 < centre_x < 160 and 170 > centre_y > 120:
						print("NWW")
						mouse_position.decreases_y(sensitivity/2)
						mouse_position.decreases_x(sensitivity)
				elif 480 < centre_x < 530 and 410 > centre_y > 360:
						print("SE")
						mouse_position.increases_x(sensitivity)
						mouse_position.increases_y(sensitivity)
				elif 480 < centre_x < 530 and 360 > centre_y > 310:
						print("SEE")
						mouse_position.increases_x(sensitivity/2)
						mouse_position.increases_y(sensitivity)
				elif 430 < centre_x < 480 and 410 > centre_y > 360:
						print("SSE")
						mouse_position.increases_x(sensitivity)
						mouse_position.increases_y(sensitivity/2)
				elif 110 < centre_x < 160 and 410 > centre_y > 360:
						print("SW")
						mouse_position.increases_y(sensitivity)
						mouse_position.decreases_x(sensitivity)
				elif 110 < centre_x < 160 and 360 > centre_y > 310:
						print("SWW")
						mouse_position.increases_y(sensitivity/2)
						mouse_position.decreases_x(sensitivity)
				elif 160 < centre_x < 210 and 410 > centre_y > 360:
						print("SSW")
						mouse_position.decreases_x(sensitivity/2)
						mouse_position.increases_y(sensitivity)

			# if statement to check if mouse is inside the monitor window size
				if 0 < x < 1920 and 0 < y < 1080:
				#moves mouse
					mouse_x = mouse_position.gets_x()
					mouse_y = mouse_position.gets_y()
					pyautogui.moveTo(mouse_x,mouse_y)
			
	#==========================================#
	# Fist Cascade
	for (x,y,w,h) in objs_fist:

		if calcArea(h,w) > min_area:
			# labels the gesture
			cv2.rectangle(frame,(x,y),(x+w,y+h),(colour1),3)
			cv2.putText(frame,fist_object,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(colour1),2)
			if check == 1:
				# handles the cooldown to avoid spamming inputs
				left.setPrevious(clickCooldown(left.getPrevious(),user_cooldown,"Left",1))

	#==========================================#
	# Thumb Cascade
	for (x,y,w,h) in objs_thumb:

		if calcArea(h,w) > min_area:
			# labels the gesture			
			cv2.rectangle(frame,(x,y),(x+w,y+h),(colour1),3)
			cv2.putText(frame,thumb_object,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(colour1),2)
			if check == 1:
				# handles the click cooldown
				right.setPrevious(clickCooldown(right.getPrevious(),user_cooldown,"Right",1))
	#==========================================#

	# Peace Cascade
	for(x,y,w,h) in objs_peace:

		if calcArea(h,w) > min_area:
			# labels the peace gesture
			cv2.rectangle(frame,(x,y),(x+w,y+h),(colour1),3)
			cv2.putText(frame,peace_object,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(colour1),2)
			if check == 1:
				# handles the cooldown for the click
				double.setPrevious(clickCooldown(double.getPrevious(),user_cooldown,"left",2))

	#==========================================#
	# Creates an FPS counter for user feedback
	# only if the user wishes to see the FPS
	if fps_choice == 1:
		new_frame = time.time()
		previous = fps.getPrevious()
		fps_string = str(int(1/(new_frame-previous)))
		fps.setPrevious(new_frame)
		cv2.putText(frame, "FPS: "+ fps_string,(1,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(colour2),2)
	#==========================================#
	#Shows the frame
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
	img = Image.fromarray(frame)
	imgtk = ImageTk.PhotoImage(image=img)
	main_frame.imgtk = imgtk
	main_frame.configure(image=imgtk)
	main_frame.after(10, gestureHandling) 

# ========================================================= GUI INITIALISATION ========================================================= #
# uses tkinter to create the main gui window
video = Tk()  #Makes main window
video.title("OnlyHands Mouse Control System")
video.iconbitmap('media/bitmaplogo.ico') # gets the team's logo
video.config(bg="#F1D93E") # sets the background colour
video.geometry("875x925+30+30") # sets the resolution of the window
video.resizable(False,False) # locks the resolution - avoids scaling issues when resizing

# creates a frame to place onto the window - for the webcam feed and openCV processing
image_frame = Frame(video, width = 600, height = 400)
image_frame.place(x=0,y=0) # places in top left

main_frame = Label(image_frame)
main_frame.place(x=0,y=0)

# Fonts
title_font = tkFont.Font(family="verdana", size=30, weight = "bold")
name_font = tkFont.Font(family="verdana", size=15, weight = "bold", slant = "italic")
slider_font = tkFont.Font(family="verdana", size=10)
quit_font = tkFont.Font(family="verdana", size=35)

# Intvars
user_cooldown_Intvar = IntVar()
sensitivity_Intvar = IntVar()
brightness_Intvar = IntVar()
min_area_Intvar = IntVar()
neighbour_Intvar = IntVar()
scale_value_Intvar = IntVar()
check_Intvar = IntVar()
fps_choice_Intvar = IntVar()

# image
onwindowlogo = Image.open("media/logo.png")
tkLogo = ImageTk.PhotoImage(onwindowlogo)

# Others
logo_label = Label(video, image=tkLogo, bg ="#F1D93E")
logo_label.image = tkLogo
logo_label.place(x=600, y= 20)
sliders_label = Label(video, text="Settings:", font =title_font,bg="#F1D93E").place(x=0,y=400)
quit_button = Button(video, text=" Quit ", command=clickExit, cursor= "tcross",bg="#F1D93E", activebackground = "lightgray", activeforeground = "white", font=quit_font, relief =RIDGE)
quit_button.place(x=625,y=150)

# Scale Slider
scale_label = Label(video, text="Scale:", font =name_font,bg="#F1D93E" ).place(x=25,y=475)
scale_slider = Scale(video, from_=0, to=1000,tickinterval=500, orient=HORIZONTAL,variable = scale_value_Intvar, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = slider_font,  relief = RIDGE, repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
scale_slider.set(400)
scale_slider.place(x=130,y=475)

#Neigbour Slider
neighbour_label = Label(video, text="Neighbours:", font =name_font,bg="#F1D93E").place(x=430,y=475)
neighbour_slider = Scale(video, from_=0, to=20,tickinterval=10,orient=HORIZONTAL,variable = neighbour_Intvar, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = slider_font,  relief = RIDGE, repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
neighbour_slider.set(8)
neighbour_slider.place(x=600,y=475)

#Minarea Slider
min_area_label = Label(video, text="Min. Area:", font =name_font,bg="#F1D93E").place(x=5,y=600)
min_area_slider = Scale(video, from_=0, to=100000,tickinterval=50000, orient=HORIZONTAL, variable = min_area_Intvar, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = slider_font,  relief = RIDGE, repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
min_area_slider.set(1)
min_area_slider.place(x=130,y=600)

#Brightness Slider
brightness_label = Label(video, text="Brightness:", font =name_font,bg="#F1D93E").place(x=430,y=600)
brightness_slider = Scale(video, from_=0, to=255,tickinterval=127, orient=HORIZONTAL, variable = brightness_Intvar, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = slider_font,  relief = RIDGE, repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
brightness_slider.set(100)
brightness_slider.place(x=600,y=600)

#Senstivity Slider
senstivity_label = Label(video, text="Sensitivity:", font =name_font,bg="#F1D93E").place(x=0,y=725)
senstivity_slider = Scale(video, from_=0, to=100,tickinterval=50, orient=HORIZONTAL, variable = sensitivity_Intvar, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = slider_font,  relief = RIDGE, repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
senstivity_slider.set(20)
senstivity_slider.place(x=130,y=725)

#Click Cooldown SLider
cooldown_label = Label(video, text="Click Cooldown:", font =name_font,bg="#F1D93E").place(x=415,y=725)
cooldown_slider = Scale(video, from_=0, to=10,tickinterval=5, orient=HORIZONTAL, variable = user_cooldown_Intvar, sliderlength = 10, length = 250, width = 25, bd = 4, cursor= "tcross", font = slider_font,  relief = RIDGE, repeatdelay = "1", bg ="#F1D93E",fg="white", activebackground ="white", highlightbackground = "white", troughcolor ="lightgray")
cooldown_slider.set(5)
cooldown_slider.place(x=600,y=725)

#Activation Checkbox
activation_checkbox = Checkbutton(video, cursor= "tcross", variable = check_Intvar, onvalue = 1, offvalue = 0, height=3, width = 20, text = "Activation", font =name_font, justify = "center", selectcolor = "lightgray",bg="#F1D93E",activebackground="#F1D93E")
activation_checkbox.place(x=100,y=820)

#Show FPS Checkbox
fps_checkbox = Checkbutton(video, cursor= "tcross", variable = fps_choice_Intvar, onvalue = 1, offvalue = 0, height=3, width = 20, text = "Show FPS", font =name_font, justify = "center", selectcolor = "lightgray",bg="#F1D93E",activebackground="#F1D93E")
fps_checkbox.place(x=580,y=820)

#Help Menubar for settings
menu_bar = Menu(video)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help Index", command=createHelpWindow)
menu_bar.add_cascade(label="Help", menu=help_menu)

#Other Menubar for settings
other_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Other", menu=other_menu)
other_menu.add_command(label="Contact us", command=createContactUsWindow)
other_menu.add_command(label="Quit", command=clickExit)

video.config(menu=menu_bar)

# ========================================================= GESTURE PROCESSING ========================================================= #
pyautogui.FAILSAFE = False # sets the pyautogui library cursor movement failsafe to false, allowing the mouse to be placed at the edge of the screen

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
path_peace = 'haarscascades/peace.xml'
peace_object = 'peace'
# ---------------------------------------------------------------------- #

# sets initial values for variables used to control click cooldowns, to avoid "spamming" inputs
left = clickTime()
right = clickTime()
double = clickTime()

#Used when measuring fps
fps = clickTime()

# creates mouse position object
mouse_position = mousePosition()

# Standardising the colour scheme
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
s_x = 960
s_y = 540

#==========================================#
# creates the cascade classifiers
cascade_palm = cv2.CascadeClassifier(path_palm)
cascade_fist = cv2.CascadeClassifier(path_fist)
cascade_thumb = cv2.CascadeClassifier(path_thumb)
cascade_peace = cv2.CascadeClassifier(path_peace)

#==========================================#
gestureHandling()  #Display 2
video.mainloop()  #Starts GUI
#==========================================#
