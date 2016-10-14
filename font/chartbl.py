# coding: utf8

fonts = (
	('ascii', 0x20),
	('font', 0x8000),
	# ('font.tgb', 0x8500),
)

for font in fonts:
	pos = font[1]
	font = open(font[0]+'.txt', 'r')
	for line in font.readlines():
		line = line.strip().decode('utf8')
		for chart in line:
			pos += 1
			print '%X=%s' % (pos, chart.encode('utf8'))