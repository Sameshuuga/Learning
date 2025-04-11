def binary(cleanlist, ram):
    # takes list of asm code for HACK computer
    # returns list of 16 bit binary
    import copy
    destcode = {'000':'000', 'M':'001', 'D':'010','MD':'011', 'A':'100', 'AM':'101', 'AD':'110', 'AMD':'111', }
    jumpcode = {'000':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100','JNE':'101', 'JLE':'110', 'JMP':'111'}
    compcode = {'0':'0101010','1':'0111111','-1':'0111010','D':'0001100','A':'0110000','!D':'0001101','!A':'0110001','-D':'0001111','-A':'0110011','D+1':'0011111','A+1':'0110111','D-1':'0001110','A-1':'0110010','D+A':'0000010','D-A':'0010011','A-D':'0000111','D&A':'0000000','D|A':'0010101','M':'1110000','!M':'1110001','-M':'1110011','M+1':'1110111','M-1':'1110010','D+M':'1000010','D-M':'1010011','M-D':'1000111','D&M':'1000000','D|M':'1010101',}
    binarylist = copy.copy(cleanlist)
    index = -1
    for item in cleanlist:
        index = index + 1
        if item[0] == '@':
            key = item.replace('@', '')
            try:
                key = int(key)
                A_code = bin(key)[2:].zfill(16)
            except:
                A_code = bin(ram[key])[2:].zfill(16)  
            binarylist[index] = A_code
                  
        
        elif '=' in item or ';' in item:
            if '=' in item:
                dest = item.split('=')[0]
                comp = item.split('=')[-1].split(';')[0]
            else:
                dest = '000'
            if ';' in item:
                comp = item.split('=')[-1].split(';')[0]
                jump = item.split(';')[-1]
            else:
                jump = '000'
            C_code = '111'+compcode[comp]+destcode[dest]+jumpcode[jump]
            binarylist[index] = C_code
        
    return binarylist