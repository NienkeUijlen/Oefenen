hoogste_niveau=int(input())
toeschouwers=list(input())


i=0
s=0     #aantal mensen die staan
v=0     #aantal vrienden
while i<=hoogste_niveau:
    if s<int(i):
        v=v+1
    else:
        v=v
    s=s+int(toeschouwers[i])+v
    i=i+1
    
print(v)
        
    