//2 bit 3-to-1 multiplexer in verilog using digital logic on DE1-SoC board

module mux2to1_2bit(s,X,Y,out); //submodule
	input [1:0]X,Y;
	input s;
	output [1:0]out;
	assign out = ({~s,~s}&X)|({s,s}&Y);
endmodule

module mux3to1_2bit(SW,LEDR); //main
	input [9:0]SW;
	output [9:0]LEDR;
	
	wire [1:0]U,V,W,S,M_intermediate,M;
	//assign appropriate board elements to wires
	assign S = SW[9:8];
	assign U = SW[5:4];
	assign V = SW[3:2];
	assign W = SW[1:0];
	assign LEDR[9] = S[1];
	assign LEDR[8] = S[0];
	assign LEDR[7:2] = 6'b0;
	
	mux2to1_2bit U1(S[0],U,V,M_intermediate);
	mux2to1_2bit U2(S[1],M_intermediate,W,M);
	
	assign LEDR[1:0] = M;
endmodule
