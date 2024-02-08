# Open the folder BlogAudio and create a file with the length of each audio file in seconds

import os
import pydub

# get the current working directory
path = os.getcwd()

# change the working directory to BlogAudio
os.chdir(path + "/BlogAudio")

# get the current working directory
path = os.getcwd()

# get a list of all files in the directory
files = os.listdir(path)

# loop through the files
for file in files:
    # get the length of the audio file
    audio = pydub.AudioSegment.from_file(file)
    length = len(audio) / 1000
    # create a file with the length of the audio file
    # the file is a csv file with 2 columns Name,Length (seconds)
    with open("audio_lengths.csv", "a") as f:
        f.write(f"{file},{length}\n")
        print(f"{file} has a length of {length} seconds")