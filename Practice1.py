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