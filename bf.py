#initializes the array with zeros
code = """
a=[]
for i in range(30000):
    a.append(0)
          
i=0

"""
#opens the files 
file = open("r.py","w")
bfcode = open("test.bf", "r")
bfcode = bfcode.read()

TabCounter = 0
LoopCounter = 0
LoopCommandArray = []



for i in range(len(bfcode)):
    NewLine = True
    if bfcode[i]=="+":
        code+="\t"*TabCounter+"a[i]+=1 "#+"

    elif bfcode[i]=="-":
        code+="\t"*TabCounter+"a[i]-=1 "#-"

    elif bfcode[i]=="<":
        code+="\t"*TabCounter+"i = i-1 if i-1>0 else 30000-1 "#\n"+"\t"*TabCounter+"except:"+"i=30000 "#<"

    elif bfcode[i]==">":
        code+="\t"*TabCounter+"i=i+1 if i+1>30000 else 0"# \n"+"\t"*TabCounter+"except:"+"i=0 "#>"

    elif bfcode[i]==".":
        code+="\t"*TabCounter+"print(chr(a[i]),end='') "#."

    elif bfcode[i]==",":
        code+="\t"*TabCounter+"a[i]=ord(input()) "#,"

    elif bfcode[i]=="[":
        LoopCounter+=1
        LoopCommandArray.append(i)
        code+="\t"*TabCounter+("b"*LoopCounter)+" = not a[i]\n"
        code+="\t"*TabCounter+"while a[i]: "#["

        TabCounter+=1
    elif bfcode[i]=="]":
        #code+="#]\n"
        TabCounter-=1
        LoopCounter-=1
    else:
        NewLine = False
    if NewLine:
        code+="\n"

file.write(code)



