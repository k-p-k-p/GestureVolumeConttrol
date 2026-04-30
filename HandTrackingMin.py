import cv2
import mediapipe as mp
import time

# integrated webcam = 0
cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# initialise cTime and pTime to be used to calc frame rates
cTime = 0
pTime = 0

while True:
    success, img = cap.read()
    if not success or img is None:
        print("Failed to capture image from camera.")
        break
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    #  first do all the processing then show the image
    if results.multi_hand_landmarks :
        for handLms in results.multi_hand_landmarks :
            for id , lm in enumerate(handLms.landmark) :
                h , w , c = img.shape 
                cx , cy = int(lm.x * w), int(lm.y * h)
                print(id, cx , cy)
                if id == 0 :
                    cv2.circle(img , (cx , cy) , 25 , (255 , 0 , 255) , cv2.FILLED)
                # thumbX , thumbY = (cx , cy) if id == 4 else  (0 , 0)
                # ringX , ringY = (cx , cy) if id == 8 else  (0 , 0)
                # distance = ( (thumbX - ringX )**2 + (thumbY - ringY)**2 )**(1/2)
                # cv2.putText(img ,
                #     str(int(distance)) ,
                #     (400,200) ,
                #     cv2.FONT_HERSHEY_SIMPLEX ,
                #     3 ,
                #     (255 , 0 , 255) ,
                #     3)
            mpDraw.draw_landmarks(img , handLms , mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1 /(cTime - pTime)
    pTime = cTime
    cv2.putText(
        img ,
        str(int(fps)) ,
        (10,70) ,
        cv2.FONT_HERSHEY_COMPLEX ,
        3 ,
        (255 , 0 , 255) ,
        3
    )


    cv2.imshow("Image", img)
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()