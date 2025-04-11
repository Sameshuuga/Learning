def codewrite(codes):
    ram = {'SP': 256, 'local' : 'LCL', 'argument' : 'ARG', 'this' : 'THIS' , 'that' : 'THAT'}
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

            if code[1] in ram:
                asmlist.append ('@'+ram[code[1]]+'\nA=M\nD=A\n@'+code[2]+'\nA=D+A\nA=M\nD=A\n@SP\nA=M\nM=D\n@SP\nAM=M+1') 
            
            if code[1] =='temp':
                asmlist.append ('@5\nD=A\n@'+code[2]+'\nA=D+A\nA=M\nD=A\n@SP\nA=M\nM=D\n@SP\nAM=M+1') 
            if code [1] == 'pointer':
                asmlist.append ('@3\nD=A\n@'+code[2]+'\nA=D+A\nA=M\nD=A\n@SP\nA=M\nM=D\n@SP\nAM=M+1')
            if code [1] == 'static':
                asmlist.append ('@16\nD=A\n@'+code[2]+'\nA=D+A\nA=M\nD=A\n@SP\nA=M\nM=D\n@SP\nAM=M+1')
        
        if 'pop' in code:
            if code [1] in ram:
                asmlist.append ('@'+ram[code[1]]+'\nA=M\nD=A\n@'+code[2]+'\nA=D+A\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\nM=0\n@R13\nA=M\nM=D')
            if code [1] == 'temp':
                asmlist.append ('@5\nD=A\n@'+code[2]+'\nA=D+A\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\nM=0\n@R13\nA=M\nM=D')  
            if code [1] == 'pointer':
                asmlist.append ('@3\nD=A\n@'+code[2]+'\nA=D+A\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\nM=0\n@R13\nA=M\nM=D')    
            if code [1] == 'static':
                asmlist.append ('@16\nD=A\n@'+code[2]+'\nA=D+A\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\nM=0\n@R13\nA=M\nM=D')  

        if code[0] in arithmetic: ### stack arith
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

