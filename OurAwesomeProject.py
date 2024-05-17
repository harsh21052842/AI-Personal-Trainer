import cv2
import time
import PoseModule as pm

cap = cv2.VideoCapture('PoseVideos/vid2.mp4')
pTime = 0
detector = pm.poseDetector()
while True:
    ret,img = cap.read()
    img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
    img = detector.findPose(img)
    lmlist = detector.findPosition(img,draw=False)
    if len(lmlist)!=0:
        print(lmlist[14])
        cv2.circle(img,(lmlist[14][1],lmlist[14][2]),15,(0,255,0),-1)
        
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3,cv2.LINE_AA)
        
    cv2.imshow("Image",img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()