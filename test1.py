import cv2
import pickle
import numpy as np
import cvzone


cap=cv2.VideoCapture('sf3.mp4')


while True:
      ret,frame=cap.read()
      if not ret:
        break
      frame=cv2.resize(frame,(1020,800))
      cv2.imshow("FRAME",frame)

      if cv2.waitKey(90) & 0xFF == 27:
         break
cap.release()    
cv2.destroyAllWindows()     
