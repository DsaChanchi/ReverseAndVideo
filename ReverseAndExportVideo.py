from pydub import AudioSegment
from moviepy.editor import *
import pathlib
import os
import errno
import cv2

#ReverseAudio
#ListadoArchivos
directorioactual = pathlib.Path()
#Filtrado de canciones y generacion ver.reverse
for archivo in directorioactual.iterdir():
    if archivo.is_file() and archivo.name.endswith('.mp3'):
        song = AudioSegment.from_mp3(archivo.name)
        backwards = song.reverse()
        audio = (archivo.name[:-4])
        backwards.export(audio+"backwards.mp3", format="mp3")
        

#Busqueda de imagen
for archivo in directorioactual.iterdir():
    if archivo.is_file() and archivo.name.endswith('.jpg'):
        original = cv2.imread(archivo.name)
        image = cv2.flip(original,-1)

#Generacion de video
for inverso in directorioactual.iterdir():
    if inverso.is_file() and inverso.name.endswith('backwards.mp3'):
        background = AudioFileClip(inverso.name) # Import the audio
        video = ImageClip(image).set_duration(background.duration) # Import the image, create the video and set its duration same as the audio
        video = video.set_audio(background) # Set the audio of the video
        video.write_videofile(inverso.name[:-4]+".mp4", fps=24) # Export the video