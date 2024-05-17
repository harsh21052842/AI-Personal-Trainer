import cv2
import mediapipe as mp
import time
import math

class poseDetector():
    # All these arguments are for the Pose() function which instantiates a Pose model instance
    def __init__(self,mode = False,model_complexity=1, upBody = False,smooth = True,detectionCon=0.5,trackCon=0.5):
        self.mode = mode
        self.comp = model_complexity
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        #used to visualize our landmark points
        self.mpDraw = mp.solutions.drawing_utils
        #used to get hold of Pose Estimation model in MediaPipe
        self.mpPose = mp.solutions.pose
        #Pose() function instantiates a Pose model instance/object
        self.pose = self.mpPose.Pose(self.mode, self.comp,self.upBody, self.smooth,self.detectionCon, self.trackCon)
    # converting BGR to RGB ,drwaing landmarks and connecting them (using mediapipe)    
    def findPose(self,img,draw=True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # pose.process() is used to perform pose Estimation on the input frame, results consist of pose landmark points (each landmarks pt. has 4 values[x,y,z,visibility])
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                # visualizing the landmarks using drawing_utils from mediapipe
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS) 
        # returning the image with connected landmark points
        return img  
    
    # converting all landmarks pts (given in some ratio ) to actual co-ordinates and storing them in lmlist , and redrawing these landmarks using new co-ords and coloring them differently   
    def findPosition(self,img,draw=True):
        # storing all the 33 landmark points in lmlist
        self.lmlist=[]
        if self.results.pose_landmarks:
            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c= img.shape
                # converting x,y ratios to actual values by multiplying it with ht. and wt. of image
                cx,cy = int(lm.x*w),int(lm.y*h)
                
                # adding the exact co-ords to lmlist 
                self.lmlist.append([id,cx,cy])
                if draw:
                    # redrawing the landmarks with different color
                    cv2.circle(img,(cx,cy),5,(255,0,0),-1)
        # returning the list containg all the landmark points for this image
        return self.lmlist
    
    def findAngle(self,img,p1,p2,p3,draw = True):
        #Getting the 3 points
        x1,y1 = self.lmlist[p1][1:]
        x2,y2 = self.lmlist[p2][1:]
        x3,y3 = self.lmlist[p3][1:]
        
        #Calculating the angle
        angle = math.degrees(math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2))
        if angle<0:
            angle = angle+360
        if angle>180:
            angle = 360-angle
        # print (angle)
        #Drawing
        if draw:
            cv2.line(img,(x1,y1),(x2,y2),(255,255,255),3)
            cv2.line(img,(x2,y2),(x3,y3),(255,255,255),3)
            cv2.circle(img,(x1,y1),15,(255,0,0),2)
            cv2.circle(img,(x1,y1),10,(255,0,0),-1)
            cv2.circle(img,(x2,y2),15,(255,0,0),2)
            cv2.circle(img,(x2,y2),10,(255,0,0),-1)
            cv2.circle(img,(x3,y3),15,(255,0,0),2)
            cv2.circle(img,(x3,y3),10,(255,0,0),-1)
            cv2.putText(img,str(int(angle)),(x2-70,y2+50),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
            
        return angle
 
def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = poseDetector()
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

if __name__=="__main__":
    main()  