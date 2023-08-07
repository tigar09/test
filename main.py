from ultralytics import YOLO
import streamlit as st

model = YOLO("yolov8x.pt") 

st.title('test')