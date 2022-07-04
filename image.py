from main import predict_cordinates,tfnet
from PIL import Image
import numpy as np
import streamlit as st
import cv2


def predict_on_image():
    image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])

    if image_file is not None:
        # To See details
        # file_details = {"filename": image_file.name, "filetype": image_file.type,
        #                 "filesize": image_file.size}
        # st.write(file_details)

        # To View Uploaded Image



        img_file = Image.open(image_file)
        image_file= np.array(img_file)
        frame = cv2.cvtColor(image_file, cv2.COLOR_BGR2RGB)

        result = tfnet.return_predict(frame)
        print(result)

        frame = predict_cordinates(frame,result)

        # image = show_img(frame, confidence, start_point, end_point, label, x1, y2)
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print(frame)
        st.image((frame),channels="BGR",use_column_width='True',caption='Predicted Image')