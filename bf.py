file = open("r.py","w")
bfcode = open("test.bf", "r")
bfcode = bfcode.read()
bfcode = bfcode.replace(" ","").replace("\n","").replace("\t","")


file.write("""a=[]
for i in range(30000):
    a.append(0)
              
i=0
""")

for i in range(len(bfcode)):
    if bfcode[i]=="+":
        file.write("a[i]+=1")
    elif bfcode[i]=="-":
        file.write("a[i]-=1")
    elif bfcode[i]=="<":
        file.write("""try:
    i-=1
    a[i]
except:
    i = 30000""")
    elif bfcode[i]==">":
        file.write("""try:
    i+=1
    a[i]
except:
    i=0""")
    file.write("\n")
    
