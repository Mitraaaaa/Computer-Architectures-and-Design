`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/30/2022 02:55:53 PM
// Design Name: 
// Module Name: ALU
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    01:36:36 04/11/2022 
// Design Name: 
// Module Name:    alu 
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
module alu(A,B,sel,resault
    );
 input [15:0]A;
 input [15:0]B;
 input [3:0]sel;
 output reg [15:0] resault;
 
 always @(*)
 begin
 resault=0;
  case(sel)
  4'b0001:
  begin
   resault=A+B;
  end
  4'b0011:
  begin
   resault=A-B;
  end
  4'b0101:
  begin
   resault=A*B;
  end
  4'b0111:
  begin
   resault=A/B;
  end
  4'b1101:
  begin
   resault=(A<<B);
  end
  4'b1111:
   resault=(A>>B);
  4'b1001:
   resault=(A&B);
  4'b1011:
   resault=(A|B); 
  4'b1010:
   if(A>B) resault=1;
   else resault=0;
  default :
  begin
   resault=A+B;
  end
  endcase
  end
endmodule
