//automatic 4 bit synchronous counter with asynchronous reset. About 1 second delay. Displays count in hex on 7-segment display. On DE1-SoC board.

module part5(input CLOCK_50,output [6:0]HEX0);
	reg [3:0] q;
	wire [26:0] countsecs;
	reg enable;
	
	s_econds S1(CLOCK_50,countsecs);
	
	always@(countsecs)
		if (countsecs==27'h2FAF080)
			enable <= 1'b1;
		else
			enable <= 1'b0;
	
	always@(posedge CLOCK_50)
		if (enable)
			if (q>=4'b1001)
				q <= 4'b0;
			else
				q <= q+1'b1;
	hexDisp H1(q,HEX0);
endmodule
	
module s_econds(input clk,output reg [27:0]c_ounter);
	always@(posedge clk)
		if (c_ounter == 27'h2FAF080)
			c_ounter <= 27'b0;
		else
			c_ounter <= c_ounter + 1'b1;
endmodule

module hexDisp(input [3:0]S,output reg [6:0]H);
	always @(S)
	begin
		case (S)
			4'b0000: H= 7'b1000000; //0
			4'b0001: H= 7'b1111001; //1
			4'b0010: H= 7'b0100100; //2
			4'b0011: H= 7'b0110000; //3
			4'b0100: H= 7'b0011001; //4
			4'b0101: H= 7'b0010010; //5
			4'b0110: H= 7'b0000010; //6
			4'b0111: H= 7'b1111000; //7
			4'b1000: H= 7'b0000000; //8
			4'b1001: H= 7'b0011000; //9
			4'b1010: H= 7'b0001000; //A
			4'b1011: H= 7'b0000011; //b
			4'b1100: H= 7'b1000110; //C
			4'b1101: H= 7'b0100001; //D
			4'b1110: H= 7'b0000110; //E
			4'b1111: H= 7'b0001110; //F
		endcase
	end
endmodule