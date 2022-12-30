import pytube
from pytube import YouTube
import ffmpeg
import pydub
from pydub import AudioSegment

from tkinter import *
import tkinter

def YouTubeMusicDownload(URL):
    # Step 1: Create a YouTube object
    yt = YouTube(URL)
    SongName = yt.title
    print(SongName)
    #Step 2: Choose the audio stream
    audio_stream = yt.streams.get_highest_resolution()
    # Step 3: Download the audio stream
    audio_stream.download("C:/Users/aa/Downloads/musicfolder")
    # Step 4: Convert the downloaded file to an MP3 file
    given_audio = AudioSegment.from_file("C:/Users/aa/Downloads/musicfolder/" + SongName +".mp4", format="mp4")
    given_audio.export("C:/Users/aa/Downloads/musicfolder/" + SongName + ".mp3", format="mp3")

#GUI TIME
#YouTubeMusicDownload("https://www.youtube.com/watch?v=8AFv7xCNJmE")

root = tkinter.Tk()
root.title("YouTube to MP3 Converter")
root.geometry("600x300")
root.configure(bg="lemon chiffon")

frame = tkinter.Frame(master=root)
frame.pack(pady=30,padx=30, expand=True)
frame.configure(bg="green")

label = tkinter.Label(master=frame, text="Input URL and Click Download")
label.pack(pady=10,padx=10)

url1 = tkinter.Entry(master=frame, width=80)
url1.pack(pady=11, padx=11)

#button = tkinter.Button(master=frame, text="Download", command=lambda:print(url1.get()))
button = tkinter.Button(master=frame, text="Download", relief= GROOVE, command=lambda:YouTubeMusicDownload(url1.get()))
button.pack(pady=9,padx=9)
root.mainloop()