def translate(line):
    ans=''

#for A instruction
    if line[0]=='@':
        ans1=bin(int(line[1:]))
        ans='0'*(16-len(ans1)+2)+str(ans1[2:])
#for C instructions
    else:
        branch=""
        dest=""
        comp=""
        
        split1=line.split(";")
        #print("split1",split1)
        if len(split1)>1:
            branch=split1[1]
        
        leftHalf=split1[0]        
        split2=leftHalf.split("=")
        if len(split2)>1:
            dest=split2[0]
            comp=split2[1]
        else:
            comp=split1[0]    

        #find code for destination
        ddd=['0','0','0']
        if 'M' in dest:ddd[2]='1'
        if 'D' in dest:ddd[1]='1'
        if 'A' in dest:ddd[0]='1'
        ddd=''.join(ddd)

        #find code for branch
        jjjDict={ "":"000" , "JGT":"001" ,"JEQ":"010", "JGE":"011", "JLT":"100", "JNE":"101", "JLE":"110", "JMP":"111" }
        jjj=jjjDict[branch]

        #find code for comp
        a="0"
        if "M" in comp:
             a="1"
             comp=comp.replace("M","A")

        c6Dict1={
            "0":"101010" , "1":"111111" , "-1":"111010" , "D":"001100" , "!D":"001111" , "D+1":"011111" , "D-1":"001110" ,
            "A":"110000" , "!A":"110001" , "-A":"110011" , "A+1":"110111" , "A-1":"110010" , "D+A":"000010" , "D-A":"010011" , "A-D":"000111" , "D&A": "000000" , "D|A": "010101"
        }
        c6=c6Dict1[comp]

        ans="111"+a+c6+ddd+jjj
        #print("dest='{}', ddd= {},comp='{}',a={}, c6={},branch='{}', jjj={}".format(dest,ddd,comp,a,c6,branch,jjj))  

    #print(ans)
    return ans 

def findempty(num,array):
    if num not in array:
        return num
    else:
        return findempty(num+1,array)

def symbolRemove(file):

    symboltable={"R0":0,"R1":1,"R2":2,"R3":3,"R4":4,"R5":5,"R6":6,"R7":7,"R8":8,"R9":9,"R10":10,"R11":11,"R12":12,"R13":13,"R14":14,"R15":15,"SCREEN":16384,"KBD":24576,"SP":0,"LCL":1,"ARG":2,"THIS":3,"THAT":4}
    lineNumber=0
    #iteration 1, finding symbols
    file1=[]
    for line in file:
        #removing all the spaces    
        line=line.replace(" ","")
        line=line.replace("\n","")
        if len(line)<1:
            continue
        #comments
        if line.startswith("//"):
            continue

        if line.startswith('('):
            sym=line.replace("(","")
            sym=sym.replace(")","")
            sym=sym.replace(" ","")
            sym=sym.replace("\n","")
            if sym not in symboltable.keys():
                symboltable[sym]=lineNumber
        else:
            lineNumber=lineNumber+1   
        file1.append(line)

    #making the array to be translated
    memory_pointer=10 #starting of memory pointer
    trimmed_array=[]
    #iteration 2 removing symbls
    for line in file1:

        #this was just a marker
        if line.startswith("("):
            continue

        if "@" in line:
            sym=line.replace("@","")
            try :
                num=int(sym)

            except:
                if sym not in symboltable.keys():
                    emptyPlace=findempty(memory_pointer,symboltable.values())
                    symboltable[sym]=emptyPlace
                    memory_pointer=emptyPlace

                line=line.replace(sym,str(symboltable[sym]))
        trimmed_array.append(line.split("//")[0])  
    #print(symboltable)    
    return trimmed_array          