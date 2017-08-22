# coding: utf8

#parse script pointer
sta = 0xE27700
ped = 0xE2B72C
end = 0xE5231E

rom = open('../../hack/rom/bokutai.gba', 'r')
# rom = open('../../hack/rom/bokutai.tgb.gba', 'r')
rom_bin = rom.read()[sta:end]
ptr_bin = rom_bin[0:ped-sta]
raw_script = rom_bin[ped-sta:]
rom.close()

chartbl =  open('../font/font.tbl', 'r')
# chartbl = open('../font/font.tgb.tbl', 'r')

tbl = dict()
for line in chartbl.readlines():
	k,v = line.strip().split('=', 1)
	tbl[k] = v
chartbl.close()

def le_unpack(bytes):
	return int(bytes[::-1].encode('hex'), 16)

def covert_script(raw, count):
	text = ''
	char = None
	for byte in raw:
		byte = ord(byte)
		if char == None:
			if byte >= 0x80 and byte < 0x8A:
				char = '%02X' % byte
				continue
			elif byte == 0x0A:
				text += '\n'
			elif byte == 0x20:
				text += ' '
			elif byte == 0x00:
				print 'No.%s' % count
				print '----------------' 
				print text
				print '----------------\n' 
				text = ''
				break
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

for block in range(0, 4107):
	ptr =  le_unpack(ptr_bin[block*4:(block+1)*4])
	nxt_ptr =  le_unpack(ptr_bin[(block+1)*4:(block+1)*4+3]) if block != 4106 else len(raw_script)
	if ptr >= 0x80000000:
		ptr -= 0x80000000
		covert_script(raw_script[ptr:nxt_ptr], block+1)
