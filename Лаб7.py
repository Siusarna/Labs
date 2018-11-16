import random
def matrix(n):
    g=[]
    for i in range(0,n):
        g.append(round(random.uniform(0,100),2))
    print (g)
    return g
n = int(input("n= "))
array=matrix(n)
k = int(input("k= "))
counter=0
summ = 0
for i in array:
    if i > k:
        summ+=i
        counter+=1
arithmetic_mean=round(summ/counter,3)
for i in range(0,len(array)):
    if array[i] > k:
        array[i]=arithmetic_mean
print (array)

        
