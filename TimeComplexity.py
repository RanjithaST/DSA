#Time complexity
'''
n=10
1. for i in range(n)
    Single loop always run in O(n).If and else doesnt matter

2.for i in range(n):
    for j in range(n):
 Two loops always run in O(n^2).

 i=1    j=10 times
 i=n    j=10 times
 so 10*10=100 times

3.for i in range(n):
    for j in range(i+1,n):
this 2 loops always run in O(n^2).No matter j value.
                            loop runs
 i=1    2,3,4,5,6,7,8,9,10      9
 i=2    3,4,5,6,7,8,9,10        8
 i=3    4,5,6,7,8,9,10          7
 i=4    5,6,7,8,9,10            6
 i=5    6,7,8,9,10              5
 i=6    7,8,9,10                4
 i=7    8,9,10                  3
 i=8    9,10                    2
 i=9    10                      1    

i=1+2+3+4+5+6+7+8+9
n(n+1)/2
n/2 + n^2/2
Rule= n is considered infinity(n) so n+1000000=n.inf/2=inf and inf^2/2=inf
so lets remove /
n+n^2
O(n^2+n).bcs n is small so neglet.square cannot be negleted.
O(n^2)

4.
2.for i in range(n):
    for j in range(n):
        for j in range(n):
Time complexity- O(n^3)
 
AS POWER INCREASES TIME COMPLEXITY INCREASES(BAD TIME COMPLEXITY)
So,try to write optimized code in O(n),worst case O(n^2)
'''
'''
a=[1,2,3,4,5,6,7,8,9,10]
Find triplet whose sum=k where i<j<k but below time complexity in n^3 so always try to reduce 1 loop.
'''
k1=13
n=10
a=[1,2,3,4,5,6,7,8,9,10]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if(a[i]+a[j]+a[k]==k1):
                print(a[i],a[j],a[k])
                print("Yes")

'''
Two sum in O(n)
Optimization in array is only possible by either hashmap or hashset
use mathematical formula
'''
a=[2,7,11,15]
#output: [0,1]
