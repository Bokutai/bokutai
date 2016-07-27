# coding: utf8

post = 0x8000
font = open('font/font.txt', 'r')
for line in font.readlines():
	line = line.strip().decode('utf8')
	for chart in line:
		post += 1
		print '%X=%s' % (post, chart.encode('utf8'))
