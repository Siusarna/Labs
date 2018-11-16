import math
x = float(input('x= '))
y = float(input('y= '))
if ((x+2)**2+y**2>=1 and (x+2)**2+y**2<=4) or (x>=-1):
    print("This point is in the shaded area")
else:
    print('This point is not in the shaded area')
