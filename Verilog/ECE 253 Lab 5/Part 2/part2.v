//binary value on switches 7-0 is taken and stored to A when key 1 is pressed. A's hex value displayed on 7-segment displays 3 and 2. Then, another binary value can be set on the switches, which we call B. Its hex value displayed on 7-segment displays 1 and 0. A and B are added and their sum in hex is displayed on 7-segment displays 5 and 4. Carry out is displayed on LEDR[0]. On DE1-SoC board.

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

module FA(input ci,a,b,output co,s);
	wire muxs = a^b;
	assign s = ci^muxs;
	assign co = (~muxs&b)|(muxs&ci);
endmodule

module FA4(input ci, input [3:0]X,Y,output co,output [3:0]S);
	wire c1,c2,c3;
	
	FA U1(ci,X[0],Y[0],c1,S[0]);
	FA U2(c1,X[1],Y[1],c2,S[1]);
	FA U3(c2,X[2],Y[2],c3,S[2]);
	FA U4(c3,X[3],Y[3],co,S[3]);
endmodule

module digitAdder(input ci, input [7:0]X,Y,output co, output [7:0]S);
	wire [3:0] X1 = X[3:0];
	wire [3:0] X2 = X[7:4];
	wire [3:0] Y1 = Y[3:0];
	wire [3:0] Y2 = Y[7:4];
	
	wire c1;
	
	FA4 U1(1'b0,X1,Y1,c1,S[3:0]);
	FA4 U2(c1,X2,Y2,co,S[7:4]);
endmodule

module asyncFF(input [7:0]D,input clk,Resetn,output reg [7:0]Q);
	always @(negedge Resetn, posedge clk)
	begin
		if (Resetn==0)
			Q <= 8'b0;
		else
			Q <= D;
	end
endmodule

module part2(input [7:0] SW, input [1:0]KEY, output [6:0] HEX0,HEX1,HEX2,HEX3,HEX4,HEX5, output [1:0] LEDR);
	wire [7:0]A;
	wire [7:0]B = SW;
	wire [8:0]sum;
	
	asyncFF F1(SW,KEY[1],KEY[0],A);
	
	hexDisp H1(A[3:0],HEX2);
	hexDisp H2(A[7:4],HEX3);
	hexDisp H3(B[3:0],HEX0);
	hexDisp H4(B[7:4],HEX1);
	
	digitAdder D1(1'b0,A,B,sum[8],sum[7:0]);
	
	hexDisp H5(sum[3:0],HEX4);
	hexDisp H6(sum[7:4],HEX5);
	assign LEDR[0] = sum[8];
endmodule