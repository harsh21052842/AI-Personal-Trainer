import cv2
import numpy as np
import time
import PoseModule as pm

print("Which exercise do you want to perform?")
print("1.Bicep Curls")
print("2.Push Ups")
print("3.Squats")
print("Enter your choice : ")
choice = int(input())

file = -1
print("How do you want to perform the exercise?")
print("1.Upload a video of the exercise.")
print("2.Perform the exercise in real time")
print("Enter : ")
ex = int(input())
print(ex)
if ex == 1:
    print("Make sure that the video file is in the PoseVideos folder!!")
    print("Enter name of the file : ")
    file = "PoseVideos/"+str(input())+".mp4"
else:
    file = 0
print(file)
cap = cv2.VideoCapture(file)
detector = pm.poseDetector()

count = 0.5
dir = -1
if choice == 1:
    dir = 0
else:
    dir = 1
pTime = 0

while True:
    success,img = cap.read()
    img = cv2.resize(img,(1280,720))
    # img = cv2.imread(cap)
    # img = cv2.resize(img,(0,0),fx=0.3,fy=0.3)
    img = detector.findPose(img,False)
    lmList = detector.findPosition(img,False)
    
    if len(lmList)!=0:
        if choice == 1:
            angle = detector.findAngle(img,11,13,15)
            angle2 = detector.findAngle(img,12,14,16)
            per = np.interp(angle,(30,150),(100,0))
            bar = np.interp(angle,(30,150),(100,650))
            # print(angle,per)
            
            #Checking for dumbbell curls
            color = (255,0,255)
            if per == 100:
                color = (0,255,0)
                if dir == 0:
                    count= count+0.5
                    dir = 1
            if per == 0:
                color = (255,0,0)
                if dir == 1:
                    count+=0.5
                    dir = 0
            cv2.rectangle(img,(1100,100),(1175,650),color,3)
            cv2.rectangle(img,(1100,int(bar)),(1175,650),color,-1)  
            cv2.putText(img,f'{int(per)} %',(1100,75),cv2.FONT_HERSHEY_PLAIN,4,color,4) 
            # print(angle,per,count)
        
            #Drawing Curl Count
            cv2.rectangle(img,(0,450),(250,720),(0,255,0),-1)
            cv2.putText(img,str(int(count)),(45,670),cv2.FONT_HERSHEY_PLAIN,15,(255,0,0),25)
                 
        elif choice == 2:
            angle = detector.findAngle(img,11,13,15)
            angle2 = detector.findAngle(img,12,14,16)
            per = np.interp(angle,(80,160),(100,0))
            bar = np.interp(angle,(80,160),(100,650))
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
        elif choice ==3:
            angle = detector.findAngle(img,23,25,27)
            angle2 = detector.findAngle(img,24,26,28)
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
