a=input()
b=a.split()
if b[2]=="+":
    uitkomst=int(b[0])+int(b[1])
elif b[2]=="-":
    uitkomst=int(b[0])-int(b[1])
elif b[2]=="*":
    uitkomst=int(b[0])*int(b[1])
elif b[2]=="/":
    uitkomst=int(b[0])/int(b[1])

print("{0:.3f}".format(uitkomst))