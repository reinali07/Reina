//regular d flip flop

module flippity_flop(input d,clock,resetn,output reg Q);
	always@(posedge clock)
		if (!resetn)
			Q <= 1'b0;
		else
			Q <= d;
endmodule
