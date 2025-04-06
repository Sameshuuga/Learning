#opens .asm file
#converts file to a list of codes
#runs list through parser, code, and symbol
#returns binary in .hack file
import parser
import binary
filename = input('Name your File:')
address = 'ASM\\'+filename+'.asm'

with open (address, 'r') as file:  #opents and stores file contents as ASM 
    asm = (file.read())

#########################################

codelist = parser.parser(asm)
print (codelist)
print (len(codelist))

binarylist = binary.binary(codelist)
print (binarylist)

address = 'HACK\\'+filename+'.hack'
with open(address, 'w') as filename:
    for item in binarylist:
        filename.write(str(item)+'\n')
        continue

