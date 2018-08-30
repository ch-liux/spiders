'''
Created on 2018年8月18日

@author: Administrator
'''

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def ranFont():
    return chr(random.randint(65, 90))
def ranColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
def ranColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
width = 60 * 4
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('C:\\Windows\\Fonts\\arial.ttf', 36)
draw = ImageDraw.Draw(image)
for w in range(width):
    for h in range(height):
        draw.point((w, h), fill=ranColor1())
for f in range(4):
    draw.text((60* f + 10, 10), ranFont(), font=font, fill=ranColor2())
image = image.filter(ImageFilter.BLUR)
image.save('demo11.jpg', 'jpeg')

