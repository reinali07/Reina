				.include "address_map_arm.s"
				.extern	LEDR_DIRECTION
				.extern	LEDR_PATTERN

/*****************************************************************************
 * MPCORE Private Timer - Interrupt Service Routine                                
 *                                                                          
 * Shifts the pattern being displayed on the LEDR
 * 
******************************************************************************/
				.global PRIV_TIMER_ISR
PRIV_TIMER_ISR:	PUSH	{R4,R5}
				LDR		R0, =MPCORE_PRIV_TIMER	// base address of timer
				MOV		R1, #1
				STR		R1, [R0, #0xC]				// write 1 to F bit to reset it
															// and clear the interrupt

/* Move the two LEDS to the centre or away from the centre to the outside. */
SWEEP:			LDR		R0, =LEDR_DIRECTION	// put shifting direction into R2
				LDR		R2, [R0]
				LDR		R1, =LEDR_PATTERN		// put LEDR pattern into R3
				LDR		R3, [R1]

				MOV R4,#1111100000
				MOV R5,#0000011111
				AND R4,R4,R3 //UPPER BIT
				AND R5,R5,R3 //LOWER BIT

				CMP R2,#1 //MOVING OUT
				BEQ TOOUTSIDE
				
TOCENTRE:		
				CMP R3,#48
				BEQ C_O //IF AT CENTRE, SWITCH DIRECTION
				LSR R4,R4,#1 //SHIFT BITS TOWARDS CENTRE
				LSL R5,R5,#1
				ADD R3,R4,R5 //ADD LOWER AND UPPER BIT
				B 	DONE_SWEEP
				
C_O:			MOV		R2, #1					// change direction to outside
TOOUTSIDE:		
				CMP R3,#513
				BEQ O_C //IF AT OUTSIDE, SWITCH DIRECTION
				LSL R4,R4,#1 //SHIFT BITS AWAY FROM CENTRE
				LSR R5,R5,#1
				ADD R3,R4,R5 //ADD LOWER AND UPPER BIT
				B 	DONE_SWEEP
				
O_C:			MOV		R2, #0					// change direction to centre
				B			TOCENTRE

DONE_SWEEP:
				STR		R2, [R0]					// put shifting direction back into memory
				STR		R3, [R1]					// put LEDR pattern back onto stack
	
END_TIMER_ISR:
				POP {R4,R5}
				MOV		PC, LR
