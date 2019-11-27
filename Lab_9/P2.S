//load 50 000 000 into timer (0x02FAF080)
//patterns: 2000000003, 0200000030, 0020000300, 0002003000, 0000230000, 0003002000, 0030000200, 0300000020, 3000000002, 0200000030
//POLL KEY3 INSIDE DELAY LOOP

//registers used:
//r0 used to store into leds
//r1 used to load and store vals from/into input devices
//r2 one of the bits /PATTERN
//r3 the other bit /INCREMENT
//r4 keys address
//r5 timer address
//r6 leds address

	.text
	.global _start
_start:
	LDR SP, =0x3ffffffc
	LDR R4, =0xFF200050 //KEYS
	LDR R5, =0xFFfec600 //TIMER
	LDR R6, =0xFF200000 //LEDS
	LDR R1, =0x2FAF080 //for 0.25s
	STR R1,[R5] //load timer
	MOV R1, #0b11
	STR R1,[R5,#8] //set autoload = 1, e = 1

	LDR R2, =LIST
	PUSH {R2}
	MOV R3,#0

DISPLAY:
	CMP R3,#8
	POPEQ {R2}
	PUSHEQ {R2}
	MOVEQ R3,#0
	LDR R0,[R2],#4
	STR R0,[R6]
	ADD R3,R3,#1

	//delay
DELAY:
	BL CHECK_KEY3_FIRST //POLL KEY3
    LDR R1, [R5,#0xC] //READ F
	CMP R1, #0
	BEQ DELAY
	STR R1, [R5,#0xC] //RESET TIMER
	B DISPLAY

CHECK_KEY3_FIRST: //CHECK IF PRESSED FIRST TIME
	PUSH {R1,LR}
	LDR R1,[R4]
	AND R1,R1,#8 //MASK IN CASE OTHER KEYS PRESSED TOO
	CMP R1,#8
    BLEQ CHECK_KEYUP
    CMP R1,#8
	BLEQ CHECK_KEY3_2ND //POLL KEY3 AGAIN
	POP {R1,PC}
    
CHECK_KEYUP: //check if let go
	PUSH {R1,LR}
KEYUP_LOOP:
	LDR R1,[R4]
	AND R1,R1,#8 //MASK IN CASE OTHER KEYS PRESSED TOO
	CMP R1,#0
    BNE KEYUP_LOOP
    POP {R1,PC}

CHECK_KEY3_2ND: //CHECK IF PRESSED AGAIN
	PUSH {LR}
SECOND_LOOP:
	LDR R1,[R4]
	AND R1,R1,#8 //MASK
	CMP R1,#8
	BNE SECOND_LOOP
    BL CHECK_KEYUP
	POP {PC}

LIST: .word 0x201, 0x102, 0x84, 0x48, 0x30, 0x48, 0x84, 0x102
