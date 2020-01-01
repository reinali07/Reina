module county_thing(input CLOCK_50,output reg clock2);
	wire [23:0] countsecs;
	reg enable;
	
	s_econds S1(CLOCK_50,countsecs);
	initial enable = 24'b0;
	always@(countsecs)
		if (countsecs==24'hBEBC20)
			enable <= 1'b1;
		else
			enable <= 1'b0;
	
	always@(posedge CLOCK_50)
		if (enable)
			clock2 <= ~clock2;
endmodule
	
module s_econds(input clk,output reg [23:0]c_ounter);
	initial c_ounter = 24'b0;
	always@(posedge clk)
		if (c_ounter == 24'hBEBC20)
			c_ounter <= 24'b0;
		else
			c_ounter <= c_ounter + 1'b1;
endmodule