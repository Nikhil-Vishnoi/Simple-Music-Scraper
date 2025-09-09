# Convert .m4a files into .mp3 files 
from pydub import AudioSegment
import os 
target = "Downloaded/drop1/"
output = "Downloaded/drop1Parsed/"


def convert_m4a_to_mp3(m4a_file, mp3_file):
    print(m4a_file)
    print(mp3_file)
    """Converts an M4A file to MP3."""
    audio = AudioSegment.from_file(m4a_file, format="m4a")
    audio.export(mp3_file, format="mp3")

files = os.listdir(target) 
for file in files: 
    print(file)
    convert_m4a_to_mp3((target+file),(output+file).replace('m4a','mp3'))