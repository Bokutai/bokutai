# coding: utf8

'''
Convert general GBA battery save to No$gba raw battery save 

todo: 
	1.reverse convert
	2.command arguments
'''

sav = open('boku.sav', 'r')
savbin = sav.read()
sav.close()

for i in range(len(savbin)/8):
	s=i*8
	e=s+8
	savbin = savbin[:s] + savbin[s:e][::-1] + savbin[e:]

# Fill FFh extend to 128KB size 
savbin += '\xFF'*(120*1024)


nsav = open('bokutai.SAV', 'w+')
nsav.write(savbin)
nsav.close()