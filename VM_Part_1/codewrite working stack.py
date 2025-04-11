def codewrite(codes):
    ram = {'SP': 256, 'LCL' : 0, 'ARG' : 0, 'THIS' : 0, 'THAT' : 0}
    arithmetic = {'add': '+' ,'sub': '-','and': '&','or': '|'}
    moreorless = {'eq': ['JEQ','JNE'], 'lt': ['JLT','JGE'], 'gt': ['JGT','JLE'],}
    asmlist = []
    true = 0
    false = 0
    cont = 0

    for key in codes:
        code = codes[key]
        if 'push' in code:
            if 'constant' in code:
                asmlist.append ('@'+str(code[2])+'\nD=A\n@SP\nA=M\nM=D\n@SP\nAM=M+1')
        if code[0] in arithmetic:
            if code[0] != 'sub':
                asmlist.append ('@SP\nAM=M-1\nD=M\n@SP\nAM=M-1\nA=M\nD=D'+str(arithmetic[code[0]])+'A\n@SP\nA=M\nM=D\n@SP\nAM=M+1')
            elif code[0] == 'sub':
                asmlist.append ('@SP\nAM=M-1\nD=M\n@SP\nAM=M-1\nA=M\nD=A'+str(arithmetic[code[0]])+'D\n@SP\nA=M\nM=D\n@SP\nAM=M+1')
        if code[0] in moreorless:
            true += 1
            false += 1
            cont += 1
            asmlist.append ('@SP\nAM=M-1\nD=M\n@SP\nAM=M-1\nA=M\nD=A-D\n@true'+str(true)+'\nD;'+str(moreorless[code[0]][0])+'\n@false'+str(false)+'\nD;'+str(moreorless[code[0]][1]))
            asmlist.append ('(true'+str(true)+')\n@SP\nA=M\nM=-1\n@SP\nAM=M+1\n@cont'+str(cont)+'\n0;JMP')
            asmlist.append ('(false'+str(false)+')\n@SP\nA=M\nM=0\n@SP\nAM=M+1\n(cont'+str(cont)+')')
        if code[0] == 'not':
            asmlist.append ('@SP\nAM=M-1\nD=!M\nM=D\n@SP\nAM=M+1')
        if code[0] == 'neg':
            asmlist.append ('@SP\nAM=M-1\nD=-M\nM=D\n@SP\nAM=M+1')

            




    return asmlist

