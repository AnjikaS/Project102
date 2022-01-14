import cv2

def snapshot():
    #initialising cv2, a module that accesses webcam
    videoCaptureObject = cv2.VideoCapture(0) #0=no frames captured
    result = True 
    #if result is 0, then the while() takes place
    while(result):
        #read() saves the picture taken. ret & frame = variables
        ret,frame=videoCaptureObject.read()
        #imwrite() changes name of image(frame var)
        cv2.imwrite("Picture1.jpg",frame)
        result = False
    #WebCam stops working, release() means stop
    videoCaptureObject.release()
    #destroys all tabs to prevent multiple images in loop
    cv2.destroyAllWindows()
snapshot()