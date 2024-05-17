import streamlit as st
import cv2
import requests
from streamlit_lottie import st_lottie
import numpy as np
import time
import PoseModule as pm


def bcurls(name):
    cap = cv2.VideoCapture(name)
    detector = pm.poseDetector()
    
    count = 0.5
    dir = 0
    pTime = 0

    while True:
        success,img = cap.read()
        if success == False:
            st.write("Video ended!")
            break
        img = cv2.resize(img,(1280,720))
        # img = cv2.imread(cap)
        # img = cv2.resize(img,(0,0),fx=0.3,fy=0.3)
        img = detector.findPose(img,False)
        lmList = detector.findPosition(img,False)
        
        if len(lmList)!=0:
                angle = detector.findAngle(img,11,13,15)
                angle2 = detector.findAngle(img,12,14,16)
                per = np.interp(angle,(60,150),(100,0))
                bar = np.interp(angle,(60,150),(100,650))
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
                cv2.putText(img,"TIP :- ",(55,200),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5)
                cv2.putText(img,"Avoid swinging.",(50,250),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
                cv2.putText(img,"Control the movement.",(50,300),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
                cv2.putText(img,"Isolate the biceps.",(50,350),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
                
                cv2.putText(img,f'{int(per)} %',(1100,75),cv2.FONT_HERSHEY_PLAIN,4,color,4) 
                # print(angle,per,count)
            
                #Drawing Curl Count
                cv2.rectangle(img,(0,450),(400,720),(0,255,0),-1)
                if count<10:
                    cv2.putText(img,'0'+str(int(count)),(45,670),cv2.FONT_HERSHEY_PLAIN,15,(255,0,0),25)
                else:
                    cv2.putText(img,str(int(count)),(45,670),cv2.FONT_HERSHEY_PLAIN,15,(255,0,0),25)
                
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime   
        cv2.putText(img,str(int(fps)),(50,100),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),5) 
        cv2.imshow('Image',img)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    
def squats(name):
    
    cap = cv2.VideoCapture(name)
    detector = pm.poseDetector()

    count = 0
    dir = 0
    pTime = 0


    while True:
        success,img = cap.read()
        if success == False:
            st.write("Video ended!")
            break
        img = cv2.resize(img,(1280,720))
        img = detector.findPose(img,False)
        lmList = detector.findPosition(img,False)
        
        if len(lmList)!=0:
            angle = detector.findAngle(img,23,25,27)
            b = detector.findAngle(img,24,26,28)
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
            cv2.putText(img,"TIP :- ",(55,200),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5)
            cv2.putText(img,"Lower until thighs are",(50,250),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
            cv2.putText(img,"parallel to the ground",(50,300),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
            cv2.putText(img,"or slightly below.",(50,350),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
            # print(angle,per,count)
    
            #Drawing Curl Count
            cv2.rectangle(img,(0,450),(400,720),(0,255,0),-1)
            if count<10:
                    cv2.putText(img,'0'+str(int(count)),(45,670),cv2.FONT_HERSHEY_PLAIN,15,(255,0,0),25)
            else:
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
    
    
def pushups(name):
    cap = cv2.VideoCapture(name)
    detector = pm.poseDetector()
    
    count = 0
    dir = 0
    pTime = 0

    while True:
        success,img = cap.read()
        if success == False:
            st.write("Video ended!")
            break
        img = cv2.resize(img,(1280,720))
        img = detector.findPose(img,False)
        lmList = detector.findPosition(img,False)
        
        if len(lmList)!=0:
            angle = detector.findAngle(img,11,13,15)
            b = detector.findAngle(img,12,14,16)
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
            #Drawing the Bar
            cv2.rectangle(img,(1100,100),(1175,650),color,3)
            cv2.rectangle(img,(1100,int(bar)),(1175,650),color,-1)  
            cv2.putText(img,f'{int(per)} %',(1100,75),cv2.FONT_HERSHEY_PLAIN,4,color,4) 
            # print(angle,per,count)
            
            cv2.putText(img,"TIP :- ",(55,200),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5)
            cv2.putText(img,"Hands should be",(50,250),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
            cv2.putText(img,"shoulder-width apart",(50,300),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
            cv2.putText(img,"or slightly wider.",(50,350),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
            
            
            #Drawing Curl Count
            cv2.rectangle(img,(0,450),(400,720),(0,255,0),-1)
            if count<10:
                    cv2.putText(img,'0'+str(int(count)),(45,670),cv2.FONT_HERSHEY_PLAIN,15,(255,0,0),25)
            else:
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
    
    
def pullups(name):
    cap = cv2.VideoCapture(name)
    detector = pm.poseDetector()
    
    count = 0.5
    dir = 0
    pTime = 0

    while True:
        success,img = cap.read()
        if success == False:
            st.write("Video ended!")
            break
        img = cv2.resize(img,(1280,720))
        # img = cv2.imread(cap)
        # img = cv2.resize(img,(0,0),fx=0.3,fy=0.3)
        img = detector.findPose(img,False)
        lmList = detector.findPosition(img,False)
        
        if len(lmList)!=0:
                angle = detector.findAngle(img,11,13,15)
                angle2 = detector.findAngle(img,12,14,16)
                per = np.interp(angle,(45,120),(100,0))
                bar = np.interp(angle,(45,120),(100,650))
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
                cv2.putText(img,"TIP :- ",(55,200),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5)
                cv2.putText(img,"Aim to bring your chin",(50,250),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
                cv2.putText(img,"over the bar while",(50,300),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
                cv2.putText(img,"keeping your chest up.",(50,350),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
            
                #Drawing Curl Count
                cv2.rectangle(img,(0,450),(400,720),(0,255,0),-1)
                if count<10:
                    cv2.putText(img,'0'+str(int(count)),(45,670),cv2.FONT_HERSHEY_PLAIN,15,(255,0,0),25)
                else:
                    cv2.putText(img,str(int(count)),(45,670),cv2.FONT_HERSHEY_PLAIN,15,(255,0,0),25)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime   
        cv2.putText(img,str(int(fps)),(50,100),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),5) 
        cv2.imshow('Image',img)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def crunches(name):
    cap = cv2.VideoCapture(name)
    detector = pm.poseDetector()
    
    count = 0.5
    dir = 0
    pTime = 0

    while True:
        success,img = cap.read()
        if success == False:
            st.write("Video ended!")
            break
        img = cv2.resize(img,(1280,720))
        # img = cv2.imread(cap)
        # img = cv2.resize(img,(0,0),fx=0.3,fy=0.3)
        img = detector.findPose(img,False)
        lmList = detector.findPosition(img,False)
        
        if len(lmList)!=0:
                angle = detector.findAngle(img,11,23,25)
                angle2 = detector.findAngle(img,12,24,26)
                per = np.interp(angle,(50,120),(100,0))
                bar = np.interp(angle,(50,120),(100,650))
                # print(angle,per)
                
                cv2.putText(img,"TIP :- ",(55,200),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5)
                cv2.putText(img,"Engage your core.",(50,250),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
                cv2.putText(img,"Contract your",(50,300),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
                cv2.putText(img,"abdominal muscles.",(50,350),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
                
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
                cv2.rectangle(img,(0,450),(400,720),(0,255,0),-1)
                if count<10:
                    cv2.putText(img,'0'+str(int(count)),(45,670),cv2.FONT_HERSHEY_PLAIN,15,(255,0,0),25)
                else:
                    cv2.putText(img,str(int(count)),(45,670),cv2.FONT_HERSHEY_PLAIN,15,(255,0,0),25)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime   
        cv2.putText(img,str(int(fps)),(50,100),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),5) 
        cv2.imshow('Image',img)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_pushups = load_lottie_url("https://lottie.host/4cecf996-9d7f-4888-a375-d4842a17c12b/ksmPX5aZR3.json")
lottie_squats = load_lottie_url("https://lottie.host/4363854b-2c2b-4537-a383-f0643a43a72c/zZM8RPYYAp.json")
lottie_bicepcurls = load_lottie_url("https://lottie.host/947a6117-968a-40e1-8502-20476249a636/oFc6s8bFwM.json")
lottie_pullups = load_lottie_url("https://lottie.host/c4efc767-60c9-4566-be9d-c8627727d9f5/Czj57r03mq.json")
lottie_crunches = load_lottie_url("https://lottie.host/03fec747-865f-4a4f-aa2a-9200841b866d/MhWCvIcr3B.json")


def main():
    st.set_page_config(page_title="Personal AI Instructor",layout="wide")
    st.markdown("<h1 style='text-align: center;font-size:70px'>Personal AI Instructor</h1>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center'>Welcome to your personal workout assistant as well as instructor. </h3>", unsafe_allow_html=True) 
    

    div_width = "100%"

    # Centering the div and adding text inside it using HTML
    st.write(f"""
        
        <div style="width: {div_width}; height:20vh;margin: 0 auto; padding: 20px;text-align:center; border-radius: 10px;">
            <p style='font-family:Times Nes Roman;font-size:20px;'>The Personal AI Instructor is a fitness companion employing advanced technology like computer vision and machine learning. It tracks exercises such as bicep curls, pull-ups, sit-ups, squats, and push-ups, counting reps and assessing form in real-time. Users receive instant feedback on their performance, including a percentage rating for exercise effectiveness. Personalized tips and recommendations cater to individual fitness levels and goals, covering posture, breathing, and muscle targeting. This groundbreaking tool revolutionizes workouts by providing accurate feedback, rep counting, and tailored guidance, ensuring efficient and safe progress towards fitness objectives.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True) 
    
    choice = -1
    ex = -1 
    name = -1
    with st.container():
        st.write("---")
        st.header("Exercises that you can perform")
        left_column,right_column = st.columns((3,1))
        with left_column :
            st.header("Push Ups")
            st.write("Push-ups are a foundational bodyweight exercise that targets the chest, shoulders, and triceps, as well as engages the core muscles. To perform a push-up, start in a plank position with hands shoulder-width apart, lower the body by bending the elbows until the chest nearly touches the ground, then push back up to the starting position. Push-ups are effective for building upper body strength, improving muscular endurance, and promoting overall upper body stability.")
            st.header("Squats")
            st.write("Squats are a fundamental lower body exercise that targets multiple muscle groups, including the quadriceps, hamstrings, glutes, and lower back. By standing with feet shoulder-width apart and lowering the body by bending the knees and hips, squats engage the muscles in a compound movement pattern. This exercise improves lower body strength, enhances balance and stability, and promotes functional movement patterns essential for daily activities and athletic performance. Squats can be performed with bodyweight or added resistance for increased intensity.")
            st.header("Bicep Curls")
            st.write("Bicep curls are a fundamental strength-building exercise that targets the biceps brachii muscles. Typically performed with dumbbells or a barbell, bicep curls involve flexing the elbows to lift the weight towards the shoulders while keeping the upper arms stationary. This exercise is highly effective in increasing arm strength, improving muscle definition, and enhancing overall upper body aesthetics. Bicep curls are versatile and can be modified with variations such as alternating curls, hammer curls, or preacher curls for added challenge and muscle engagement.")
            st.header("Pull Ups")
            st.write("Pull-ups are a challenging bodyweight exercise that target the upper body muscles, particularly the back, biceps, and forearms. To perform a pull-up, grasp an overhead bar with palms facing away, then pull the body upward until the chin clears the bar. This exercise enhances upper body strength, improves grip strength, and boosts overall functional fitness. Pull-ups are versatile, requiring minimal equipment, and can be modified to suit different fitness levels by adjusting grip width or using assistance bands.")
            st.header("Sit Ups")
            st.write("Sit-ups are a core-strengthening exercise that targets the abdominal muscles, particularly the rectus abdominis and obliques. To perform sit-ups, lie on your back with knees bent, feet flat on the floor, and hands behind your head. Engage your core muscles to lift your upper body off the ground towards your knees, then lower back down with control. Sit-ups are effective for improving core stability, enhancing posture, and toning the abdominal muscles.")
        with right_column :
            st_lottie(lottie_pushups, height = 175 , key = "pushups")
            st_lottie(lottie_squats, height = 175 , key = "squats")
            st_lottie(lottie_bicepcurls, height = 150 , key = "bicepcurls")
            st_lottie(lottie_pullups, height = 185 , key = "pullups")
            st_lottie(lottie_crunches, height = 185 , key = "crunches")
         
    with st.container():
        st.write("---")
        st.markdown("<h1 style='text-align: center'>Let's analyse your exercises!</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center'>Which of the above exercises do you want to perform?</h3>",unsafe_allow_html=True)
        
        st.markdown("<br>",unsafe_allow_html=True)
        left_column,right_column = st.columns((2))
        with left_column :
            st.markdown("<h4> <center>Do you want to perform the exercise in real time?</center></h4>",unsafe_allow_html=True)
            st.markdown("""
            <style>
            div.stButton > button { 
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                margin: 4px 35%;
                width: 30%;
            }

            
            </style>""", unsafe_allow_html=True)

            st.markdown("<h4> <center>NOTE - </center></h4>",unsafe_allow_html=True)
            st.markdown("<h6> <center>1.Make sure to have good lighting and low background noise. </center></h6>",unsafe_allow_html=True)
            st.markdown("<h6> <center>2. Postion yourself correctly in front of the camera.</center></h6>",unsafe_allow_html=True)
            
            btn1op1 = st.button("Push Ups",key="1")
            btn1op2 = st.button("Squats",key = "2")
            btn1op3 = st.button("Bicep Curls",key = "3")
            btn1op4 = st.button("Pull Ups",key = "4")
            btn1op5 = st.button("Sit Ups",key = "5")
   
        with right_column :
            st.markdown("<h4> <center>Do you want to analyze an uploaded video?</center></h4>",unsafe_allow_html=True)
            st.markdown("<h5> <center>Enter the file name and click on the exercise being performed.</center></h5>",unsafe_allow_html=True)
            st.markdown("""
            <style>
            div.stButton > button {
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                
                background-color:#666666;
                color:white;
                margin: 4px 35%;
                width: 30%;
            }
            div.stButton > button:hover {
                background-color:white;
                color:black;
                border:2px solid black;
                }

             
            </style>""", unsafe_allow_html=True)
            
            ip = st.text_input("Enter file name : ",placeholder="filename.mp4")
            btn2op1 = st.button("Push Ups",key="6")
            btn2op2 = st.button("Squats",key = "7")
            btn2op3 = st.button("Bicep Curls",key = "8")
            btn2op4 = st.button("Pull Ups",key = "9")
            btn2op5 = st.button("Sit Ups",key = "10")
            
        st.write("---")
        st.markdown("<h4> <center>For any further queries or information about the project contact the team members mentioned below.</center></h4>",unsafe_allow_html=True)
        st.markdown("<br>" ,unsafe_allow_html=True)
        st.markdown("<h5> <center>Anushka Priyadarshini : 21052813@gmail.com</center></h5>",unsafe_allow_html=True)
        st.markdown("<h5> <center>Kumar Harsh : 21052842@gmail.com</center></h5>",unsafe_allow_html=True)
        st.markdown("<h5> <center>Raxit Singh : 21052915@gmail.com</center></h5>",unsafe_allow_html=True)
        st.markdown("<h5> <center>Ripudaman Singh Walia : 2105138@gmail.com</center></h5>",unsafe_allow_html=True)
        st.markdown("<h5> <center>Saumyajeet Jena : 21052919@gmail.com</center></h5>",unsafe_allow_html=True)

        if btn1op1 == True:
            ex = 1
            name = 0
            pushups(name)
        elif btn1op2 ==True:
            ex = 1
            name = 0
            squats(name)
        elif btn1op3 ==True:
            ex = 1
            name = 0
            bcurls(name)
        elif btn1op4 ==True:
            ex = 1
            name = 0
            pullups(name)
        elif btn1op5 ==True:
            ex = 1
            name = 0
            crunches(name)
        elif btn2op1 ==True:
            ex = 2
            name = "PoseVideos/"
            name = name+ip
            st.write(name)
            pushups(name)
        elif btn2op2 ==True:
            ex = 2
            name = "PoseVideos/"
            name = name+ip
            st.write(name)
            squats(name)
        elif btn2op3 ==True:
            ex = 2
            name = "PoseVideos/"
            name = name+ip
            st.write(name)
            bcurls(name)
        elif btn2op4 ==True:
            ex = 2
            name = "PoseVideos/"
            name = name+ip
            st.write(name)
            pullups(name)
        elif btn2op5 == True: 
            ex = 2
            name = "PoseVideos/"
            name = name+ip
            st.write(name)
            crunches(name)
            
if __name__ == "__main__":
    main()
