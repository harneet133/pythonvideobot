from moviepy.editor import *
from imagesaver import gen_sou

gen_sou(5)

audio1 = AudioFileClip("audio/speech0.mp3")
audio2 = AudioFileClip("audio/speech1.mp3")
audio3 = AudioFileClip("audio/speech2.mp3")
audio4 = AudioFileClip("audio/speech3.mp3")
audio5 = AudioFileClip("audio/speech4.mp3")
audio1end = audio1.duration + 1
audio2end = audio2.duration + audio1end + 1
audio3end = audio3.duration + audio2end + 1
audio4end = audio4.duration + audio3end + 1
final = CompositeAudioClip([audio1.set_start(0), audio2.set_start(audio1end), audio3.set_start(audio2end),
                            audio4.set_start(audio3end), audio5.set_start(audio4end)])

audioclip = final.set_fps(44100)
audioclip.write_audiofile("audio.mp3")
image1 = ImageClip("images/img0.png").set_duration(audio1.duration+1)
image2 = ImageClip("images/img1.png").set_duration(audio2.duration+1)
image3 = ImageClip("images/img2.png").set_duration(audio3.duration+1)
image4 = ImageClip("images/img3.png").set_duration(audio4.duration+1)
image5 = ImageClip("images/img4.png").set_duration(audio5.duration+1)

videofinalfile = CompositeVideoClip([image1.set_start(0), image2.set_start(audio1end),
                                     image3.set_start(audio2end), image4.set_start(audio3end),
                                     image5.set_start(audio4end)])
videofinalfile.audio = AudioFileClip("audio.mp3")
videofinalfile.write_videofile("hehe.mp4", fps=24)
