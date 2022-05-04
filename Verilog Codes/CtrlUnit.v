`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    15:22:38 05/01/2022 
// Design Name: 
// Module Name:    CtrlUnit 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module CtrlUnit(input [3:0] OpCode, output reg bra, output reg branch, 
							output reg regWrite, output reg regDes, output reg aluSrc, output reg memR,
							output reg memW, output reg MemToReg, output reg notStri
    );
		 reg Op1, Op2, Op3, Op4;
		 reg load;
		 reg store; 
		 reg stri;
		 reg boz;
		 reg bran;
		 reg comp;
		 
	always @(*)
		begin
		 {Op4, Op3, Op2, Op1} = OpCode;
		 
		 load = ~Op1 && ~Op2 && ~Op3 && ~Op4;
		 store = ~Op1 && Op2 && ~Op3 && ~Op4; 
		 stri = ~Op1 && ~Op2 && Op3 && ~Op4;
		 boz = ~Op1 && Op2 && Op3 && ~Op4;
		 bran = ~Op1 && ~Op2 && ~Op3 && Op4;
		 comp = ~Op1 && Op2 && ~Op3 && Op4;	 
	 
		 bra = bran;
		 branch = boz || bran;
		 regWrite = load || stri || comp || Op1;
		 regDes = ~load && ~store && ~stri;
		 aluSrc = load || store || stri;
		 memW = store;
		 memR = load;
		 MemToReg = load;
		 notStri = ~stri;
		end 
		
endmodule
