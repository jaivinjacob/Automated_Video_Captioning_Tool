
import sys
sys.path.append('src')

import streamlit as st
import time
from Gen_auido import Gen_auido
from VPPP import insert_caption_audio
from Model import video_to_descriptions
from Sum_Dis import process_and_summarize
# Title
st.title("Video Processing")

# File uploader
uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:


    video_path = f"./{uploaded_file.name}"
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())



    caption = video_to_descriptions(video_path)
    caption = process_and_summarize(caption)
    Gen_auido(caption)
    
    # Simulate processing with a progress bar
    st.write("Processing video...")
    progress_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.05)  # Simulate processing time
        progress_bar.progress(percent_complete + 1)

    output_video_path = "final_video_with_caption.mp4"

    
    insert_caption_audio(video_path, "caption.mp3", output_video_path)


    # Display video after processing
    st.success(f'"Processing complete!"')
    st.snow()
    st.video("final_video_with_caption.mp4")

# # Usage
# video_path = "Test_Env\sample_video_1.mp4"
# output_video_path = "final_video_with_caption.mp4"