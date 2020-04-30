# Motion-Detector-using-python

Face detection and video capture is done using opencv in python. Later on, both the codes are combined to create file that detects faces while capturing the video i.e in real time.

for running the file in windows system,pyhton interpreter is needed alongwith opencv, which can be done using command prompt and using the 'pip install' command to installing both of the applications.

In the motion detector code,firstly the static frame is captured, saved and later on, each and every frame is compared with that static frame(stored earlier) and the difference is calculated and displayed in a separate frame.
Another frame is generated that displays the objects only when the content in the frame is above the threshold value specified.
Another frame is the converted version of the threshold frame by adding contours to it.

In total there are 4 frames in it,
Gray frame
Delta frame
Threshold frame
Original frame



# Motion-detector using time graph

Firstly the time is noted and saved in a dataframe that contains the start and end time of an object when it is entering and exiting.
That dataframe object is passed to the file and 'bokeh' library of python is used to create a quad graph based on the values in the dataframe.
