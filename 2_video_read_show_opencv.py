import cv2
import numpy as np

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('assets/Dog.mp4')  #To capture a video, you need to create a VideoCapture object

# Check if camera opened successfully
if (cap.isOpened()== False): 
 print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
 # Capture frame-by-frame
 ret, frame = cap.read()    #cap.read() returns a bool (True/False). If the frame is read correctly, it will be True. So you can check for the end of the video by checking this returned value.
 if ret == True:
   # Display the resulting frame
   cv2.imshow('Frame',frame)

   # Press Q on keyboard to  exit
   if cv2.waitKey(25) & 0xFF == ord('q'):
     break

 # Break the loop
 else: 
   break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

