def binary (codelist):
# Recives code list from parser and translates to binary
# Input a codelist containing an assembly program for a HACK machine
    import re
    import copy
    length = len (codelist) 
    symbols = dict()
    symbol = 15
    destcode = {'':'000', 'M':'001', 'D':'010','MD':'100', 'A':'100', 'AM':'101', 'AD':'110', 'AMD':'111', }
    jumpcode = {'':'000', 'JGT':'001', 'JEQ':'011', 'JGE':'011', 'JLT':'100','JNE':'101', 'JLE':'110', 'JMP':'111'}
    compcode = {'0':'0101010','1':'0111111','-1':'0111010','D':'0001100','A':'0110000','!D':'0001101','!A':'0110001','-D':'0001111','-A':'0110011','D+1':'0011111','A+1':'0110111','D-1':'0001110','A-1':'0110010','D+A':'0000010','D-A':'0010011','A-D':'0000111','D&A':'0000000','D|A':'0010101','M':'1110000','!M':'1110001','-M':'1110011','M+1':'1110111','M-1':'1110010','D+M':'1000010','D-M':'1010011','M-D':'1000111','D&M':'1000000','D|M':'1010101',}
    
    ###############################################################################################################
    templist =  copy.copy(codelist)
    for i in range(length + 1):             ##### append ROM location to Symbols used to jump
        if '(' in codelist [i-1] not in '//':
            L_command = codelist[i-1]
            templist.remove(L_command)
            L_command = L_command.replace('(','')
            L_command = L_command.replace(')','')
            L_command = '@'+L_command
            symbol = symbol + 1
            symbols [L_command] = bin(i-1)[2:].zfill(16)
            continue
        else:
            continue
    codelist = copy.copy(templist)
    length = len (codelist)

    for i in range(length + 1):
            if '//' in codelist [i-1]: 
                ignore = codelist [i-1]
                templist.remove(ignore)
                continue
            else:
                continue
    codelist = templist
    length = len (templist)

    for i in range(length+1):                    ######## length + 1 since range = length - 1
        if '@' in codelist[i-1]:
            A_command = codelist[i-1]            ######## i - 1 since i of 1 = list index [0]
            if '@R0' in A_command or '@SP' in A_command:
                A_command = bin(0)[2:].zfill(16)
            elif '@R1' in A_command  or '@LCL' in  A_command:
                A_command = bin(1)[2:].zfill(16)
            elif '@R2' in A_command or '@ARG' in A_command:
                A_command = bin(2)[2:].zfill(16)
            elif '@R3' in A_command or '@THIS' in A_command:
                A_command = bin(3)[2:].zfill(16)
            elif '@R4' in A_command or "@THAT" in A_command:
                A_command = bin(4)[2:].zfill(16)
            elif ('@R5') in A_command:          
                A_command = bin(5)[2:].zfill(16)
            elif ('@R6') in A_command:          
                A_command = bin(6)[2:].zfill(16)
            elif ('@R7') in A_command:          
                A_command = bin(7)[2:].zfill(16)
            elif ('@R8') in A_command:          
                A_command = bin(8)[2:].zfill(16)
            elif ('@R9') in A_command:          
                A_command = bin(9)[2:].zfill(16)
            elif ('@R10') in A_command:         
                A_command = bin(10)[2:].zfill(16)
            elif ('@R11') in A_command:         
                A_command = bin(11)[2:].zfill(16)
            elif ('@R12') in A_command:         
                A_command = bin(12)[2:].zfill(16)
            elif ('@R13') in A_command:         
                A_command = bin(13)[2:].zfill(16)
            elif ('@R14') in A_command:         
                A_command = bin(14)[2:].zfill(16)
            elif ('@R15') in A_command:         
                A_command = bin(15)[2:].zfill(16)
            elif ('SCREEN') in A_command:         
                A_command = bin(16384)[2:].zfill(16)   
            elif ('KBD') in A_command:         
                A_command = bin(24576)[2:].zfill(16)
            else:
                ########## checks for integer and converts to binary ##############
                try:                                        
                    A_command = A_command.replace('@','')
                    A_command.strip() #remove after fixing parser
                    A_command = int(A_command)
                    A_command = bin(A_command)[2:].zfill(16)

                ########## handles symbol storage usign a dict ###############
                except ValueError:  
                    if A_command in symbols:
                        A_command = bin(symbols [A_command])[2:].zfill(16)
                    else:
                        symbol = symbol + 1
                        symbols [A_command] = symbol
                        A_command = bin(symbols [A_command])[2:].zfill(16)

            codelist [i-1] = A_command
            continue

        elif "=" in codelist[i-1] or ';'in codelist[i-1]:                   #### dest = comp;jump
            C_command = codelist[i-1]
            C_command = C_command.strip() ##### remove after fixing parser
            lead_binary = "111"
            if '=' in C_command:
                dest = C_command.split('=')[0]
                dest_binary = destcode[dest]
            else:
                dest_binary = '000'
            if ';' in C_command:
                jump = C_command.split(';')[-1]
                jump_binary = jumpcode[jump]
            else:
                jump_binary = '000'
            
            comp = C_command.split('=')[-1].split(';')[0]
            comp_binary = compcode[comp]
            C_command = lead_binary+comp_binary+dest_binary+jump_binary
            codelist[i-1]=C_command
            continue
        else:
            continue
    
    
    


    return codelist