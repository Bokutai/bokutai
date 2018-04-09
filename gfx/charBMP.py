# coding: utf8

'''
Bitmap fonts generating

todo: 
	
'''

import sys

if len(sys.argv) < 4:
	print 'Usage: python %s [text_file] [color] [bmp_name]' % sys.argv[0]
	exit()

from PIL import Image, ImageFont, ImageDraw

#read text
f = open(sys.argv[1], 'r')
text = f.read().decode('utf8')
text = text.split('\n')
f.close()

count = len(''.join(text))
line = len(text)

#parse color
color = sys.argv[2]
color = [color[i:i+2] for i in range(0, len(color), 2)]
rgb = tuple(map(lambda x:int(x,16), color))

white = (255, 255, 255)
char = Image.new('RGB', (224, 15*line), white)
char_draw = ImageDraw.Draw(char)

# use a truetype font
font = ImageFont.truetype("FZShaoEr.ttf", 14)
for l,t in enumerate(text):
	char_draw.text((0, 15*l), t, font=font, fill=rgb)

offset = []
for l in range(0, line):
	offset.append([1,1])
	for xp in range(0, 15):
		if char.getpixel((0, l*15+xp)) == rgb:
			offset[l][0] = 0
			break
	for yp in range(0, 224):
		if char.getpixel((yp, (l+1)*15-1)) != white:
			offset[l][1] = 2
			break

image = Image.new('RGB', (192, 12*line), white)
y = 0
for i in range(0, count):
	x = i%16
	y += 1 if not x and i else 0
	o = offset[y]
	part = char.crop((x*14+o[0], y*15+o[1], x*14+12+o[0], y*15+12+o[1]))
	image.paste(part, (x*12, y*12, (x+1)*12, (y+1)*12))

image.save(sys.argv[3], 'BMP', quality=100, dpi=(72, 72))
# char.save('font/org_font.bmp', 'BMP', quality=100, dpi=(72, 72))