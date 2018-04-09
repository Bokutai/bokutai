# coding: utf8

pt_start = 0xCF3ED2
#0xD7179E start
#0xD275B2 item
col = 20
row = 9
index = 14

attr_start = 0xCF3FAD
#0xD71915 start
#0xD2808D item

#attrib D286A5-D28993
rom = open('../../hack/rom/bokutai.gba', 'r').read()
pt_area = rom[pt_start:pt_start + col * row]

comment = [
	"太陽センサーとは (太阳感应器是什么)",
	"太陽センサーの効果 (太阳感应器的效果)",
	"使用上の注意 (使用注意)",
	"向き・傾き (方向・倾斜)",
	"太陽センサーと場所 (太阳感应器与场所)",
	"太陽センサーと時間 (太阳感应器与时间)",
	"太陽センサーと天気 (太阳感应器与天气)",
	"炎天下 (烈日下)",
	"太陽センサーと？ (太阳感应器与谜题)",
]
size = [
]

tile_start =  (ord(pt_area[index+1]) << 8) + ord(pt_area[index])

for i in range(0, row):
	piece = pt_area[i*col:(i+1)*col]
	tile_size_adr = pt_start + i*col
	tile_size = ord(piece[0])
	print '\n;%s' % comment[i]
	print '.org 0x08%6X' % tile_size_adr
	print '.byte 0x%02X' % tile_size

	tile_offset_adr = tile_size_adr + index
	tile_start_str = '%04X' % tile_start
	print '.org 0x08%6X' % tile_offset_adr
	print '.byte 0x%s,0x%s' % (tile_start_str[2:], tile_start_str[:2])

	print '\n.org 0x08%6X' % (attr_start + tile_start)
	atr_adr = attr_start + (ord(piece[index+1]) << 8) + ord(piece[index])
	tile_area = rom[atr_adr:atr_adr + 8 * tile_size]
	for t in range(0, tile_size):
		text = '.byte '
		for char in tile_area[t*8:t*8+8]:
			text += '0x%02X,' % ord(char)
		print text[:-1]

	tile_start += 8 * tile_size