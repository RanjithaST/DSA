'''
Two pointers
hashmap => O(n)

Sliding window protocol => O(n+) quite long
***** Not necessary that list will be in sorted order ****

Variations
1.fixed size
2.dynamic size

a=[10 20 30 40 50 60 70 80 90 100]
   i=0
   j=0
j is for insertion/accessing 
i is for deletion

a=[1,2,4,6,11,2,10,5]
window size=3
max sum in the subarray of size 3
            sum
1 2 4        7
2 4 6        12
4 6 11       21
6 11 2       19
11 2 10      23 (ans)
2 10 5       17

Prefix sum
i=0
j=0
size=3
[ 0 1 2]
so k=k-1 adjusting value of k with array indexing
1.Move j to perfect end (k)

sum=0
while(j<=k):
    sum = sum + a[i]
    j=j+1
'''
'''
a=[1,2,4,6,11,2,10,5]
i=0
j=0
k=3
k=k-1
sum=0

while(j<=k):
    j=j+1
j=j-1
while(j<=len(a)-1):
    i=i+1
    j=j+1
    print(a[i],a[j])

2 6
4 11
6 2
11 10
2 5

'''
'''
Brute force approach => O(n*k)

a=[1,2,4,6,11,2,10,5]
k=3
i=0
k=k-1
sum=0
maxsum=0
for i in range(0,len(a)-k):
    sum=0
    print(a[i])
    1
    2
    4
    6
    11
    2
    for j in range(i,i+k+1):
        sum=sum+a[j]
   
    print(sum)
    maxsum=max(maxsum,sum)
print("**************")
print(maxsum)
'''

a=[1,2,4,6,11,2,10,5]
k=3
i,j=0,0
sum=0
maxsum=0
while(j<k):
    sum=sum+a[j]
    j=j+1
while(j<len(a)):
    sum=sum+a[j]-a[i]
    maxsum=max(sum,maxsum)
    i=i+1
    j=j+1
print(maxsum)