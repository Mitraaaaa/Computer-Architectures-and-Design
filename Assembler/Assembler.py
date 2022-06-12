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
        rs = int(ins[1])
        rt = int(ins[2])
        imm = int(ins[3])
    elif(ins[0] == 'add'):
        opCode = 1
        rd = int(ins[1])
        rs = int(ins[2])
        rt = int(ins[3])
    elif(ins[0] == 'st'):
        opCode = 2
        rs = int(ins[1])
        rt = int(ins[2])
        imm = int(ins[3])
    elif(ins[0] == 'sub'):
        opCode = 3
        rd = int(ins[1])
        rs = int(ins[2])
        rt = int(ins[3])
    elif(ins[0] == 'sti'):
        opCode = 4
        rt = int(ins[1])
        imm = int(ins[2])
    elif(ins[0] == 'mul'):
        opCode = 5
        rd = int(ins[1])
        rs = int(ins[2])
        rt = int(ins[3])
    elif(ins[0] == 'boz'):
        opCode = 6
        rs = int(ins[1])
        imm = int(ins[2])
    elif(ins[0] == 'div'):
        opCode = 7
        rd = int(ins[1])
        rs = int(ins[2])
        rt = int(ins[3])
    elif(ins[0] == 'baw'):
        opCode = 8
        imm = int(ins[2])
    elif(ins[0] == 'and'):
        opCode = 9
        rd = int(ins[1])
        rs = int(ins[2])
        rt = int(ins[3])
    elif(ins[0] == 'cmp'):
        opCode = 10
        rd = int(ins[1])
        rs = int(ins[2])
        rt = int(ins[3])
    elif(ins[0] == 'or'):
        opCode = 11
        rd = int(ins[1])
        rs = int(ins[2])
        rt = int(ins[3])
    elif(ins[0] == 'ls'):
        opCode = 13
        rd = int(ins[1])
        rs = int(ins[2])
        rt = int(ins[3])
    elif(ins[0] == 'rs'):
        opCode = 15
        rd = int(ins[1])
        rs = int(ins[2])
        rt = int(ins[3])

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
