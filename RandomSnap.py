import cv2
import random
import time
import dropbox

start_time=time.time()

def snap():
    number=random.randint(1,100)
    #initialising cv2, a module that accesses webcam
    videoCaptureObject = cv2.VideoCapture(0) #0=no frames captured
    result = True 
    #if result is 0, then the while() takes place
    while(result):
        ret,frame=videoCaptureObject.read()
        image_name="img"+str(number)+".png"
        cv2.imwrite(image_name, frame) 

        start_time = time.time()
        result = False 
    return image_name 
    print("Snapshot taken!")
    videoCaptureObject.release() 
    cv2.destroyAllWindows()

def upload_file(img_name): 
    access_token = "FXDSEoswMmQAAAAAAAAAAbQZc-UIRyfb_xijLoTIHgkE5SVdakja9A6JqxCk8_dE" 
    file =img_name 
    file_from = file 
    file_to="/testStory/"+(img_name) 
    dbx = dropbox.Dropbox(access_token) 
    with open(file_from, 'rb') as f: 
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite) 
        print("file uploaded") 
        
def main(): 
        while(True): 
            if ((time.time() - start_time) >= 15): 
                name = snap() 
                upload_file(name) 
main()