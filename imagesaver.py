import textwrap
import randfacts
import pyttsx3
import time
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS


def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=20)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text),
                  line, font=font, fill=text_color)
        y_text += line_height


def gen_sou(time):
    for i in range(time):
        y = randfacts.get_fact()
        print(y)
        st = str(i)
        img = Image.new('RGB', (1080, 1920), color=(73, 109, 137))
        fnt = ImageFont.truetype('RobotoMono-VariableFont_wght.ttf', 80)
        text_start_height = 200
        text_color = '#ffffff'
        draw_multiple_line_text(img, "Did You Know " + y, fnt, text_color, text_start_height)
        img.save('images/img'+st+'.png')
        tts = gTTS("Did you know," + y)
        tts.save('audio/speech'+st+'.mp3')
