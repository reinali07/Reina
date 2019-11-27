/*pseudo code for part 1

bubble_sort:
	R4 = LIST
	R5 = R4[0] //NUMBER OF ELEMENTS IN LIST
	R4 = R4[1]
	R0 = 1
	while R0 == 1: //if the previous run, something was swapped
		R0 = 0
		for i = 0 to R5: //not including the last element
			SWAP R4[i] and R4[i+1] //swap if needed
		end for
	end while
end

SWAP:
	if R4[i] > R4[i+1]:
		swap these
		R0 = 1
	end if
end
*/

//registers used:
//r0 is swapped and address
//r1 is increment
//r2 is current word
//r3 is next word
//r4 is list
//r5 is list length

	.text
	.global _start
_start:
	LDR SP,=0X3FFFFFFC
	LDR R4,=LIST //LOAD LIST INTO R4
	LDR R5, [R4], #4 //R5 IS NUMBER OF ELEMENTS, R4 IS THE LIST WE CARE ABOUT
	SUB R5,R5,#1 //NOT INCLUDING LAST ELEMENT
	MOV R0,#1 //SWAPPED

BUBBLE_SORT:
	CMP R0,#1
	BNE END  //IF NOTHING WAS SWAPPED, END
	
	PUSH {R4} //SAVE THE ORIGINAL ADDRESS 
	MOV R0,#0 //SET SWAPPED = 0
	MOV R1,#0
FOR_LOOP:
	CMP R1,R5 //INCREMENT FROM 0 TO R5 (EVERY ELEMENT BUT LAST ONE)
	BEQ ENDLOOP
	BL SWAP
	ADD R1,#1 //INCREMENT R1
	ADD R4,#4 //MOVE TO NEXT WORD
	B FOR_LOOP
ENDLOOP:
	POP {R4}
	B BUBBLE_SORT
	
END: B END
	
SWAP:
	PUSH {R0} //save swapped
	MOV R0,R4 //R0 HOLDS ADDRESS OF CURRENT WORD
	LDR R2,[R0] //R2 IS CURRENT WORD
	LDR R3,[R0,#4] //R3 IS NEXT WORD
	CMP R2,R3 //IF R2 > R3
	STRGT R2,[R0,#4]
	STRGT R3,[R0]
	POP {R0} //restore swapped
	MOVGT R0,#1 //if swapped, SWAPPED = 1
	MOV PC,LR

LIST: .word 10, 1400, 45, 23, 5, 3, 8, 17, 4, 20, 33