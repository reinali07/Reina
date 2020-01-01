//4 bit 2-to-1 multiplexer in verilog using digital logic on DE1-SoC board
module mux2to1_4bit(input[9:0]SW,output[9:0]LEDR);
	wire [3:0]X = SW[3:0];
	wire [3:0]Y = SW[7:4];
	wire s = SW[9];
	wire [3:0]M;
	assign M = ({~s,~s,~s,~s}&X)|({s,s,s,s}&Y);
	assign LEDR[3:0] = M;
	assign LEDR[8:4] = 5'b0;
	assign LEDR[9] = s;
endmodule
