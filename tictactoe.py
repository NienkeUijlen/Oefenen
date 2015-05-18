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


if a==b==c==1:
        print("Player 1 wins")
elif a==b==c==2:
        print("Player 2 wins")
elif d==e==f==1:
        print("Player 1 wins")
elif d==e==f==2:
        print("Player 2 wins")
elif g==h==i==1:
        print("Player 1 wins")
elif g==h==i==2:
        print("Player 2 wins")
elif a==d==g==1:
        print("Player 1 wins")
elif a==d==g==2:
        print("Player 2 wins")
elif b==e==h==1:
        print("Player 1 wins")
elif b==e==h==2:
        print("Player 2 wins")
elif c==f==i==1:
        print("Player 1 wins")
elif c==f==i==2:
        print("Player 2 wins")
elif a==e==i==1:
        print("Player 1 wins")
elif a==e==i==2:
        print("Player 2 wins")
elif c==e==g==1:
        print("Player 1 wins")
elif c==e==g==2:
        print("Player 2 wins")
else:
    print("No winner")