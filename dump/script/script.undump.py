# coding: utf8

import re

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

#import script translation file
trans = open('../../translation/trans.txt', 'r')
trans_script = trans.read()
trans.close()

#build addition character set and table
clr_text = re.sub(u'[\x00-\x7F÷×，。、～ー…ＡＢＬＲ✚・：；「」＋ｘ↑↓→←★♥♪ⅠⅡⅢ□强戈ぃぇ]', '', trans_script.decode('utf8'))
fnt_text = ''
for t in clr_text:
	if t not in fnt_text:
		i = len(fnt_text) + 1
		fnt_text += ('\n' + t) if not i%17 and i else t

fnt_file = open('../../gfx/font/font.txt', 'wb')
fnt_file.write(fnt_text.encode('utf8'))
fnt_file.close()

chartbl =  open('symbol.tbl', 'r')
tbl = dict()
for line in chartbl.readlines():
	k,v = line.strip().split('=', 1)
	tbl[k] = v.decode('utf8')

chartbl.close()

ext_idx = 0x8500
for t in fnt_text.replace('\n', ''):
	ext_idx += 1
	tbl.update({'%02X' % ext_idx : t})

tbl = {v: k for k, v in tbl.iteritems()}
#fix several char mapping
tbl.update({'\n':'0A'})
tbl.update({' ':'20'})
tbl.update({u'\uff0c':'83F7'})
tbl.update({u'\u3000':'84EC'})

#parse script translation blocks
trans_script = trans_script.replace('{84EC}', '　')
regex_blocks = re.findall(r'No\.(\d+?)\n\-{16}\n([\s\S]*?)\n\-{16}', trans_script.decode('utf8'))

trans_blocks = [None]*4107
for b in regex_blocks:
	trans_blocks[int(b[0])-1] = b[1]

def le_unpack(bytes):
	return int(bytes[::-1].encode('hex'), 16)

def le_pack(num):
	lb_str = '%06X' % num
	return lb_str.decode('hex')[::-1]

trans_ptr_bin = ''
trans_raw_script = ''
for block in range(0, 4107):
	org_type = ptr_bin[block*4+3]
	org_ptr =  le_unpack(ptr_bin[block*4:block*4+3])
	nxt_ptr =  le_unpack(ptr_bin[(block+1)*4:(block+1)*4+3]) if block != 4106 else len(raw_script)
	
	trans_ptr_bin += le_pack(len(trans_raw_script)) + org_type

	if trans_blocks[block]:
		for t in trans_blocks[block]:
			trans_raw_script += tbl[t].decode('hex')
		trans_raw_script += '\x00'
	else:
		trans_raw_script += raw_script[org_ptr:nxt_ptr]

	if block == 3885 or block == 3916:
		fill_count = (len(trans_raw_script) + ped) % 4
		trans_raw_script += '\x00' * fill_count

if (len(trans_raw_script) + ped) >= end:
	print 'Game script is out of end!'

fnt_file = open('test.bin', 'wb')
fnt_file.write(trans_ptr_bin + trans_raw_script)
fnt_file.close()