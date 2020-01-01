//Part V
//loops 253 on 3 7-segment displays depending switch 9 and 8. specific switch pattern for switch 5-0 should be set.
module hexLoop(SW,LEDR,HEX0,HEX1,HEX2);
	input [9:0] SW;
	output [9:0] LEDR;
	output [6:0] HEX0;
	output [6:0] HEX1;
	output [6:0] HEX2;

	wire [1:0]M0;
	wire [1:0]M1;
	wire [1:0]M2;
	
	mux3to1_2bit U0 (SW[9:8],SW[5:4],SW[3:2],SW[1:0],M0); //if SW[9] = 0 and SW[8] = 0, takes SW[5:4], set to 0,0 (gives 2). if SW[9] = 1, SW[8] = 0 or 1, takes SW[1:0], set to 1,0 (gives 3). if SW[9] = 0, SW[8] = 1, takes SW[3:2], set to 0,1 (gives 5). 
	hexDisp H0 (M0,HEX2);
	assign LEDR[6:5] = M0;

	mux3to1_2bit U1 (SW[9:8],SW[3:2],SW[1:0],SW[5:4],M1); //if SW[9] = 0 and SW[8] = 0, takes SW[3:2], set to 0,1 (gives 5). if SW[9] = 1, SW[8] = 0 or 1, takes SW[5:4], set to 0,0 (gives 2). if SW[9] = 0, SW[8] = 1, takes SW[1:0], set to 1,0 (gives 3). 
	hexDisp H1 (M1,HEX1);
	assign LEDR[4:3] = M1;

	mux3to1_2bit U2 (SW[9:8],SW[1:0],SW[5:4],SW[3:2],M2); //if SW[9] = 0 and SW[8] = 0, takes SW[1:0], set to 1,0 (gives 3). if SW[9] = 1, SW[8] = 0 or 1, takes SW[3:2], set to 0,1 (gives 5). if SW[9] = 0, SW[8] = 1, takes SW[5:4], set to 0,0 (gives 2). 
	hexDisp H2 (M2,HEX0);
	assign LEDR[1:0] = M2;
	
	assign LEDR[9:8] = SW[9:8];
endmodule
