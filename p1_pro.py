lt = [12, 13, 14, 15]
l = []
for num in lt:
    s = 0
    for i in str(num):
        s += int(i)
    l.append(s)
print(l)
s1 = 0
for i in l:
    s1 += i
print(s1)

for i in range(1, 5):
    print('*'*i)

for i in range(1, 5):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j, end=' ')
    print()


nested_list = [[1,3,4], [5,4,3]]
rev_list = []
for sub_list in nested_list:
    rev_list.append(sub_list[::-1])

print(rev_list)

for sub_list in rev_list:
    print(sum(sub_list))

dt = [{'one':[1,2]},{'two':[2,3]}]
for k in dt:
    for k1 in k:
        if k1 == 'one':
            k[k1].append(1)
print(dt)

for i in range(1, 5):
    for j in range(1, 5):
        if i == 1 or i == 4 or j == 1 or j == 4:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

print('@@@@@@@@@')
m = 6
for i in range(1,m):
    for j in range(1,m):
        if i == j or j == m-i:
            print('@', end=' ')
        else:
            print('',end=' ')
    print()

n = 6
for i in range(0, n+1):
    for j in range(0,n+1):
        if i == n//2 or j == n//2:
            print('#', end=' ')
        else:
            print(' ',end=' ')
    print()

y = 6
for i in range(0, y):
    for j in range(0,y):
        if i == 0 or i == y-1 or j == y-i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

A = 65

for i in range(0, 5):
    for j in range(0, i+1):
        print(chr(A+j), end=' ')

    print()

y = 6
for i in range(1,y):
    for j in range(1,y):
        if i == j or j == y-i:
            print('@', end=' ')
        else:
            print('',end=' ')
    print()

print('do something...')
z = 6
for i in range(1, z):
    for j in range(i,z):
        print(' ',end='')
    for k in range(0, i*2-1):
        print('@',end='')
    print()
for i in range(z, 0, -1):
    for j in range(i,z):
        print(' ',end='')
    for k in range(0, i*2-1):
        print('@',end='')
    print()

print("Don’t leave this world without doing anything ,leave after creating something meaningful.")


r = 5
for i in range(0, r):
    for j in range(0, i+1):
        if j == 0 or j == i:
            print('@', end=' ')
        elif i == r-1:
            for k in range(0, j//2):
                print('@',end=' ')
        else:
            print(end=' ')

    print()

print('print y shape pattern ...')

size = 7
mid = size // 2
char = '*'
for r in range(size):
    for c in range(size):
        if r <= mid and (c == r or c == size - 1 - r):
            print(char, end="")
        elif r > mid and c == mid:
            print(char, end="")
        else:
            print(" ", end="")
    print()

