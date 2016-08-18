# coding: utf8

sta = 0x0E2B72C
end = 0x0E5231E
rom = open('../crack/rom/bokutai.gba', 'r')
# rom = open('../crack/rom/bokutai.tgb.gba', 'r')
textbin = rom.read()[sta: end] 
chartbl =  open('../font/font.tbl', 'r')
# chartbl = open('../font.tgb.tbl', 'r')

tbl=dict()
for line in chartbl.readlines():
	k,v = line.strip().split('=', 1)
	tbl[k] = v 

text = ''
char = None
count = 0
for byte in textbin:
	byte = ord(byte)
	if char==None:
		if byte >= 0x80 and byte < 0x8A:
			char = '%02X' % byte
			continue
		elif byte == 0x0A:
			text += '\n'
		elif byte == 0x20:
			text += ' '
		elif byte == 0x00:
			count += 1
			print 'No.%s' % count
			print '----------------' 
			print text
			print '----------------\n' 
			text = ''
			continue
		else:
			ascii = '%02X' % byte
			str = tbl.get(ascii)
			if str == None:
				text += '{%s}' % ascii
			else:
				text += str
	else:
		char += '%02X' % byte
		str = tbl.get(char)
		if str == None or str == '　':
			text += '{%s}' % char
		else:
			text += str
		char = None
