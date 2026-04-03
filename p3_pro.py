print('arithmatic series....programs.....')
n = int(input("Enter positive number "))

a = 1
cnt = 0
for i in range(0, n):
    cnt += a
    print(a,end=' ')
    a += 4

print(cnt)

print('multiplication series ')
mul = 0
a = 2
for i in range(n):
    mul += a
    print(a,end=' ')
    a *= 2
print()
print('multiplication series sum is ',mul)

''' arithmatic series sum '''

sum_a = 0
for i in range(1, n+1):
    sum_a += i
print(f'sum of series is {sum_a}')

sum_of_diff = 0
d = n
for i in range(1, n+1):
    sum_of_diff += d
    d -= 1

print(f'difference series is {sum_of_diff}')

pw = 1
a = 2
for i in range(1, n+1):
    pw += pw * a
    print(pw)
print('power series is ',pw)
