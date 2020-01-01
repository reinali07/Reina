//4 bit synchronous counter with asynchronous reset. Displays count in hex on 7-segment displays. On DE1-SoC board.
//uses verilog built-in addition operation, instead of manually coding a series of flip flops.

module part4(input [1:0]SW, input [1:0] KEY, output [6:0] HEX0,HEX1,HEX2,HEX3);
	reg [15:0] Q = 0;
	wire enable = SW[0];
	wire resetn = KEY[0];
	wire clk = KEY[1];
	
	always@(negedge resetn, posedge clk)
	begin
		if (!resetn)
			Q <= 0;
		else if (enable)
			Q <= Q+1;
	end
	
	hexDisp H1(Q[3:0],HEX0);
	hexDisp H2(Q[7:4],HEX1);
	hexDisp H3(Q[11:8],HEX2);
	hexDisp H4(Q[15:12],HEX3);
	
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