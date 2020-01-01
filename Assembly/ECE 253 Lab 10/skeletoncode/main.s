//this is the main program file
//sweeping lights inwards then outwards (i.e. 1000000001 then 0100000010, etc. then 0000110000 then 0001001000, etc. repeating) using interrupt IO. DE1-SoC board with ARMv7

	.include "address_map_arm.s"
/* 
 * This program demonstrates the use of interrupts using the KEY and timer ports. It
 * 	1. displays a sweeping red light on LEDR, which moves left and right
 * 	2. stops/starts the sweeping motion if KEY3 is pressed
 * Both the timer and KEYs are handled via interrupts
*/

/*
REGISTERS USED IN SVC:
R0: HOLD ADDRESSES/MODE BITS FOR CONFIG
R1: 
R2:
R3:
R4: LED PATTERN
R5: 
R6: LED ADDRESS
*/
			.text
			.global	_start
_start:
			MOV R0,#0B10010
			MSR CPSR,R0 //CHANGE TO IRQ MODE 
			LDR SP,=0x20000 //IRQ STACK POINTER
			MOV R0,#0B10011
			MSR CPSR, R0 //CHANGE TO SVC MODE
			LDR SP,=0X3FFFFFFC

			BL			CONFIG_GIC				// configure the ARM generic interrupt controller
			BL			CONFIG_PRIV_TIMER		// configure the MPCore private timer
			BL			CONFIG_KEYS				// configure the pushbutton KEYs
			
			//enable ARM processor interrupts
			MOV R0,#0xffffffbf
			AND CPSR,CPSR,R0

			LDR		R6, =0xFF200000 		// red LED base address
MAIN:
			LDR		R4, LEDR_PATTERN		// LEDR pattern; modified by timer ISR
			STR 		R4, [R6] 				// write to red LEDs
			B 			MAIN

/* Configure the MPCore private timer to create interrupts every 0.25 seconds */
CONFIG PRIV TIMER:
			LDR		R0, =0xFFFEC600 		// Timer base address
			MOV		R1, #50000000
			STR 	R1,[R0]		//LOAD 50000000 FOR 0.25s
			MOV 	R1, #111
			STR 	R1,[R0],#8 //INTERRUPT, AUTOLOAD, ENABLE FOR TIMER

			MOV 		PC, LR 					// return

/* Configure the KEYS to generate an interrupt */
CONFIG KEYS:
			LDR 		R0, =0xFF200050 		// KEYs base address
			MOV 		R1, #0b1000
			STR 		R1,[R0],#8 //ENABLE INTERRUPTS FOR KEY3
			MOV 		PC, LR 					// return

			.global	LEDR_DIRECTION
LEDR_DIRECTION:
			.word 	0							// 0 means means moving to centre; 1 means moving to outside

			.global	LEDR_PATTERN
LEDR_PATTERN:
			.word 	0x201	// 1000000001
