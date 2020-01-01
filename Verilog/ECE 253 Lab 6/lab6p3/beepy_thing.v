module beepy_thing(input [2:0]letter,input ln, resetn,output reg [13:0]order);
	parameter J=3'b000, K=3'b001, L=3'b010, M=3'b011, N=3'b100, O=3'b101, P=3'b110, Q=3'b111;
	initial order = 14'b0;
	//1 is light on, 0 is light off
	always@(negedge resetn, negedge ln)
		if (!resetn)
			order <= 14'b0; //turn it off
		else
			case(letter)
				J: order <= 14'b01011101110111; //sequences for light on/off
				K: order <= 14'b01110101110000;
				L: order <= 14'b01011101010000;
				M: order <= 14'b01110111000000;
				N: order <= 14'b01110100000000;
				O: order <= 14'b01110111011100;
				P: order <= 14'b01011101110100;
				Q: order <= 14'b01110111010111;
				default: order <= 14'b0;
			endcase
endmodule