//counts longest string of consecutive 1s, longest string of leading 0s, longest string of trailing 0s in a list of numbers. ARMv7

	.text
	.global _start
_start:
	LDR R4,=TEST_NUM
    MOV R0,#32
	MOV R8,#0
	MOV R9,#0
	MOV R10,#0
LOOP:
	LDR R1,[R4]
	CMP R1,#-1
	BEQ END
	
	//ONES
	MOV R3,#0
	BL	ONES
	MOV R5,R3
	CMP R8,R5
	MOVLT R8,R5
	
	//LEADING
    LDR R1,[R4]
	MOV R3,#0
	BL LEADING
	MOV R6,R3
	CMP R9,R6
	MOVLT R9,R6
	
	//TRAILING
    LDR R1,[R4]
	MOV R3,#0
	BL TRAILING
	MOV R7,R3
	CMP R10,R7
	MOVLT R10,R7
	
    //INCREMENT
    ADD R4,#4
	B	LOOP
END: B END

ONES:
	CMP R1,#0
	BEQ END_ONES
    ANDS R2,R1,#1
    ADDNE R3,R3,#1
	LSR R1,R1,#1
	B	ONES
END_ONES:	MOV PC,LR

LEADING:
	CMP R1,#0
	BEQ END_LEADING
	LSR R1,R1,#1
	ADD R3,#1
	B LEADING
END_LEADING:
	SUB R3,R0,R3
	MOV PC,LR

TRAILING:
	CMP R1,#0
	BEQ END_TRAILING
	LSL R1,R1,#1
	ADD R3,#1
	B TRAILING
END_TRAILING:
	SUB R3,R0,R3
	MOV PC,LR

TEST_NUM:
	.word 0x7fffffff
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