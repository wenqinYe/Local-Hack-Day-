#our code

import cv2
from time import sleep 

def overlayImageAtPoint(x,y,w,h,frame):
    s_img = cv2.imread("C:\Users\Pujan\Documents\GitHub\Local-Hack-Day-\eating cat.jpg",-1)
    l_img = frame
    s_img =cv2.resize(s_img,(w,h))
    x_offset=x
    y_offset=y
    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
    
cascPath = "C:\Users\Pujan\Documents\GitHub\Local-Hack-Day-\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
print faceCascade
#video_capture = cv2.VideoCapture(1)
capture = cv2.VideoCapture(1)
capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 600)
capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 600)
while True:
   # sleep(0.25)
    # Capture frame-by-frame
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        overlayImageAtPoint(x,y,w,h,frame)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
        
# When everything is done, release the capture
capture.release()
cv2.destroyAllWindows()
