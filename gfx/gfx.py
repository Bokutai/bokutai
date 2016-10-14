# coding: utf8

'''
To slice off GFX content from ROM.

todo: 
	
'''

import sys

if len(sys.argv) < 3:
	print 'Usage: python %s [hex:position] [gfx]' % sys.argv[0]
	exit()

rom = open('../hack/rom/bokutai.gba', 'r')
rom_bin = rom.read()
rom.close()

s,e = sys.argv[1].split(':', 2)
print s,e
s = int(s, 16)
e = int(e, 16)

gfx_bin = rom_bin[s:e]

gfx = open(sys.argv[2], 'wb')
gfx.write(gfx_bin)
gfx.close()