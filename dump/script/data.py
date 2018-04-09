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

def le_unpack(bytes):
	return int(bytes[::-1].encode('hex'), 16)

for block in range(0, 4107):
	ptr =  le_unpack(ptr_bin[block*4:(block+1)*4])
	nxt_ptr =  le_unpack(ptr_bin[(block+1)*4:(block+1)*4+3]) if block != 4106 else len(raw_script)
	if ptr < 0x80000000:
		print '%04d: 0x%06X' % (block, ptr + ped)
