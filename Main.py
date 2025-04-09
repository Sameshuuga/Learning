import pars
import binary
import symbol

filename = input('File Name:')
path='ASM\\'+filename+'.asm'

with open(path,'r') as file:
    asm = file.read()

codelist = pars.pars(asm)
cleanlist = pars.clean(codelist)

print(cleanlist)

ram = symbol.symboltable(codelist)
print(ram)
binarylist = binary.binary(cleanlist, ram)

print(binarylist)


with open('HACK\\'+filename+'.hack', 'w') as hack:
    for item in binarylist:
        hack.write(str(item)+'\n')
        continue