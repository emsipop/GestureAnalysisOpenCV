![Logo](/Logo.png "Title")
# OnlyHands Mouse Control System
This tool enables you to perform mouse functions using your webcam and gestures.

The mouse functionality and their respective gestures include:
* Cursor Control - Open Palm
* Left Click - Fist
* Right Click - Thumbs up
* Double Left Click - Peace

## Explanation
The program makes use of Haar cascades in OpenCV to recognise the user's hand and PyAutoGUI to handle the mouse functions.

In order to create the cascades, positives and negatives were taken using [this python script](https://github.com/JacobMarshall0/OpenCV-Positive-Negative-Capturer).

These images were then processed using the tools provided by OpenCV referenced [here](https://docs.opencv.org/4.2.0/dc/d88/tutorial_traincascade.html).




