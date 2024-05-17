import cv2
import numpy as np
import time
import PoseModule as pm
import os 

cap = cv2.VideoCapture('PoseVideos/Squats.mp4')

detector = pm.poseDetector()

count = 0
dir = 0
pTime = 0


while True:
    success,img = cap.read()
    img = cv2.resize(img,(1280,720))
    img = detector.findPose(img,False)
    lmList = detector.findPosition(img,False)
    
    if len(lmList)!=0:
        angle = detector.findAngle(img,23,25,27)
        b = detector.findAngle(img,24,26,28)
        print(angle," ",b)
        per = np.interp(angle,(90,160),(100,0))
        bar = np.interp(angle,(90,160),(100,650))
        # print(angle,per)
            
        #Checking for dumbbell curls
        color = (255,0,255)
        if per == 100:
            color = (0,255,0)
            if dir == 1:
                count= count+0.5
                dir = 0
        if per == 0:
            color = (255,0,0)
            if dir == 0:
                count+=0.5
                dir = 1
        cv2.rectangle(img,(1100,100),(1175,650),color,3)
        cv2.rectangle(img,(1100,int(bar)),(1175,650),color,-1)  
        cv2.putText(img,f'{int(per)} %',(1100,75),cv2.FONT_HERSHEY_PLAIN,4,color,4) 
        # print(angle,per,count)
   
        #Drawing Curl Count
        cv2.rectangle(img,(0,450),(250,720),(0,255,0),-1)
        cv2.putText(img,str(int(count)),(45,670),cv2.FONT_HERSHEY_PLAIN,15,(255,0,0),25)
    #FPS
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime   
    cv2.putText(img,str(int(fps)),(50,100),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),5) 
    
    cv2.imshow('Image',img)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()