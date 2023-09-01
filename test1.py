import cv2
import pickle
import numpy as np
import cvzone

with open("shelf",'rb')as f:
            points=pickle.load(f)
            
            
w,h=69,199 
cap=cv2.VideoCapture('sf3.mp4')

def cropt(f):
    scount=0
    for pts in points:
        x,y,=pts
        crop=f[y:y+h,x:x+w]
#        cv2.imshow(str(x*y),crop)
        count=cv2.countNonZero(crop)       
        cv2.putText(frame,str(count),(x,y -1),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),2)
        if count>2:
           cv2.rectangle(frame,pts,(pts[0]+w,pts[1]+h),(0,255,0),2)
            
        else:
            cv2.rectangle(frame,pts,(pts[0]+w,pts[1]+h),(0,0,255),2)
            scount+=1
        cvzone.putTextRect(frame,f'freespace:-{scount}',(50,60),2,2)

#        cv2.rectangle(img,pts,(pts[0]+w,pts[1]+h),(0,0,255),2)
while True:
      ret,frame=cap.read()
      if not ret:
        break
      frame=cv2.resize(frame,(1020,800))
    
      gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      frameBlur=cv2.GaussianBlur(gray,(5,5),1)
      frameThreshold=cv2.adaptiveThreshold(frameBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV,105,9)
      frameMedian=cv2.medianBlur(frameThreshold,5)
      kernel=np.ones((3,3),np.uint8)
      FrameDilate=cv2.dilate(frameMedian,kernel,iterations=1)
    
    
   
      cropt(FrameDilate)
     
      cv2.imshow("FRAME",frame)

      if cv2.waitKey(90) & 0xFF == 27:
         break
cap.release()    
cv2.destroyAllWindows()     
