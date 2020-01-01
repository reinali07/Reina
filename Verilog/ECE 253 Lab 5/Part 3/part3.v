//4 bit synchronous counter with asynchronous reset using toggle flip flops. Displays count in hex on 7-segment displays. On DE1-SoC board.

module T_FF(input T, clk, Resetn, output reg Q);
	wire D = T^Q;
	always @(negedge Resetn, posedge clk)
	begin
		if (!Resetn)
			Q <= 1'b0;
		else
			Q <= D;
	end
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

module c_ount(input enable, clk, Resetn, output [15:0]Q);
	
	T_FF T1(enable, clk, Resetn, Q[0]);
	T_FF T2(enable&Q[0], clk, Resetn, Q[1]);
	T_FF T3(enable&Q[0]&Q[1], clk, Resetn, Q[2]);
	T_FF T4(enable&Q[0]&Q[1]&Q[2], clk, Resetn, Q[3]);
	T_FF T5(enable&Q[0]&Q[1]&Q[2]&Q[3], clk, Resetn, Q[4]);
	T_FF T6(enable&Q[0]&Q[1]&Q[2]&Q[3]&Q[4], clk, Resetn, Q[5]);
	T_FF T7(enable&Q[0]&Q[1]&Q[2]&Q[3]&Q[4]&Q[5], clk, Resetn, Q[6]);
	T_FF T8(enable&Q[0]&Q[1]&Q[2]&Q[3]&Q[4]&Q[5]&Q[6], clk, Resetn, Q[7]);
	T_FF T9(enable&Q[0]&Q[1]&Q[2]&Q[3]&Q[4]&Q[5]&Q[6]&Q[7], clk, Resetn, Q[8]);
	T_FF T10(enable&Q[0]&Q[1]&Q[2]&Q[3]&Q[4]&Q[5]&Q[6]&Q[7]&Q[8], clk, Resetn, Q[9]);
	T_FF T11(enable&Q[0]&Q[1]&Q[2]&Q[3]&Q[4]&Q[5]&Q[6]&Q[7]&Q[8]&Q[9], clk, Resetn, Q[10]);
	T_FF T12(enable&Q[0]&Q[1]&Q[2]&Q[3]&Q[4]&Q[5]&Q[6]&Q[7]&Q[8]&Q[9]&Q[10], clk, Resetn, Q[11]);
	T_FF T13(enable&Q[0]&Q[1]&Q[2]&Q[3]&Q[4]&Q[5]&Q[6]&Q[7]&Q[8]&Q[9]&Q[10]&Q[11], clk, Resetn, Q[12]);
	T_FF T14(enable&Q[0]&Q[1]&Q[2]&Q[3]&Q[4]&Q[5]&Q[6]&Q[7]&Q[8]&Q[9]&Q[10]&Q[11]&Q[12], clk, Resetn, Q[13]);
	T_FF T15(enable&Q[0]&Q[1]&Q[2]&Q[3]&Q[4]&Q[5]&Q[6]&Q[7]&Q[8]&Q[9]&Q[10]&Q[11]&Q[12]&Q[13], clk, Resetn, Q[14]);
	T_FF T16(enable&Q[0]&Q[1]&Q[2]&Q[3]&Q[4]&Q[5]&Q[6]&Q[7]&Q[8]&Q[9]&Q[10]&Q[11]&Q[12]&Q[13]&Q[14], clk, Resetn, Q[15]);
	
endmodule

module part3(input [1:0]SW, KEY, output [6:0] HEX0,HEX1,HEX2,HEX3);
	wire [15:0]q;
	
	c_ount C1(SW[0], KEY[1], KEY[0], q);
	hexDisp H1(q[3:0],HEX0);
	hexDisp H2(q[7:4],HEX1);
	hexDisp H3(q[11:8],HEX2);
	hexDisp H4(q[15:12],HEX3);
endmodule
	