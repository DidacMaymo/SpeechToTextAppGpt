import os
import openai
import tkinter as tk
from tkinter import filedialog

openai.api_key = os.environ['OPENAI_API_KEY']

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
        print('Transcription Done')

        # Extract the text content from the transcription result
        transcript_text = transcription_result['text']

        # Obtén la ubicación del archivo MP3
        mp3_directory = os.path.dirname(file_path)

        # Combina la ubicación del archivo MP3 con el nombre del archivo de transcripción
        output_file_path = os.path.join(mp3_directory, f"{base_name}.txt")

        # Escribe el archivo de transcripción en la ubicación deseada
        with open(output_file_path, "w") as output_file:
            output_file.write(transcript_text)

        print('save path')

        audio_file.close()

        # Print a message indicating that the transcript has been saved
        print(f"Transcript saved to {output_file_path}")

# Create a GUI window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Call the function to select and transcribe an audio file
transcribe_audio()
