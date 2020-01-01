//main module
//displays morse code for letters J-Q on led. 0.5 second pulse for dots. 1.5 second pulses for dashes. asynchronous reset on KEY[0]. On DE1-SoC board.

module blinky_thing(input [2:0]SW,input [1:0] KEY,input CLOCK_50, output [0:0]LEDR);

	//make the slower counter
	wire clock2;
	county_thing C1(CLOCK_50,clock2);
	
	//get the dot dash sequence
	wire start = KEY[1];
	wire resetn = KEY[0];
	
	wire [2:0]letter = SW[2:0]; //which letter
	wire [13:0]sequence;

	beepy_thing B1(letter,start,resetn,sequence);
	
	//shift register
	wire [13:0]light;
	shifty_thing S2(sequence,start,clock2,resetn,light); //shift bits of sequence w/ time
	assign LEDR[0] = light[13]; //display the 10th bit (since shifting left)
endmodule