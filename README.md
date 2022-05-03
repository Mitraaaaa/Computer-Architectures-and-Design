# Computer Architectures and Design Project  
## ISA:  
~~~
ld  : Load           : ld  $Rt, $Rs, immad : 0000 ---- ---- ---- : $Rt = MEM[$Rs + ZeroExt(immad)*2]  
add : Add            : add $Rd, $Rs, $Rt   : 0001 ---- ---- ---- : $Rd = $Rs + $Rt  
st  : Store          : st  $Rt, $Rs, immad : 0010 ---- ---- ---- : MEM[$Rs + ZeroExt(immad)*2] = $Rt  
sub : Subtract       : sub $Rd, $Rs, $Rt   : 0011 ---- ---- ---- : $Rd = $Rs - $Rt  
sti : StoreImmidiate : sti $Rt, imm        : 0100 ---- --------  : $Rt = imm  
mul : multiply       : mul $Rd, $Rs, $Rt   : 0101 ---- ---- ---- : $Rd = $Rs * $Rt  
boz : BranchOnZero   : boz $Rs, immad      : 0110 ---- --------- : ($Rs == 0)? PC = address #address = (pc and 1111111000000000) or (ZeroExt(immad)*2)  
div : divide         : dev $Rd, $Rs, $Rt   : 0111 ---- ---- ---- : $Rd = $Rs / $Rt  
baw : BranchAnyway   : baw immad           : 1000 0000 --------  : PC = address             #address = (pc and 1111111000000000) or (ZeroExt(immad)*2)  
and : LogicalAnd     : and $Rd, $Rs, $Rt   : 1001 ---- ---- ---- : $Rd = $Rs and $Rt
cmp : comparator     : cmp $Rd, $Rs, $Rt   : 1010 ---- ---- ---- : $Rd = ($Rs > $Rt)? 1:0  
or  : LogicalOr      : or  $Rd, $Rs, $Rt   : 1011 ---- ---- ---- : $Rd = $Rs or $Rt  
ls  : LeftShift      : lf  $Rd, $Rs, $Rt   : 1101 ---- ---- ---- : $Rd = $Rs << $Rt  
rs  : RightShift     : rs  $Rd, $Rs, $Rt   : 1111 ---- ---- ---- : $Rd = $Rs >> $Rt  
~~~
  
![main](CPU.jpg)

#### Alireza Karimi: 993623035  
#### Alireza Dastmalch Saei : 993613026
#### Mitra Omrani: 993613047  
