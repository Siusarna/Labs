from math import factorial as fict
def Pascal (n):
    g =  []
    C = fict(n)/(fict(0)*fict(n-0))
    g.append(C)
    k = C
    for i in range  (1,n+1):
       k = k * ((n-i) + 1)/i
       g.append(k)
    return g
N = int(input('N= '))
for n in range (0,N+1):
    print(Pascal(n))
    
