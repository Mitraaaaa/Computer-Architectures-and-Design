`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   
// Design Name:   alu
// Module Name:   
// Project Name:  ALU
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: alu
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module ALU_tst;

	// Inputs
	reg [15:0] A;
	reg [15:0] B;
	reg [3:0] sel;

	// Outputs
	wire [15:0] resault;

	// Instantiate the Unit Under Test (UUT)
	alu uut (
		.A(A), 
		.B(B), 
		.sel(sel), 
		.resault(resault)
	);

	initial begin
		// Initialize Inputs
		A = 10;
		B = 3;
		sel = 1;
		#100;
		sel = 3;
		#100;
		sel = 5;
		#100;
		sel = 7;
		#100;
		sel = 9;
		#100;
		sel = 10;
		#100;
		sel = 11;
		#100;
		sel = 13;
		#100;
		sel = 15;
		#100;
		$finish;
        

	end
      
endmodule

