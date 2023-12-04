import streamlit as st
import base64
import os
import time

st.set_page_config(layout="wide")

def get_video_base64(video_path):
    if os.path.exists(video_path):
        with open(video_path, "rb") as file:
            video_base64 = base64.b64encode(file.read()).decode("utf-8")
        return video_base64
    else:
        st.error("Video file not found.")

video_path_response = r"C:\Users\mohci\Downloads/adobestock-95385826-video-hd-preview_l3gl8iQ5.mp4"
video_path_transition = r"C:\Users\mohci\Downloads/adobestock-325606362-video-hd-preview-3odvyozu_QseLBMXP.mp4"
video_path_sign_up = r"C:\Users\mohci\Downloads/untitled-video-made-with-clipchamp-1_VX3IUxCI.mp4"

video_base64 = get_video_base64(video_path_transition)

video_html = f"""
    <style>
        
        
        #myVideo {{
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            object-fit: cover;
        }}
        .content {{
            position: fixed;
            bottom: 0;
            background: rgba(0, 0, 0, 0.5);
            color: #f1f1f1;
            width: 100%;
            padding: 20px;
            box-sizing: border-box;
        }}
    </style>
    <video autoplay muted loop id="myVideo">
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        Your browser does not support HTML5 video.
    </video>
    """

video_container_transition = st.empty()
video_container_transition.markdown(video_html, unsafe_allow_html=True)

# Wait for a few seconds (you can adjust the duration)
time.sleep(5)

# Clear the transition video
video_container_transition.empty()

# Now, you can display your new content
st.write("Your new content goes here.")


