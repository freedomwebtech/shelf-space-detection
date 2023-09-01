import cv2
import pickle

  
cap=cv2.VideoCapture('sf3.mp4')


def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        point = [x, y]
        print(point)
       
def drawing(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
       points.append((x,y))
       with open("shelf",'wb')as f:
            pickle.dump(points,f)
    if event==cv2.EVENT_RBUTTONDOWN:
       for i,pts in enumerate(points):
           x1,y1=pts
           print(i)
          
    
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)
while True:
    ret,frame=cap.read()
    if not ret:
        break
    frame=cv2.resize(frame,(1020,800))

    cv2.rectangle(frame,(429,182),(498,381),(0,0,255),2)
    cv2.imshow("RGB",frame)
#    cv2.setMouseCallback("FRAME",drawing)
    if cv2.waitKey(0) & 0xFF == 27:
        break
cap.release()    
cv2.destroyAllWindows()     
