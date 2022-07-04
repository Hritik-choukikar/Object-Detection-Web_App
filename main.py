import cv2
import streamlit as st
from darkflow.net.build import TFNet
from PIL import Image
import numpy as np









def load_model():
    options = {"model": "cfg/yolo.cfg", "load": "yolov2.weights", "threshold": 0.1}
    tfnet = TFNet(options)
    return tfnet


tfnet=load_model()

# def show_img(frame,confidence,start_point,end_point,label,x1,y2):
#     color = (255,255,255)
#     # # Line thickness of 1 px
#     thickness = 1
#     image = cv2.rectangle(frame, start_point, end_point, color, thickness)
#     image = cv2.putText(image, "{} [{:.2f}]".format(label, float(confidence)), (x1, y2 - 5), cv2.FONT_HERSHEY_SIMPLEX,
#                         0.5, color, 1)
#     return image

def predict_cordinates(frame,result):
    a = len(result)

    # # create transparent overlay for bounding box
    # image = np.zeros([480,640,4], dtype=np.uint8)

    for i in range(a):
        b = result[i]
        label = b['label']
        confidence = b['confidence']
        topleft = b['topleft']
        bottomright = b['bottomright']
        x1 = topleft['x']
        y2 = topleft['y']
        x2 = bottomright['x']
        y1 = bottomright['y']
        start_point = (x1, y1)
        end_point = (x2, y2)
        print(start_point)
        print(end_point)

        color = (255, 25, 25)
        # # Line thickness of 1 px
        thickness = 1
        image = cv2.rectangle(frame, start_point, end_point, color, thickness)
        image = cv2.putText(image, "{} [{:.2f}]".format(label, float(confidence)), (x1, y2 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, color, 2)


    return image


def predict_on_video():
    #
    # page=st.sidebar.selectbox('Image or Video',("Image","Video"))

    a='Access Camera'
    run = st.button(a, key='djhd')
    FRAME_WINDO2 = st.image([])
    cam = cv2.VideoCapture(0)

    while run:





        ret, frame = cam.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result=tfnet.return_predict(frame)
        image=predict_cordinates(frame,result)


        FRAME_WINDO2.image(image)





            # Ending coordinate, here (220, 220)
            # represents the bottom right corner of rectangle




