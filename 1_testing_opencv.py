import cv2
print(cv2.__version__)

img=cv2.imread('assets/a.jpeg')
cv2.imshow("Output",img)
cv2.waitKey(0)  # allows users to display a window for given milliseconds. 0 means infinity. 2000 means 2 seconds
