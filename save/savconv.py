# coding: utf8

'''
Convert general GBA battery save to No$gba raw battery save 

todo: 
	1.reverse convert
'''

import sys

if len(sys.argv) < 3:
	print 'Usage: python %s [input_save] [output_save]' % sys.argv[0]
	exit()

sav = open(sys.argv[1], 'r')
savbin = sav.read()
sav.close()

for i in range(len(savbin)/8):
	s=i*8
	e=s+8
	savbin = savbin[:s] + savbin[s:e][::-1] + savbin[e:]

# Fill FFh extend to 128KB size 
savbin += '\xFF'*(120*1024)


nsav = open(sys.argv[2], 'wb')
nsav.write(savbin)
nsav.close()