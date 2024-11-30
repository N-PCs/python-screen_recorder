#importing required packages

import pyautogui
import cv2
import numpy as np

#Specifying Resolution
res=(1920,1080)

#Specifying video codec
codec=cv2.VideoWriter_fourcc(*'XVID')

#Specifying name of output file
filename="recording.avi"

#Specifying frame rates
fps=10  #your choice

#Creating a VideoWriter object
out=cv2.VideoWriter(filename,codec,fps,res)

#Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

#Resize the window
cv2.resizeWindow("Live",480,270)


while True:
	#taking screenshot using pyautogui
	img=pyautogui.screenshot()

	#convert screenshot to numpy array
	frame=np.array(img)

	#convert it from BGR(Bue ,Green ,Red) to RGB(Red ,Green ,Blue)
	frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

	#write it to output file
	out.write(frame)

	#optional :Display the recording screen
	cv2.imshow('Live', frame)

	#stop the recording
	if cv2.waitKey(1)==ord('q'):
		break

#release the video editor
out.release()

#destroy all the windows
cv2.destroyAllWindows()