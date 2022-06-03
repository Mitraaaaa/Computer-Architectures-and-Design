try:
    inp = open('/in.txt', 'r')
    data = inp.readlines()
except Exception as error:
    print(error)

for instruction in data:
    ins = list(instruction.split())
    opCode = ""
    if(ins[0] == 'ld'):
        opCode = '0000'
    elif(ins[0] == 'add'):
        opCode = '0001'
    elif(ins[0] == 'st'):
        opCode = '0010'
    elif(ins[0] == 'sub'):
        opCode = '0011'
    elif(ins[0] == 'sti'):
        opCode = '0100'
    elif(ins[0] == 'mul'):
        opCode = '0101'
    elif(ins[0] == 'boz'):
        opCode = '0110'
    elif(ins[0] == 'div'):
        opCode = '0111'
    elif(ins[0] == 'baw'):
        opCode = '1000 0000'
    elif(ins[0] == 'and'):
        opCode = '1001'
    elif(ins[0] == 'cmp'):
        opCode = '1010'
    elif(ins[0] == 'or'):
        opCode = '1011'
    elif(ins[0] == 'ls'):
        opCode = '1101'
    elif(ins[0] == 'rs'):
        opCode = '1111'

    print(opCode)
