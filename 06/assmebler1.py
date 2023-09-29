from required_functions import translate
from required_functions import symbolRemove

name1="Pong"
name=name1+".asm"
f=open(name)#open the asm file

#dealing with symbols
trimmedF=symbolRemove(f)
#print(trimmedF)

finalFile=""
for line in trimmedF:
    ans=translate(line)
    if ans!=None:
        finalFile=finalFile+ans+"\n"

f.close

f=open(name1+".hack","w") #create new file
f.write(finalFile)
f.close



