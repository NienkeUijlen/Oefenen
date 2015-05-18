eerste_rij=list(input())
tweede_rij=list(input())
derde_rij=list(input())

a=int(eerste_rij[0])
b=int(eerste_rij[1])
c=int(eerste_rij[2])

d=int(tweede_rij[0])
e=int(tweede_rij[1])
f=int(tweede_rij[2])

g=int(derde_rij[0])
h=int(derde_rij[1])
i=int(derde_rij[2])


if a==b==c:
    if a==1:
        print("Player 1 wins")
    elif a==2:
        print("Player 2 wins")
elif d==e==f:
    if d==1:
        print("Player 1 wins")
    elif d==2:
        print("Player 2 wins")
elif g==h==i:
    if g==1:
        print("Player 1 wins")
    elif g==2:
        print("Player 2 wins")
elif a==d==g:
    if a==1:
        print("Player 1 wins")
    elif a==2:
        print("Player 2 wins")
elif b==e==h:
    if b==1:
        print("Player 1 wins")
    elif b==2:
        print("Player 2 wins")
elif c==f==i:
    if c==1:
        print("Player 1 wins")
    elif c==2:
        print("Player 2 wins")
elif a==e==i:
    if a==1:
        print("Player 1 wins")
    elif a==2:
        print("Player 2 wins")
elif c==e==g:
    if c==1:
        print("Player 1 wins")
    elif c==2:
        print("Player 2 wins")
else:
    print("No winner")