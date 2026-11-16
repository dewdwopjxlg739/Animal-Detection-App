import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# set background image
from util import add_bg
add_bg("/Users/zhukaihong/Desktop/Personal.Project/Website Articles - DO NOT DELETE/vecteezy_pastel-blue-aesthetic-background-can-use-for-print_13109681.jpg")

# set title
st.title("Cat, Duck, or Rabbit?")

# set header
st.header("Please upload an image! <3")

# upload file
file = st.file_uploader('', type=['png', 'jpg', 'jpeg'])

# load model
model = YOLO("/Users/zhukaihong/PycharmProjects/Personal_Project/runs/detect/train11/weights/best.pt")

# produce results
if file:
    image = Image.open(file).convert("RGB")
    image_array = np.array(image)

    results = model(image_array)[0]
    annotated = results.plot()

    st.image(annotated, caption="Detections")

# simple explanation paragraph for the code
st.subheader("The Coding Process Behind This Project")
st.markdown(
    """
    This app uses object-oriented code to run your image through my trained YOLOv8 model that recognizes 
    ducks, cats, and rabbits. The uploaded image is opened using PIL, converted to a NumPy array, and
    then passed into a YOLO results object, which draws the bounding boxes you see. If you would also like 
    to learn how to create a project just like this, reference the video linked below or ask me
    for portions of my more detailed personal project process journal!
    https://www.youtube.com/watch?v=UL2cfTTqdNo&t=15499s
    """
)
st.subheader("Screenshots of my code:")
st.markdown('The "train.py" file for the training process:')
st.image('/Users/zhukaihong/Desktop/Personal.Project/Website Articles - DO NOT DELETE/Screenshot 2025-11-30 at 11.08.54 PM.png')
st.markdown('The "data.yaml" file for directories to my datasets used for training:')
st.image('/Users/zhukaihong/Desktop/Personal.Project/Website Articles - DO NOT DELETE/Screenshot 2025-11-30 at 11.09.22 PM.png')
st.markdown('The "util.py" file for this website:')
st.image('/Users/zhukaihong/Desktop/Personal.Project/Website Articles - DO NOT DELETE/Screenshot 2025-12-01 at 11.55.45 PM.png')
st.markdown('The "app.py" file for this website:')
st.image('/Users/zhukaihong/Desktop/Personal.Project/Website Articles - DO NOT DELETE/Screenshot 2025-12-01 at 11.55.02 PM.png')
st.image('/Users/zhukaihong/Desktop/Personal.Project/Website Articles - DO NOT DELETE/Screenshot 2025-12-01 at 11.55.29 PM.png')

# my journey with coding
st.subheader("My Coding Journey")
st.markdown(
    """
    To state simply, I was never the type of person who would throw myself into a newfound passion as fast 
    as some others may, but it was my father’s dedication to programming that sparked my interest. My desire 
    to keep up with technological advancements led me to select coding for my personal project. Before this project, 
    I used to feel intimidated by programming, but building the project step-by-step helped me overcome that fear. 
    As I started with an object-identification concept that is quite difficult for beginners, I feel more confident 
    and well-equipped for future learning and starting with the basics. My personal project was just the push I needed 
    to officially begin programming!
    """
)