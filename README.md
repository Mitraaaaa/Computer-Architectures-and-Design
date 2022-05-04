# Computer Architectures and Design Project  
## ISA  
| Instruction | Usage | Binary | Description |
| --- | --- | --- | --- |
| Load           | ld  $Rs, $Rt, immad | 0000 ---- ---- ---- | $Rt = MEM[$Rs + ZeroExt(immad)*2]|  
| Add            | add $Rd, $Rs, $Rt   | 0001 ---- ---- ---- | $Rd = $Rs + $Rt |  
| Store          | st  $Rs, $Rt, immad | 0010 ---- ---- ---- | MEM[$Rs + ZeroExt(immad)*2] = $Rt |  
| Subtract       | sub $Rd, $Rs, $Rt   | 0011 ---- ---- ---- | $Rd = $Rs - $Rt |  
| StoreImmidiate | sti $Rt, imm        | 0100 ---- --------  | $Rt = imm |  
| multiply       | mul $Rd, $Rs, $Rt   | 0101 ---- ---- ---- | $Rd = $Rs * $Rt |  
| BranchOnZero   | boz $Rs, immad      | 0110 ---- --------- | ($Rs == 0)? PC = address |  
| divide         | dev $Rd, $Rs, $Rt   | 0111 ---- ---- ---- | $Rd = $Rs / $Rt |  
| BranchAnyway   | baw immad           | 1000 0000 --------  | PC = address |  
| LogicalAnd     | and $Rd, $Rs, $Rt   | 1001 ---- ---- ---- | $Rd = $Rs and $Rt |
| comparator     | cmp $Rd, $Rs, $Rt   | 1010 ---- ---- ---- | $Rd = ($Rs > $Rt)? 1:0 |  
| LogicalOr      | or  $Rd, $Rs, $Rt   | 1011 ---- ---- ---- | $Rd = $Rs or $Rt |  
| LeftShift      | lf  $Rd, $Rs, $Rt   | 1101 ---- ---- ---- | $Rd = $Rs << $Rt |  
| RightShift     | rs  $Rd, $Rs, $Rt   | 1111 ---- ---- ---- | $Rd = $Rs >> $Rt |  
  
![main](CPU.png)

#### Alireza Karimi: 993623035  
#### Alireza Dastmalchi Saei : 993613026
#### Mitra Omrani: 993613047  
