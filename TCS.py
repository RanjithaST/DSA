'''
Array
case 1:
size=3
1 2 3
(space separated)
n = int(input())
arr = list(map(int, input().split()))
input: 
3
1 2 3

case 2:size not gives
1,2,3,4(comma separated)
arr = list(map(int, input().split(',')))
input:
3
1,2,3

case 3:
n = int(input())        # size
s = input()             # array as string
arr = list(map(int, s[1:-1].split(',')))
print(arr)
input:
3
[1,3,5]

case 4:
n = int(input())        # size
arr=[]
for i in range(n):
    arr.append(int(input()))
print(arr)
3
1
2
3
[1, 2, 3]

String:
n = int(input())
s = input()
5 
hello

n, s = input().split()
n = int(n)
print(n)
print(s)

n = int(input())      # size
s = input()           # {r,g,b,b,g}
arr = s[1:-1].split(',')
print(arr)
'''
'''
**##
0

**###
-1

star=0
hash=0
s=input()
for i in s:
    if i=='*':
        star=star+1
    else:
        hash=hash+1
print(star-hash)

count the elements that are greater than prior
5
7 4 8 2 9
3

count=1
n=int(input())
arr=list(map(int,input().split()))
count=1
max=arr[0]
for i in arr:
    if i>max:
        max=i
        count=count+1
print(count)
'''
'''
5
{g,g,b,b,a}
{'g': 2, 'b': 2, 'a': 1}
a

n = int(input())      # size
s = input()           
h={}
count=0
found=False
for i in s:
    if i in h:
        count=h[i]
        count=count+1
        h[i]=count
    else:
        h[i]=1
print(h)
for k in h:
    if h[k]%2!=0:
        print(k)
        found=True
        break
if found==False:
    print("All are even")  
'''  
# To return only single element
#xor - x^y=1 and y^y=0

s = input() 
ans=0
for i in range(len(s)):
    ans=ans^ord(s[i])
print(chr(ans))
    
