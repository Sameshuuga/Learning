def symboltable (codelist):
    import copy
    ram = {'R0':0,'R1':1, 'R2':2, 'R3':3,'R4':4,'R5':5,'R6':6,'R7':7,'R8':8,'R9':9,'R10':10,'R11':11,'R12':12,'R13':13,'R14':14,'R15':15,'SP':0,'LCL':1,'ARG':2,'THIS':3,'THAT':4,'SCREEN':16384,'KBD':24576}
    symbol = 15
    tracklist = copy.copy(codelist)
    for item in codelist:
        if item [0] == '(':
            ram[item[1:-1]] = tracklist.index(item)
            del tracklist[tracklist.index(item)]
    for item in codelist:
        if item[0] == '@':
            if item[1:] not in ram:
                try:
                    int(item[1:])
                    continue
                except:ValueError
                symbol = symbol + 1
                ram[item[1:]] = symbol

    return ram