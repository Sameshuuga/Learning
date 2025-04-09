def pars (asm):
    #takes asm file and removes comments and dead space
    #returns list of asm code
    raw = asm.splitlines()
    rawlist = []
    for item in raw:
        rawlist.append(item.strip())
    codelist=[]
    for item in rawlist:
        if item[:2] != '//'and item[:2] != '':
            codelist.append(item)
    return codelist

def clean (codelist):
    #takes list of asm code and removes (xxx) labels
    symbols = {}
    symbol = 15
    cleanlist = []
    for item in codelist:
        if item [0] != '(':
            cleanlist.append(item)

    return cleanlist

    