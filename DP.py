'''
DSA - "look up data structure"
a=[10,20,30,4,5,11,17,19,1,20,21,22]

i,j,k sum is min and i<j<k
a=[min(4)|19|min(1)] so min sum bcmz 24
min(4)|11|min(1) so min sum bcmz 16

i<j<k
min(max(a[j-1]))|a[j]|max(a[j+1]))

lookup table is applicable only for 2 elements in hashmap if target given
'''
'''
1.find a pair i,j where i<j and a[i]+a[j]=min
'''
l=[]
a=[1,2,-3,5,8,-11,2,3]
min1=[0]*len(a)
min1[0]=a[0]
for i in range(1,len(a)):
    min1[i]=min(min1[i-1],a[i])
print(min1)
#min1=[1,1,-3,-3,-3,-3,-3,-3] #min value upto that index no
for i in range(1,len(a)):
    x=a[i]+min1[i-1]
    l.append(x)
print(l)
print(min(l))

'''
1.find a pair i,j,k where i<j<k and a[i]+a[j]+a[k]=max
'''
l=[]
a=[1,4,3,7,8,11,2,1,0,2]
max1=[0]*len(a)
max1[0]=a[0]
for i in range(1,len(a)):
    max1[i]=max(max1[i-1],a[i])
print(max1)
for j in range(1,len(a)-1):
    x=max1[j-1]+a[j]+a[j+1]
    l.append(x)
print(l)
print(max(l))


# max11=float('inf')
# a1=[1,4,3,7,8,11,2,1,0,2]
# for i in range(len(a1)):
#     for j in range(i+1,len(a1)):
#             cur=a1[i]+a1[j]
#             if cur<max11:
#                 max11=cur
# print(max11)

'''
121 leetcode
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

7(buy) - 1,5,3,6,4 - loss
 problem of lookup
 a=[buy(min)|x|sell(max)]
'''

'''
Dynamic programing means

large problem statement
break into smaller chunks and proceed
al chunks will be done and last value will be final value

eg:
sum in dp:
[1,2,3,4,5]
[1,3,6,10,15] upto certain index
so sum is 15

smallest element:
[1,2,3,4,5,0,1]
[1,1,1,1,1,0,-]
'''
'''
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
5 pots,if one pot filled other must be empty, no 2 pots are adjacent
[1,0,1,0,1] n=1 ->true
[1,0,0,0,1] n=2 ->[1,0,1,0,1] -> 1 remaining so false

boundary case
[1] n=1 ->no
[0] n=1 ->yes
'''
