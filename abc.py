import streamlit as st
from main import predict_on_video
from image import predict_on_image


page=st.sidebar.selectbox("Image or Video",("Image","Video"))
st.title("Object Detection Web Application")
st.write("""### We need some information to detect the objects""")
if page=="Video":
    predict_on_video()
else:
    predict_on_image()