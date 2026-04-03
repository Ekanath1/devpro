import math

# Bubble sort
lt = [1, 2, 3, 4, 5, 6]

n = len(lt)
for i in range(n):
    for j in range(i+1, n):
        if lt[i] < lt[j]:
            lt[i], lt[j] = lt[j], lt[i]
print('sorted in descending order ',lt)

str1 = "Ram"
age = int(input("Enter your age "))

s = ""
for i in range(len(str1)-1,-1,-1):
    s += str1[i]
s = s+str(age)
print('reverse string ',s)

print("to print prime numbers between 2 to 100")
def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

l = []
for i in range(2,100):
    if is_prime(i):
        l.append(i)
print('prime numbers ',l)


num = int(input("Enter positive number "))

cnt = 0
for i in range(1,num+1):
    if num%i == 0:
        cnt += 1

if cnt == 2:
    print('Prime Number')
else:
    print("Not Prime Number")

print("To check multiple prime numbers ")


print()
# info interview python programs
var_str = 'python programming'

vowels = 'aioue'
cnt = 0
cnt1 = 0
for ch in var_str:
    if ch in vowels:
        cnt += 1
    elif ch == 'g':
        cnt1 += 1

print('no of vowels present in the given string',cnt)

print('no of times g is repeated',cnt1)

d = {}
for ch in var_str:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print({k:v for k,v in d.items() if k != ' '})

sum_0 = 0
count_num = 0
while True:
    try:
        n = int(input("Enter value or type 0 "))
        if n == 0:
            break
        sum_0 += n
        count_num += 1
    except (ValueError,TypeError):
        print("please type integer value ")
        continue

print('total sum ', sum_0)
print('total number entered ',count_num)

def character_count(string):
    ch_count = 0
    digit_cnt = 0
    c_let = 0
    for c in string:
        if c.isalpha():
            ch_count += 1
        elif c.isdigit():
            digit_cnt += 1
        elif c.upper():
            c_let += 1
    return [ch_count,digit_cnt, c_let]

input_str = input("Enter string ")
res = character_count(input_str)
print('no of characters present in above str ',res[0])
print('no of digits present in above str ',res[1])
print('no of capital letters in above str ',res[2])

# Binary search program
def binary_search(l,k):
    k = 4
    lwr = 0
    upr = len(l)-1
    while lwr <= upr:
        mid = (lwr+upr)//2
        if k == l[mid]:
            return mid
        elif k < l[mid]:
            upr = mid - 1
        else:
            lwr = mid + 1

    return None

k = 4
lt = [1, 2, 3, 4, 5, 6]
res = binary_search(lt,k)
if res:
    print('element found at location ',res)
else:
    print('element not found')


def linear_search(l,k):
    length = len(l)
    for num in range(length):
        if k == l[num]:
            return num
    return None

elements = [1, 2, 3, 4, 5, 6]
key = 3
result = linear_search(elements,key)
if result:
    print('element found at location ',result)
else:
    print('element not found ')


