# parser function
# parses .asm code to be passed to code moduel
# Must be passed the .asm file as a list of codes
def parser(asm):
    rawlist = asm.split('@',1)        ########### No good fix later
    rawcode = '@'+rawlist [1]
    codelist = rawcode.splitlines()
    return codelist 
    

    
