# coding: utf8

'''
Bitmap fonts generating

todo: 
	
'''

import sys

if len(sys.argv) < 5:
	print 'Usage: python %s [text_file] [color] [size] [bmp_name]' % sys.argv[0]
	exit()

from PIL import Image, ImageFont, ImageDraw

#read text
f = open(sys.argv[1], 'r')
text = f.read()
f.close()

#parse color
color = sys.argv[2]
color = [color[i:i+2] for i in range(0, len(color), 2)]
rgb = tuple(map(lambda x:int(x,16), color))

image = Image.new('RGB', (400, 300), (255, 255, 255))
draw = ImageDraw.Draw(image)

# use a truetype font
font = ImageFont.truetype("FZShaoEr.ttf", int(sys.argv[3]))

draw.text((0, 0), text.decode('utf8'), font=font, fill=rgb)

# pal = open('item.act').read()[:768]
# image = image.convert(mode='P', palette=pal)
image.save(sys.argv[4], 'BMP', quality=100, dpi=(72, 72))