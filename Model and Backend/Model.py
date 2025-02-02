import os
import pandas as pd
from tqdm import tqdm
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import cv2

def video_to_descriptions(video_path, fps=1, max_new_tokens=20):
    # Load the model and processor
    processor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-base')
    model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')

    # Function to generate descriptions for each frame
    def generate_descriptions(image):
        inputs = processor(images=image, return_tensors="pt")
        out = model.generate(**inputs, max_new_tokens=max_new_tokens)
        description = processor.decode(out[0], skip_special_tokens=True)
        return description

    # Function to extract frames from video
    def extract_frames(video_path, fps):
        video = cv2.VideoCapture(video_path)
        frames = []
        frame_rate = int(video.get(cv2.CAP_PROP_FPS))
        interval = frame_rate // fps

        success, image = video.read()
        count = 0

        while success:
            if count % interval == 0:
                # Convert the frame to RGB (OpenCV uses BGR by default)
                image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(image_rgb)
                frames.append(pil_image)
            success, image = video.read()
            count += 1

        video.release()
        return frames

    # Extract frames at the specified frames per second
    frames = extract_frames(video_path, fps)

    # Generate descriptions for each frame
    descriptions = [generate_descriptions(frame) for frame in tqdm(frames)]

    # Return the descriptions
    return descriptions

