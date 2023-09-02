# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import os
import openai
import tkinter as tk
from tkinter import filedialog

openai.api_key = os.environ['OPENAI_API_KEY']

# Function to handle transcription
# Function to handle transcription
def transcribe_audio():
    # Prompt the user to select an audio file using a file dialog
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])

    if file_path:
        # Extract the base name of the selected audio file (without the extension)
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        print(base_name)

        # Transcribe the selected audio
        audio_file = open(file_path, "rb")
        transcription_result = openai.Audio.transcribe("whisper-1", audio_file)

        # Extract the text content from the transcription result
        transcript_text = transcription_result['text']

        # Prompt the user to choose where to save the transcript text file
        save_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

        if save_file_path:
            # Write the transcript text to the selected file
            with open(save_file_path, "w") as output_file:
                output_file.write(transcript_text)

            # Close the audio file
            audio_file.close()

            # Print a message indicating that the transcript has been saved
            print(f"Transcript saved to {save_file_path}")

# Create a GUI window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Call the function to select and transcribe an audio file
transcribe_audio()