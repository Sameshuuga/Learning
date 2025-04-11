import vmpars
import codewrite

filename = input('Name of .vm file:')
with open ('VM\\'+filename+'.vm', 'r') as file:
    vm = file.read()

asmlist = ['@256', 'D=A','@SP', 'M=D']

codelist = vmpars.vmpars(vm)

codes = vmpars.commandtype(codelist)
print (codes)

asmlist = asmlist + codewrite.codewrite(codes)
print (asmlist)

with open('Assembler\\ASM\\'+filename+'.asm', 'w') as asm:
    for item in asmlist:
        asm.write(str(item)+'\n')
        continue
    