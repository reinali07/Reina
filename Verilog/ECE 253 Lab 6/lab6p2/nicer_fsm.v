//four consecutive 1s or four consecutive 0s (input using high-low from switch and pressing key to store input) gives a output of 1 on LEDR[9]. Uses minimum bits state encodings and verilog case statement. On DE1-SoC board.


module nicer_fsm(input [1:0]SW,input [0:0]KEY,output [9:0]LEDR);
	wire resetn = SW[0];
	wire w = SW[1];
	wire clock = KEY[0];
	wire z;

	//states
	reg [3:0]now,next;
	parameter A=4'h0, B=4'h1, C=4'h2, D=4'h3, E=4'h4, F=4'h5, G=4'h6, H=4'h7, I=4'h8;
	
	//state table
	always@(w,now)
		case(now)
		A: if(!w) next=B;
			else next=F;
		B: if(!w) next=C;
			else next=F;
		C: if(!w) next=D;
			else next=F;
		D: if(!w) next=E;
			else next=F;
		E: if(!w) next=E;
			else next=F;
		F: if(!w) next=B;
			else next=G;
		G: if(!w) next=B;
			else next=H;
		H: if(!w) next=B;
			else next=I;
		I: if(!w) next=B;
			else next=I;
		//default case: latch
		endcase

	//state FFs (1 for each bit technically, so 4)
	always@(posedge clock)
		if (!resetn)
			now<=A;
		else
			now<=next;

	assign z = (now==I)|(now==E);
	assign LEDR[9] = z;
	assign LEDR[3:0] = now;
endmodule
