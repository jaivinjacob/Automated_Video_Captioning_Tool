from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
from pydub import AudioSegment
import speech_recognition as sr
import os

def insert_caption_audio(video_path, caption_audio_path, output_video_path):
    # Load the video and extract audio
    video = VideoFileClip(video_path)
    audio_path = "temp_audio.wav"
    video.audio.write_audiofile(audio_path)

    # Load the audio using pydub
    audio = AudioSegment.from_file(audio_path, format="wav")

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Define the step (chunk size) in milliseconds
    step = 1000  # 1 second

    # List to store non-speech ranges
    non_speech_ranges = []

    # Loop through the audio file in chunks
    for i in range(0, len(audio), step):
        chunk = audio[i:i + step]
        chunk_path = f"chunk_{i // step}.wav"
        chunk.export(chunk_path, format="wav")

        # Recognize speech in the chunk
        with sr.AudioFile(chunk_path) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
                print(f"Speech detected: '{text}' at {i / 1000}s to {(i + step) / 1000}s")
            except sr.UnknownValueError:
                print(f"No speech detected at {i / 1000}s to {(i + step) / 1000}s")
                non_speech_ranges.append((i / 1000, (i + step) / 1000))
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

        # Clean up the chunk file
        os.remove(chunk_path)

    # Clean up the extracted audio file
    os.remove(audio_path)

    # Combine consecutive non-speech ranges if they are continuous
    combined_non_speech_ranges = []
    current_range = None

    for start, end in non_speech_ranges:
        if current_range is None:
            current_range = [start, end]
        else:
            if start == current_range[1]:
                current_range[1] = end
            else:
                combined_non_speech_ranges.append(tuple(current_range))
                current_range = [start, end]

    if current_range is not None:
        combined_non_speech_ranges.append(tuple(current_range))

    # Display non-speech ranges
    print("Non-speech ranges detected:", combined_non_speech_ranges)

    # Load the audio description
    caption_audio = AudioFileClip(caption_audio_path)
    caption_duration = caption_audio.duration

    # Find a suitable non-speech range
    suitable_range = None
    for start, end in combined_non_speech_ranges:
        if (end - start) >= caption_duration:
            suitable_range = (start, end)
            break

    # Insert audio description into the suitable non-speech range
    if suitable_range:
        start_non_speech, end_non_speech = suitable_range
        print(f"Inserting audio description into non-speech part from {start_non_speech} to {end_non_speech} seconds")

        # Trim or extend the caption audio to fit the non-speech part
        caption_audio = caption_audio.subclip(0, caption_duration)

        # Split the video into three parts: before, non-speech part, and after
        video_before = video.subclip(0, start_non_speech)
        video_non_speech = video.subclip(start_non_speech, start_non_speech + caption_duration)
        video_after = video.subclip(start_non_speech + caption_duration)

        # Replace the non-speech part's audio with the caption audio
        video_non_speech = video_non_speech.set_audio(caption_audio)

        # Concatenate the video parts back together
        final_video = concatenate_videoclips([video_before, video_non_speech, video_after])

        # Save the final video
        final_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
    else:
        print("No suitable non-speech part found in the video.")

