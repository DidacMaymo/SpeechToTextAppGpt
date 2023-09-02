# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import os

import openai

openai.api_key = os.environ['OPENAI_API_KEY']
mp3_file_path = "TheArchers-20230820.mp3"

# Extract the base name of the MP3 file (without the extension)
base_name = os.path.splitext(mp3_file_path)[0]

# Transcribe the audio
audio_file = open(mp3_file_path, "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

# Extract the text content from the transcript object
transcript_text = transcript['text']

# Specify the path to the text file with the same name as the MP3 file
output_file_path = f"{base_name}.txt"

# Write the transcript to the text file
with open(output_file_path, "w") as output_file:
    output_file.write(transcript_text)

# Close the audio file
audio_file.close()

# Print a message indicating that the transcript has been saved
print(f"Transcript saved to {output_file_path}")
