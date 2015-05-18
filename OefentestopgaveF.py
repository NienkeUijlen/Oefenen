hoogste_niveau=int(input())
toeschouwers=list(input())


i=1
s=int(toeschouwers[0])      #aantal mensen die staan
v=0                         #aantal vrienden
while i<=hoogste_niveau:
    if s<i:
        v=v+1
        s=s+int(toeschouwers[i])+1
    else:
        s=s+int(toeschouwers[i])
    i=i+1
    
print(v)
        
    