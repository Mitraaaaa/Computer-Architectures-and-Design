def int2bin(opCode, rs, rt, rd, imm):
    if opCode % 2:
        opcode_hx = appendZero(str(bin(opCode)))
        rs_hx = appendZero(str(bin(rs)))
        rt_hx = appendZero(str(bin(rt)))
        rd_hx = appendZero(str(bin(rd)))
        imm_hx = ""

    elif opCode == 0 or opCode == 2:
        opcode_hx = appendZero(str(bin(opCode)))
        rs_hx = appendZero(str(bin(rs)))
        rt_hx = appendZero(str(bin(rt)))
        rd_hx = ""
        imm_hx = appendZero(str(bin(imm)))

    elif opCode == 4:
        opcode_hx = appendZero(str(bin(opCode)))
        rs_hx = ""
        rt_hx = appendZero(str(bin(rt)))
        rd_hx = ""
        imm_hx = appendZero(str(bin(imm)))

    elif opCode == 6:
        opcode_hx = appendZero(str(bin(opCode)))
        rs_hx = appendZero(str(bin(rs)))
        rt_hx = ""
        rd_hx = ""
        imm_hx = appendZero(str(bin(imm)))

    else:
        opcode_hx = appendZero(str(bin(opCode)))
        rs_hx = ""
        rt_hx = "0000"
        rd_hx = ""
        imm_hx = appendZero(str(bin(imm)))

    return str(opcode_hx).replace("0b", "") + str(rs_hx).replace("0b", "") + str(rt_hx).replace("0b", "") + str(rd_hx).replace("0b", "") + str(imm_hx).replace("0b", "")


def appendZero(st):
    adder = "0"*(6-len(st))
    return adder + st
