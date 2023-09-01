import cv2
import pickle

  
cap=cv2.VideoCapture('sf3.mp4')

try:
    with open("shelf",'rb')as f:
            points=pickle.load(f)
except:
      points=[]
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        point = [x, y]
        print(point)
#points=[]        
def drawing(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
       points.append((x,y))
       with open("shelf",'wb')as f:
            pickle.dump(points,f)
    if event==cv2.EVENT_RBUTTONDOWN:
       for i,pts in enumerate(points):
           x1,y1=pts
           print(i)
           if x1<x+w and y1<y+h:
              points.pop(i)
    
        
frame_counter = 0  
w,h=69,199
429,182,498,381
#cv2.namedWindow('RGB')
#cv2.setMouseCallback('RGB', RGB)
while True:
    ret,frame=cap.read()
    if not ret:
        break
    frame=cv2.resize(frame,(1020,800))
#    for pts in points:
#        cv2.rectangle(frame,pts,(pts[0]+w,pts[1]+h),(0,0,255),2)
    cv2.rectangle(frame,(429,182),(498,381),(0,0,255),2)
    cv2.imshow("FRAME",frame)
    cv2.setMouseCallback("FRAME",drawing)
    if cv2.waitKey(0) & 0xFF == 27:
        break
cap.release()    
cv2.destroyAllWindows()     
