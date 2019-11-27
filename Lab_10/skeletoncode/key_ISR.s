/***************************************************************************************
 * Pushbutton - Interrupt Service Routine                                
 *                                                                          
 * This routine checks which KEY has been pressed.  If KEY3 it stops/starts the timer.
****************************************************************************************/
					.global	KEY_ISR
KEY_ISR: 		LDR		R0, =0xFF200050			// base address of KEYs parallel port
				LDR		R1, [R0, #0xC]			// read edge capture register
				STR		R1, [R0, #0xC]			// clear the interrupt

CHK_KEY3:		MOV R3,#0b1000
				AND R3,R3,R1
				CMP R3,#0b1000
                
UNEXPECTED_KEY:	BNE UNEXPECTED_KEY

START_STOP:		LDR		R0, =0xFFFEC600		// timer base address
				LDR		R1, [R0, #0x8]			// read timer control register
				MOV 	R3,#1
				EOR 	R1,R1,R3
				STR 	R1, [R0, #0x8] //TOGGLE TIMER ENABLE

END_KEY_ISR:	MOV	PC, LR
					.end
	
