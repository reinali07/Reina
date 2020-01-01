//verilog code for d latch and d flip flops (posedge clock triggered and negedge clock triggered)

module d_Latch(D, clk, Q);
	input D, clk;
	output reg Q;
	always @(D, clk)
		if (clk == 1)
			Q = D;
endmodule

module posDFF(input D,clk,output reg Q);
	always @(posedge clk)
		Q <= D;
endmodule

module negDFF(input D,clk,output reg Q);
	always @(negedge clk)
		Q <= D;
endmodule

module part1(input D,clk,output[2:0]Q);
	d_Latch U1(D,clk,Q[2]);
	posDFF U2(D,clk,Q[1]);
	negDFF U3(D,clk,Q[0]);
endmodule

