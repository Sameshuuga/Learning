import os
import vmpars
import codewrite
directory = 'VM\\' + input('Directory:')
path = os.listdir(directory)
print(path)
vm = 'call Sys.init 0\n'

for file in path:
    if '.vm' in file: 
        filepath = directory +'\\'+file
        with open (filepath, 'r') as vmfile:
            vmfile = vmfile.read()
            vm = vm + file + '\n' + vmfile

print(vm)

asmlist = ['@256', 'D=A','@SP', 'M=D']  ## 

codelist = vmpars.vmpars(vm)

codes = vmpars.commandtype(codelist)
print(codes)

asmlist = asmlist + codewrite.codewrite(codes)
print(asmlist)

with open(directory +'\\'+input('Name .asm file:')+'.asm', 'w') as asm:
    for item in asmlist:
        asm.write(str(item)+'\n')
        continue