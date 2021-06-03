import os
from moviepy.editor import VideoFileClip


def mp4_a_mp3(ruta, nombre):

    video = VideoFileClip(os.path.join(ruta,ruta, nombre + ".mp4"))
    video.audio.write_audiofile(os.path.join(ruta,ruta, nombre + " mp3" + ".mp3"))
