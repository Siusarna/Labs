n = int(input('n= '))
g = []
k = 0
if n >27:
    print ('N >= 27 ')
    exit()
else:
    for i in range (100,1000):
        j = i
        while j > 0 :
            g.append(j%10)
            j = j//10
        if sum(g) == n:
            print (i, end=' ')
            k +=1
            if k ==10:
                print ()
                k = 0
        g = []
