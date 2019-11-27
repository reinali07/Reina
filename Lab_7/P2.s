.include    "address_map_arm.s"

.text                       
.global     _start          
_start: 
		LDR		R1, =TEST_NUM
        LDR     R1, =LED_BASE  /* Address of red LEDs. */
        LDR     R2, =SW_BASE    /* Address of switches. */
LOOP:   
        LDR     R3, [R2]        /* Read the state of switches. */
        STR     R3, [R1]        /* Display the state on LEDs. */
        B       LOOP            
.end                        
TEST_NUM: .word 1,2,3,6,0xA,-1

		.end
