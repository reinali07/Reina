//four consecutive 1s or four consecutive 0s (input using high-low from switch and pressing key to store input) gives a output of 1 on LEDR[9]. Uses one-hot state encoding. On DE1-SoC board

module onboard_fsm(input [1:0]SW,input [0:0] KEY,output [9:0]LEDR);
	wire resetn = SW[0];
	wire w = SW[1];
	wire clock = KEY[0];
	wire z;
	wire [8:0]now;
	
	wire [8:0]next = {(now[7]^now[8])&w,now[6]&w,now[5]&w,(now[0]^now[1]^now[2]^now[3]^now[4])&w,(now[3]^now[4])&(~w),now[2]&~w,now[1]&~w,(now[0]^now[5]^now[6]^now[7]^now[8])&~w,1'b0};

	flippity_flop_zero F0(clock,resetn,now[0]);
	flippity_flop F1(next[1],clock,resetn,now[1]);
	flippity_flop F2(next[2],clock,resetn,now[2]);
	flippity_flop F3(next[3],clock,resetn,now[3]);
	flippity_flop F4(next[4],clock,resetn,now[4]);
	flippity_flop F5(next[5],clock,resetn,now[5]);
	flippity_flop F6(next[6],clock,resetn,now[6]);
	flippity_flop F7(next[7],clock,resetn,now[7]);
	flippity_flop F9(next[8],clock,resetn,now[8]);

	assign LEDR[8:0] = now[8:0];

	assign z = now[4]|now[8];
	assign LEDR[9] = z;
endmodule
