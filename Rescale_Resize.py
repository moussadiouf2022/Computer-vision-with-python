import cv2 as cv

#im = cv.imread(r"C:\Users\hp\opencv_tuturial_python\image_3.jpg")
#cv.imshow('Image_1',im)

def ChageRes(width,height):
    # Only for Live videos
    capture.set(3,width)
    capture.set(4,height)
    

def rescaleFrame(frame,scale = 0.75):
    # for Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = ( width ,height)
    
    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)

capture = cv.VideoCapture(r"C:\Users\hp\Opencv_tuturial_python\Vid_1.mp4")

while True :
    isTrue,frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Video_resized', frame_resized)
    
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break 

capture.release()
cv.destroyAllWindows() 
 