import math

v=float(input())        # vuurkracht
z=float(input())        # zwaartekracht
a=float(input())        # horizontale afstand

print("{0:.2f}".format(0.5*math.asin((z*a)/v**2)))