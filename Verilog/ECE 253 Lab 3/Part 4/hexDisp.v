//not compiled
//displays a number on DE1-SoC 7-segment display based on 2-bit switch positions (i.e 10 displays 2)
//Part IV

module hexDisp(input [1:0] SW, output [6:0] HEX0);
	wire [1:0]C = SW[1:0];
	assign HEX0[0] = C[0]&C[1];
	assign HEX0[1] = C[0];
	assign HEX0[2] = (C[0]&C[1])|(~C[0]&~C[1]);
	assign HEX0[3] = C[0]&C[1];
	assign HEX0[4] = C[0]|C[1];
	assign HEX0[5] = (~C[0])|C[1];
	assign HEX0[6] = C[0]&C[1];
end module
