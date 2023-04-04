'''
NanoCamera: It is a camera interface for the Jetson Nano for working with USB, CSI, IP and also RTSP cameras or streaming video in Python 3.
It is OpenCV ready. The image file can be called directly with OpenCV imshow.
This library requires OpenCV to be installed to work. 

pip3 install nanocamera   

github repo: https://github.com/thehapyone/NanoCamera
'''


import nanocamera as nano

# Create the Camera instance for 640 by 480
camera = nano.Camera()
# Create the Camera instance for No rotation (flip=0) with size of 1280 by 800
#camera = nano.Camera(flip=0, width=1280, height=800, fps=30)

# Working with USB Camera
# For USB Cameras, set the camera_type = 1, and set the device_id as well.
#see connected USB cameras by running:  ls /dev/video*
camera = nano.Camera(camera_type=1, device_id=1, width=640, height=480, fps=30)  



# Working with RTSP streaming camera or streaming video
# For RTSP source, set the camera_type = 2, and set the source as well
# a location for the rtsp stream. Stream location without "rtsp://"
#rtsp_location = "192.168.1.26:8554/stream"

rtsp_location = "admin:hello123@192.168.29.126:554/cam/realmonitor?channel=1&subtype=0"
# Create the Camera instance
camera = nano.Camera(camera_type=2, source=rtsp_location, width=640, height=480, fps=30)


if __name__ == '__main__':
    # Create the Camera instance
    camera = nano.Camera(flip=0, width=640, height=480, fps=30)
    print('CSI Camera ready? - ', camera.isReady())
    while camera.isReady():
        try:
            # read the camera image
            frame = camera.read()
            # display the frame
            cv2.imshow("Video Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        except KeyboardInterrupt:
            break

    # close the camera instance
    camera.release()

    # remove camera object
    del camera