import os


def int2hex(opCode, rs, rt, rd, imm):
    if opCode % 2:
        pass
    else:
        pass


def asm2int(asm):
    ins = list(asm.split())
    opCode = 0
    rd = 0
    rs = 0
    rt = 0
    imm = 0

    if(ins[0] == 'ld'):
        opCode = int('0000', base=2)
        rs = int(ins[1], base=2)
        rt = int(ins[2], base=2)
        imm = int(ins[3], base=2)
    elif(ins[0] == 'add'):
        opCode = int('0001', base=2)
        rd = int(ins[1], base=2)
        rs = int(ins[2], base=2)
        rt = int(ins[3], base=2)
    elif(ins[0] == 'st'):
        opCode = int('0010', base=2)
        rs = int(ins[1], base=2)
        rt = int(ins[2], base=2)
        imm = int(ins[3], base=2)
    elif(ins[0] == 'sub'):
        opCode = int('0011', base=2)
        rd = int(ins[1], base=2)
        rs = int(ins[2], base=2)
        rt = int(ins[3], base=2)
    elif(ins[0] == 'sti'):
        opCode = int('0100', base=2)
        rt = int(ins[1], base=2)
        imm = int(ins[2], base=2)
    elif(ins[0] == 'mul'):
        opCode = int('0101', base=2)
        rd = int(ins[1], base=2)
        rs = int(ins[2], base=2)
        rt = int(ins[3], base=2)
    elif(ins[0] == 'boz'):
        opCode = int('0110', base=2)
        rs = int(ins[1], base=2)
        imm = int(ins[2], base=2)
    elif(ins[0] == 'div'):
        opCode = int('0111', base=2)
        rd = int(ins[1], base=2)
        rs = int(ins[2], base=2)
        rt = int(ins[3], base=2)
    elif(ins[0] == 'baw'):
        opCode = int('1000', base=2)
        imm = int(ins[2], base=2)
    elif(ins[0] == 'and'):
        opCode = int('1001', base=2)
        rd = int(ins[1], base=2)
        rs = int(ins[2], base=2)
        rt = int(ins[3], base=2)
    elif(ins[0] == 'cmp'):
        opCode = int('1010', base=2)
        rd = int(ins[1], base=2)
        rs = int(ins[2], base=2)
        rt = int(ins[3], base=2)
    elif(ins[0] == 'or'):
        opCode = int('1011', base=2)
        rd = int(ins[1], base=2)
        rs = int(ins[2], base=2)
        rt = int(ins[3], base=2)
    elif(ins[0] == 'ls'):
        opCode = int('1101', base=2)
        rd = int(ins[1], base=2)
        rs = int(ins[2], base=2)
        rt = int(ins[3], base=2)
    elif(ins[0] == 'rs'):
        opCode = int('1111', base=2)
        rd = int(ins[1], base=2)
        rs = int(ins[2], base=2)
        rt = int(ins[3], base=2)

    return opCode, rs, rt, rd, imm


def decode(asm):
    opcode, rs, rt, rd, imm = asm2int(asm)
    print("OpCOde:", opcode, "rs:", rs, "rt:", rt, "rd:", rd, "imm:", imm)
    instr = int2hex(opcode, rs, rt, rd, imm)
    return instr


def readFromFile(address):
    address = address.replace("\Assembler.py", "\in.txt")
    with open(address, 'r') as file:
        return file.readlines()


def writeToFile(address, info):
    address = address.replace("\Assembler.py", "\out.txt")
    file = open(address, 'w+')
    for line in info:
        file.write(line + "\n")
    file.close()


try:
    script_path = os.path.abspath(__file__)
    data = readFromFile(script_path)
    print("File Read Successfully")

    hexList = []

    for instruction in data:
        hexList.append(decode(instruction))

    # writeToFile(script_path, data)

except IOError as error:
    print(error)
