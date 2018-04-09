.gba
.open "./hack/rom/bokutai.gba","./hack/menu/bokutai.gba",0x08000000

// Fix menu confirm dialog OK/Cancel button tile asm

.org 0x0803CD96
sub r3, 3Eh
.org 0x0804575A
sub r3, 3Eh

.org 0x0803CD9E
add r0, 1h
strh r0, [r2, 0h]
strh r1, [r2, 6h]
.org 0x0803CDDE
add r0, 1h
strh r0, [r2, 0h]
strh r1, [r2, 6h]
.org 0x08045762
add r0, 1h
strh r0, [r2, 0h]
strh r1, [r2, 6h]
.org 0x080457A2
add r0, 1h
strh r0, [r2, 0h]
strh r1, [r2, 6h]

.org 0x0803CDAE
add r3, 3h
.org 0x0803CDEE
add r3, 3h
.org 0x08045772
add r3, 3h
.org 0x080457B2
add r3, 3h

.org 0x0803CDB8
strh r0, [r2, 4h]
.org 0x0803CDF8
strh r0, [r2, 4h]
.org 0x0804577C
strh r0, [r2, 4h]
.org 0x080457BC
strh r0, [r2, 4h]

// Fix menu confirm dialog OK/Cancel button tile pointer 

.org 0x0803CE2C
.byte 0x8A
.org 0x080457F0
.byte 0x8A

.org 0x0803CE3C
.byte 0x8A, 0xE8
.org 0x08045800
.byte 0x8A, 0xE8

.org 0x0803CE40
.byte 0x5C
.org 0x08045804
.byte 0x5C

.close