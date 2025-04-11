def vmpars (vm):
    #takes .vm file and removes comments and dead space
    #returns list of vm code
    raw = vm.splitlines()
    rawlist = []
    for item in raw:
        rawlist.append(item.strip())
    codelist=[]
    for item in rawlist:
        if item[:2] != '//'and item[:2] != '':
            codelist.append(item)
    return codelist

def commandtype (codelist):
    #takes list of .vm code and creates a list to assign command type
    key = 0
    codes  = {}
    for item in codelist:
        code = item.split(' ')
        codes[key] = code
        key += 1
        

    return codes