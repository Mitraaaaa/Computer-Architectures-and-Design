`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   17:18:35 05/04/2022
// Design Name:   CtrlUnit
// Module Name:   F:/University 4/CA/Project/Ctrl_Unit_Verlog/CtrlUnit/CtrlUnit_tst.v
// Project Name:  CtrlUnit
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: CtrlUnit
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module CtrlUnit_tst;

	// Inputs
	reg [3:0] OpCode;

	// Outputs
	wire bra;
	wire branch;
	wire regWrite;
	wire regDes;
	wire aluSrc;
	wire memR;
	wire memW;
	wire MemToReg;
	wire notStri;

	// Instantiate the Unit Under Test (UUT)
	CtrlUnit uut (
		.OpCode(OpCode), 
		.bra(bra), 
		.branch(branch), 
		.regWrite(regWrite), 
		.regDes(regDes), 
		.aluSrc(aluSrc), 
		.memR(memR), 
		.memW(memW), 
		.MemToReg(MemToReg), 
		.notStri(notStri)
	);

	initial begin
		OpCode = 0;
		#100;
		OpCode = 1;
		#100;
		OpCode = 2;
		#100;
		OpCode = 3;
		#100;
		OpCode = 4;
		#100;
		OpCode = 5;
		#100;
		OpCode = 6;
		#100;
		OpCode = 7;
		#100;
		OpCode = 8;
		#100;
		OpCode = 9;
		#100;
		//It will show up to here due to max ns duration. comment some to see the rest
		OpCode = 10;
		#100;
		OpCode = 11;
		#100;
		OpCode = 13;
		#100;
		OpCode = 15;
		#100;
		$finish;
        

	end
      
endmodule

