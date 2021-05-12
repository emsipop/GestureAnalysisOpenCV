![Logo](/LogoTitle.png "Title")
# OnlyHands Mouse Control System
This tool enables you to perform mouse functions using your webcam and gestures.

The mouse functionality and their respective gestures include:
* Cursor Control - Open Palm
* Left Click - Fist
* Right Click - Thumbs up
* Double Left Click - Peace

The program includes a settings window with several parameters, for the best results reduce the scale value and slightly increase brightness. Decreasing the neighbours slider can improve recognition but also causes more false positives. 
Once you are happy with the hand detection drag the activation slider to 1 and the mouse controls will be unlocked.

A video demonstration can be found [here](https://www.youtube.com/watch?v=qfBEfVnS2Xc).
## Explanation
The program makes use of Haar cascades in OpenCV to recognise the user's hand and PyAutoGUI to handle the mouse functions.

In order to create the cascades, positives and negatives were taken using [this python script](https://github.com/JacobMarshall0/OpenCV-Positive-Negative-Capturer).

These images were then processed using the tools provided by OpenCV referenced [here](https://docs.opencv.org/4.2.0/dc/d88/tutorial_traincascade.html).

## Feedback

If you wish to improve the code or leave a suggestion, please use the [issues tab](https://github.com/emsipop/GestureAnalysisOpenCV/issues) on this repository.

Please use as much detail as possible for bug reports or suggestions.

You can also contact the team at onlyhands.uol@gmail.com


