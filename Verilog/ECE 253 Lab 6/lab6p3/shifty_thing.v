module shifty_thing(input [13:0]sequence,input ln, clock,resetn,output reg [13:0]Q);
	initial Q = 14'b0;
	always@(negedge resetn,negedge ln,posedge clock)
		if(!ln)
			Q<=sequence;
		else if (!resetn)
			Q<=14'b0;
		else begin //shift all bits over every half second
			Q[13]<=Q[12];
			Q[12]<=Q[11];
			Q[11]<=Q[10];
			Q[10]<=Q[9];
			Q[9]<=Q[8];
			Q[8]<=Q[7];
			Q[7]<=Q[6];
			Q[6]<=Q[5];
			Q[5]<=Q[4];
			Q[4]<=Q[3];
			Q[3]<=Q[2];
			Q[2]<=Q[1];
			Q[1]<=Q[0];
			Q[0]<=1'b0;
		end
endmodule