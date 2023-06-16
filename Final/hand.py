import tensorflow as tf
import mediapipe as mp
import numpy as np
import cv2

interpreter = tf.lite.Interpreter(model_path='model/pose017.tflite')
interpreter.allocate_tensors()

# 获取输入和输出张量的索引
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def cos1(ax,ay,bx,by,cx,cy):#計算角度
    #handangle1=((cx-bx)*(ax-bx)+(cy-by)*(ay-by))/(((cx-bx)**2)**0.5+((cy-by)**2)**0.5)
    handangle1=((ax-bx)*(cx-bx)+(ay-by)*(cy-by))/((((ax-bx)**2+(ay-by)**2)**0.5)*(((cx-bx)**2+(cy-by)**2)**0.5))
    handangle2=np.degrees(np.arccos(handangle1))
    return handangle2
def howlong(ax,ay,bx,by):#計算兩點之間的長度
    fingerlong=round(abs(((ax-bx)**2+(ay-by)**2)**0.5),2)
    return fingerlong
cap=cv2.VideoCapture(0)
mpHands = mp.solutions.hands #手部追蹤模組
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
num=[1,5,9,13,17]
THRESHOLD = 0.85

import numpy as np

while True:
    ret, img = cap.read()
    imgH = img.shape[0]
    imgW = img.shape[1]
    if ret == True:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)
        if result.multi_hand_landmarks:
            for handlms in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)
                allcsvdata = []  # 初始化为空列表
                for i, lm in enumerate(handlms.landmark):
                    Xpoint = lm.x
                    Ypoint = lm.y
                    allcsvdata.extend([Xpoint, Ypoint])  # 将Xpoint和Ypoint追加到allcsvdata列表中

                allcsvdata = np.array([allcsvdata], dtype=np.float32)  # 将列表转换为NumPy数组
                interpreter.set_tensor(input_details[0]['index'], allcsvdata)
                interpreter.invoke()
                output_data = interpreter.get_tensor(output_details[0]['index'])
                predicted_classes = np.argmax(output_data, axis=1)
                if np.max(output_data) < THRESHOLD:
                    print("-1")
                else:
                    predicted_classes = np.argmax(output_data, axis=1)
                    print(predicted_classes)
                    # 在螢幕左上角顯示動作編號
                    action_text = "Action: {}".format(predicted_classes)
                    cv2.putText(img, action_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


        cv2.imshow('img', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
