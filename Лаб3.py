x = int(input('x= '))
top = 1
down = 1
for i in range(2,64,2):
    top *=(x-i)
    down *=(x-(i-1))
try:
    k = top/down
except ZeroDivisionError:
    print('Denominator = 0. Run the program again and enter a different value')
    exit()
print(k)
