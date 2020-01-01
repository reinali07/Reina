//loops dE1 on 7-segments displays with wrap-around. On DE1-SoC board.

module part6finally(input CLOCK_50,output [6:0]HEX0,HEX1,HEX2,HEX3,HEX4,HEX5);
	reg [2:0] q;
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
			if (q>=3'b101)
				q <= 3'b0;
			else
				q <= q+1'b1;
				
	hex0Disp H1(q,HEX0);
	hex1Disp H2(q,HEX1);
	hex2Disp H3(q,HEX2);
	hex3Disp H4(q,HEX3);
	hex4Disp H5(q,HEX4);
	hex5Disp H6(q,HEX5);
endmodule
	
module hex0Disp(input [2:0]q,output reg [6:0]H);
	parameter a=3'h0, b=3'h4, c=3'h5;
	always@(q)
		case (q)
			a: H = 7'b1111001; //1
			b: H = 7'b0100001; //d
			c: H = 7'b0000110; //E
			default: H = 7'b1111111;
		endcase
endmodule

module hex1Disp(input [2:0]q,output reg [6:0]H);
	parameter a=3'h0, b=3'h1, c=3'h5;
	always@(q)
		case (q)
			a: H = 7'b0000110;
			b: H = 7'b1111001;
			c: H = 7'b0100001;
			default: H = 7'b1111111;
		endcase
endmodule

module hex2Disp(input [2:0]q,output reg [6:0]H);
	parameter a=3'h0, b=3'h1, c=3'h2;
	always@(q)
		case (q)
			a: H = 7'b0100001;
			b: H = 7'b0000110;
			c: H = 7'b1111001;
			default: H = 7'b1111111;
		endcase
endmodule

module hex3Disp(input [2:0]q,output reg [6:0]H);
	parameter a=3'h1, b=3'h2, c=3'h3;
	always@(q)
		case (q)
			a: H = 7'b0100001;
			b: H = 7'b0000110;
			c: H = 7'b1111001;
			default: H = 7'b1111111;
		endcase
endmodule

module hex4Disp(input [2:0]q,output reg [6:0]H);
	parameter a=3'h2, b=3'h3, c=3'h4;
	always@(q)
		case (q)
			a: H = 7'b0100001;
			b: H = 7'b0000110;
			c: H = 7'b1111001;
			default: H = 7'b1111111;
		endcase
endmodule
	
module hex5Disp(input [2:0]q,output reg [6:0]H);
	parameter a=3'h3, b=3'h4, c=3'h5;
	always@(q)
		case (q)
			a: H = 7'b0100001;
			b: H = 7'b0000110;
			c: H = 7'b1111001;
			default: H = 7'b1111111;
		endcase
endmodule
	
	
module s_econds(input clk,output reg [27:0]c_ounter);
	always@(posedge clk)
		if (c_ounter == 27'h2FAF080)
			c_ounter <= 27'b0;
		else
			c_ounter <= c_ounter + 1'b1;
endmodule