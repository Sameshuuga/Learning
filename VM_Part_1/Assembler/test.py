import pars
import copy

filename = input('File Name:')
path='HACK\\'+filename+'.hack'

with open(path,'r') as file:
    asm = file.read()

filename = input('File Name:')
path='HACK\\'+filename+'.hack'

with open(path,'r') as file:
    tasm = file.read()

code = pars.pars (asm)
tcode = pars.pars (tasm)

dif = copy.copy(code)
index = -1
indexlist = []
for item in code:
    index = index +1
    if item != tcode[index]:
        indexlist.append(index)

print (indexlist)





