import random
def creation(m,n):
    w = []
    t = []
    for i in range(0,m):
        for j in range(0,n):
            t.append(random.randint(-99,99))
        w.append(t)
        t = []
    return w

def printmatrix(q):
        print('\n'.join(str(value) for value in q))
def saddle(matrix):
    g = []
    e = []
    for i in range(len(matrix)):
        min_m = min(matrix[i])
        l = matrix[i]
        if l.count(min_m) != 1:
            continue
        g.append(min_m)
        index = l.index(min_m)
        for j in range(len(matrix)):
            g.append(matrix[j][index])
        if min_m == max(g):
            e.append(i)
            e.append(index)
            l = []
            g = []
        else:
            l = []
            g = []
    if len(e) == 0:
        k = ['Не має']
        return k
    else:
        return e
                    
                    
                
                
                
    


m = int(input('Рядків '))
n = int(input('Стовпців '))

#m2 = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3], [13, 12, 11, 10, 9, 8, 7, 6, 5, 4], [14, 13, 12, 11, 10, 9, 8, 7, 6, 5], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6], [16, 15, 14, 13, 12, 11, 10, 9, 8, 7], [17, 16, 15, 14, 13, 12, 11, 10, 9, 8], [18, 17, 16, 15, 14, 13, 12, 11, 10, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]]
#m3 =[[0,0,0],[2,1,2],[1,0,1]]
m1=creation(m,n)
printmatrix(m1)
print(' ')

a = saddle(m1)
print(a)
