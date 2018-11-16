import math
x = int(input('x= '))
e = int(input('e= '))
sh = 0
i = 1
n = 1
k = x
while n <=e:
    sh += k
    k *= x**2/((2*n+1)*2*n)
    n += 1
print (round(sh,4))
