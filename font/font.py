# coding: utf8
from PIL import Image, ImageFont, ImageDraw

image = Image.new('RGBA', (400,300), (248, 248, 224,0))
draw = ImageDraw.Draw(image)

# use a truetype font
font = ImageFont.truetype("FZShaoEr.ttf", 14)

text = u'''
存档 操作方式 上左右 上
睡眠 文字速度 普通快慢
设定 标记 开关
返回 确定 取消

我们的太阳
'''

draw.text((0, 0), text, font=font, fill=(152,80,80,0))

image.save('font.tile.bmp','BMP')
