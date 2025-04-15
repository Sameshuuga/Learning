def codewrite(codes):
    ram = {'SP': 256, 'local' : 'LCL', 'argument' : 'ARG', 'this' : 'THIS' , 'that' : 'THAT'}
    arithmetic = {'add': '+' ,'sub': '-','and': '&','or': '|'}
    moreorless = {'eq': ['JEQ','JNE'], 'lt': ['JLT','JGE'], 'gt': ['JGT','JLE'],}
    asmlist = []
    true = 0
    false = 0
    cont = 0
    resume = 0
    clear = 0

    for key in codes: 
        code = codes[key]
        if '.vm' in code[0]:
            filename = code[0]
        ##Programflow
        if code[0] == 'label':
            asmlist.append ('('+code[1]+')')
        if code[0] == 'goto':
            asmlist.append ('@'+code[1]+'\n0;JMP')
        if code [0] == 'if-goto':
            asmlist.append ('@SP\nAM=M-1\nD=M\n@'+code[1]+'\nD;JNE')
        ##Mem Access
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
                asmlist.append ('@'+filename+'.'+code[2]+'\nD=M\n@SP\nA=M\nM=D\n@SP\nAM=M+1')
        if 'pop' in code:
            if code [1] in ram:
                asmlist.append ('@'+ram[code[1]]+'\nA=M\nD=A\n@'+code[2]+'\nA=D+A\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\nM=0\n@R13\nA=M\nM=D')
            if code [1] == 'temp':
                asmlist.append ('@5\nD=A\n@'+code[2]+'\nA=D+A\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\nM=0\n@R13\nA=M\nM=D')  
            if code [1] == 'pointer':
                asmlist.append ('@3\nD=A\n@'+code[2]+'\nA=D+A\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\nM=0\n@R13\nA=M\nM=D')    
            if code [1] == 'static':
                asmlist.append ('@SP\nAM=M-1\nD=M\nM=0\n@'+filename+'.'+code[2]+'\nM=D')  
        ### stack arith
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
        ### function handling
        if code[0] == 'call':
            resume += 1
            asmlist.append('@resume'+str(resume)+'\nD=A\n@SP\nA=M\nM=D\n@SP\nAM=M+1') ##push return address
            asmlist.append('@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nAM=M+1\n@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nAM=M+1\n@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nAM=M+1\n@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nAM=M+1') ## push RAM
            asmlist.append('@SP\nD=M\n@'+str(int(code[2])+5)+'\nD=D-A\n@ARG\nM=D\n@SP\nD=M\n@LCL\nM=D\n@'+code[1]+'\n0;JMP\n(resume'+str(resume)+')') #Set new ARG and LCL base goto function
        if code[0] == 'function':
            clear += 1
            asmlist.append('('+code[1]+')\n@'+code[2]+'\nD=A\n@qwert'+str(clear)+'\nD;JEQ\n(clear'+str(clear)+')\n@SP\nA=M\nM=0\n@SP\nAM=M+1\nD=D-1\n@clear'+str(clear)+'\nD;JGT\n(qwert'+str(clear)+')') #sets jump lable and clears LCL segment
        if code[0] == 'return':
            asmlist.append('@LCL\nD=M\n@R13\nM=D\n@5\nA=D-A\nD=M\n@R14\nM=D') ## sets LCL to R13 and return address to R14 
            asmlist.append('@SP\nAM=M-1\nD=M\n@ARG\nA=M\nM=D\nD=A+1\n@SP\nM=D') ##returns value and resets SP
            asmlist.append('@R13\nAM=M-1\nD=M\n@THAT\nM=D\n@R13\nAM=M-1\nD=M\n@THIS\nM=D\n@R13\nAM=M-1\nD=M\n@ARG\nM=D\n@R13\nAM=M-1\nD=M\n@LCL\nM=D') ##resets RAM
            asmlist.append('@R14\nA=M\n0;JMP')

            

    return asmlist

