'''
n=6
arr=[1,2,3,4,1,2]
print(sum(arr))
print(min(arr))
print(max(arr))
min=arr[0]
max=arr[0]
for i in arr:
    if i<min:
        min=i
    elif i>max:
        max=i
print(min,max)
o=0
e=0
for i in arr:
    if i%2==0:
        e=e+1      
    else:
        o=o+1     
print('Even',e)
print('Odd',o)
a=[]
for i in range(n-1,-1,-1):
    a.append(arr[i])
print(a)
print(arr)
print(arr[::-1])

largest=arr[0]
second_largest=arr[0]
for i in arr:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i!=largest:
        second_largest=i
print(largest)
print(second_largest)
    
isSorted=True
for i in range(n-1):
    if arr[i]>arr[i+1]:
        isSorted=False
        break
if isSorted==True:
    print("Sorted")
else:
    print("Not Sorted")

k=2
leftrotation=[]
k=k%n
for i in range(k,n):
    leftrotation.append(arr[i])
for i in range(0,k):
    leftrotation.append(arr[i])
print(leftrotation)

k=2
rightrotation=[]
k=k%n
for i in range(n-k,n):
    rightrotation.append(arr[i])
for i in range(n-k):
    rightrotation.append(arr[i])
print(arr)
print(leftrotation)
print(rightrotation)

f={}
for i in arr:
    if i in f:
        f[i]=f[i]+1
    else:
        f[i]=1
print(f)

unique=[]
for i in a:
    if i not in unique:
        unique.append(i)
print(unique)

expected_sum = n * (n + 1) // 2
actual_sum = 0

for i in arr:
    actual_sum += i

print("Missing number =", expected_sum - actual_sum)
print(arr)
max_right = arr[-1]
print(max_right, end=" ")

for i in range(n-2, -1, -1):
    if arr[i] > max_right:
        max_right = arr[i]
        print(max_right, end=" ")

n=int(input())
a=list(map(int,input().split()))
pos=0
for i in range(len(a)):
    if a[i]!=0:
        a[pos]=a[i]
        pos=pos+1
for i in range(pos,len(a)):
    a[i]=0
print(*a)

n=int(input())
bin=""
while n>0:
    a=n%2
    bin=str(a)+bin
    n=n//2
print(bin)

n=int(input())
d=bin(n)
print(d[2:])

n=input()
d=0
p=0
for i in n[::-1]:
    d=d+int(i)*(2**p)
    p=p+1
print(d)

n=str(100)
dec=int(n,2)
print(dec)
'''
# n=10
# bin=""
# while n>0:
#     a=n%2
#     bin=str(a)+bin
#     n=n//2
# print(bin)
# toggle=''
# for i in bin:
#     if i=='0':
#         toggle+='1'
#     else:
#         toggle+='0'
# print(int(toggle,2))


# a=10
# b=""
# while a>0:
#     n=a%2
#     b=str(n)+b
#     a=a//2
# print(b) #1010
 
# a=10
# print(bin(a)[2:])

# a=2
# b=3
# r=1
# for i in range(b):
#     r=r*a
# print(r)

# n=[1,2,3,0,0,4,4,0,1,2]
# pos=0
# for i in range(len(n)):
#     if n[i]!=0:
#         n[pos]=n[i]
#         pos=pos+1
# for i in range(pos,len(n)):
#     n[i]=0
# print(n)

# a=[1,1,2,2,2,2,3,3,3,3,8,8]
# i=1
# j=1
# count=0
# while(j<len(a)):
#     if(a[j]!=a[i-1]):
#         a[i]=a[j]
#         i=i+1
#         count+=1
#     j=j+1
# print(a)
# print(count) #or i

a=[1,3,5]
b=[2,4,6]
c=[]
i=0
j=0
while(i<len(a) and j<len(b)):
    if(a[i]<b[j]):
        c.append(a[i])
        i=i+1
    elif(a[i]>b[j]):
        c.append(b[j])
        j=j+1
if(i!=len(a)):
    c.append(a[i])
if(j!=len(b)):
    c.append(b[j])
print(c)
