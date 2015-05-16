aantal = input()                    # Hoe veel zinnen?

for i in range(int(aantal)):
    zin = input()
    aantal_woorden = zin.split()
    
    if len(aantal_woorden)>4:
       print("Crackers!") 
    else:
        print(zin, "krAh!")
   