import numpy as np
import cv2

# capture video input
cap = cv2.VideoCapture(0)

# create old frame - convert colour to grey
ret, frame = cap.read()
old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# set Lucas Kanade parameters
parameters = dict(winSize = (15, 15), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# mouse function
def select_point(event, x, y, flags, parameters):

	# declare global variables to store point changes
	global point, point_selected, old_points

	# points set to where mouse is clicked
	if event == cv2.EVENT_LBUTTONDOWN:
		point = (x, y)
		point_selected = True
		old_points = np.array([[x, y]], dtype=np.float32)

# create placeholder - call mouse event 'select_point'
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", select_point)

# reset points for next frame
point_selected = False
point = ()
old_points = np.array([[]])

# continue to capture until exit key pressed
while(True):

	# store video in a frame
	ret, frame = cap.read()

	# convert frame from colour to grey
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# if point is selected
	if point_selected is True:
		
		# create mouse pointer
		cv2.circle(frame, point, 5, (0, 255, 0), 3)

		# assign optical flow 
		new_points, status, error = cv2.calcOpticalFlowPyrLK(old_gray, gray_frame, old_points, None, **parameters)

		# create copy of frame - update points in frame
		old_gray = gray_frame.copy()
		old_points = new_points
		
		# extracts points
		x, y = new_points.ravel()

		# create circle tracker
		cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
	
	# display frame
	cv2.imshow("Frame", frame)

	# if key 'q' pressed, video input terminates
	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break

# release software and hardware resource
cap.release()

# close all open windows
cv2.destroyAllWindows()

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv.VideoWriter('testvideo.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (frame_width, frame_height))

while(True):

	ret, frame = cap.read()

	out.write(frame)
	frame = cv.resize(frame, (0,0), fx=0.5,fy=0.5)
	hsvim = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	lower = np.array([0, 48, 80], dtype = "uint8")
	upper = np.array([20, 255, 255], dtype = "uint8")
	skinRegionHSV = cv.inRange(hsvim, lower, upper)
	blurred = cv.blur(skinRegionHSV, (2,2))
	ret,thresh = cv.threshold(blurred,0,255,cv.THRESH_BINARY)
	contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	contours = max(contours, key=lambda x: cv.contourArea(x))
	cv.drawContours(frame, [contours], -1, (255,255,0), 2)
	cv.imshow("contours", frame)
	hull = cv.convexHull(contours)
	cv.drawContours(frame, [hull], -1, (0, 255, 255), 2)
	cv.imshow("hull", frame)

	ch = cv.waitKey(1)
	if ch & 0xFF == ord('q'):
		break

cap.release()
out.release()

cv.destroyAllWindows()
