	.text
	.global _start
_start:
	LDR R3,=TEST_NUM
	MOV R5,#0
LOOP:
	LDR R1,[R3],#4
	CMP R1,#-1
	BEQ END
	MOV R0,#0
	BL	ONES
	CMP R0,R5
	MOVGT R5,R0
	B	LOOP
END: B END

ONES:
	CMP R1,#0
	BEQ END_ONES
	LSR R2,R1,#1
	AND R1,R1,R2
	ADD R0,R0,#1
	B	ONES
END_ONES:	MOV PC,LR

TEST_NUM:
	.word 0x00000100
	.word 0xff00bc01
	.word 0x00000111
	.word 0x00000fff
	.word 0x01ff000f
	.word 0x010bc0f0
	.word 0xfffff011
	.word 0x010b0ace
	.word 0x10100edf
	.word 0x0dfe0bca
	.word -1

	.end