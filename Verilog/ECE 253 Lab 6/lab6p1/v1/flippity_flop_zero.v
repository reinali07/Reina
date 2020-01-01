module flippity_flop_zero(input clock,resetn,output reg Q);
	initial Q = 1'b1;
	always@(posedge clock)
		Q <= ~resetn;
endmodule