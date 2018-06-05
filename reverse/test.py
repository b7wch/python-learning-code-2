#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/3/1
from capstone import *
import matplotlib.pyplot as plt

# from capstone.arm import *

CODE = b""
with open('./psftp.exe', "rb") as f:
    CODE += f.read()
CODE = CODE[2*16*16+4:]
md = Cs(CS_ARCH_X86, CS_MODE_32)
out = "./out.txt"
outf = open(out, 'w')
comm_dict = dict()
comm_num = 1
result = []
for i in md.disasm(CODE, 0x0001000):
    comm_n = 0
    if not comm_dict.get(i.mnemonic):
        comm_n = comm_num
        comm_num += 1
        comm_dict[i.mnemonic] = comm_n
    else:
        comm_n = comm_dict.get(i.mnemonic)
    result.append(comm_n)
    s = "0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str)
    outf.write(s + '\r\n')
    # print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))
print comm_dict
print result
lenght = len(result)
# x = [i for i in range(lenght)]
# plt.figure()
# plt.xlabel('time-line')
# plt.ylabel('command')
# plt.plot(x, result)
# plt.show()
outf.close()
