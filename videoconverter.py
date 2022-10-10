from moviepy.editor import *
from imagesaver import gen_sou
import os

gen_sou(3)

audiofolder = "audio/"
audio_files = os.listdir(audiofolder)
imagesfolder = "images/"
image_files = os.listdir(imagesfolder)


audio_clips = [AudioFileClip(f"audio/speech{i}.mp3") for i in range(len(audio_files))]
audio_concat = concatenate_audioclips(audio_clips)
audio_composite = CompositeAudioClip([audio_concat])
audioclip = audio_composite.set_fps(44100)
audioclip.write_audiofile("finalaudio.mp3")

images_clips_list = []
for i in range(0, len(image_files)):
        images_clips_list.append(
            ImageClip(f"images/img{i}.png")
            .set_duration(audio_clips[i].duration)
        )
image_concat = concatenate_videoclips(images_clips_list)
image_concat.audio = AudioFileClip("finalaudio.mp3")
image_concat.write_videofile("finalvideo.mp4", fps=24)
os.remove("finalaudio.mp3")
for i in range(len(image_files)):
    os.remove(f"images/img{i}.png")
    os.remove(f"audio/speech{i}.mp3")

    
