# python version 3.6
assem = open("assembly", 'r')
data = assem.read()
assem.close()
n = 8
lines = data.split(";\n")
lines = [x for x in lines if x != '']
cmddict = {
    'ADD': '1000',
    'SHR': '1001',
    'SHL': '1010',
    'NOT': '1011',
    'AND': '1100',
    'OR': '1101',
    'XOR': '1110',
    'CMP': '1111',
    'LOAD': '0000',
    'STOR': '0001',
    'DATA': '001000',
    'JMPR': '001100',
    'JMP': '01000000',
    'JmIf': '0101',
    'ClF': '01100000',
    'HALT': '01101111'
}
cmds = []
for cmd in lines:
    cmd = cmd.split(" ")
    cmd = [x.replace(x, cmddict[x]) if x in cmddict else x for x in cmd]
    cmd = [format(int(x[1:], 16), '02b') if x[0] == "R" else x for x in cmd]
    cmd = [format(int(x, 16), '08b') if x[:2] == '0x' else x for x in cmd]
    cmd = ''.join(cmd)
    cmd = [cmd[i:i+n] for i in range(0, len(cmd), n)]
    cmd = [format(int(x, 2), '02x') for x in cmd]
    cmds.append(" ".join(cmd))
cmds = " ".join(cmds)
cmds = cmds.split(" ")