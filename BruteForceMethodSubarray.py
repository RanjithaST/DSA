'''
Docstring for DSA.BruteForceMethodSubarray

Subarray:Continous part of the main array
a=[10,20,30,40,50]
[10] - yes
[20,30] - yes
[10,20,40] - no because 30 is missing
'''

#BruteForce method to generate all values subarray - Time complexity- O(n^3)
a=[10,20,30]
# for i in range(0,len(a)):
#     for j in range(i,len(a)):
#         for k in range(j,len(a)):
#             print(a[k],end=" ")
#         print(" ")
###################################################################################
'''
10  
10 20  
10 20 30
20
20 30
30
'''
for i in range(len(a)):#left bound
    for j in range(i,len(a)):#right bound
        for k in range(i,j+1):#all values
            print(a[k],end=" ")
        print(" ")
###################################################################################

'''
10 20
10 30
20 30
'''

for i in range(len(a)):
    for j in range(i+1,len(a)):
            print(a[i],a[j])
###################################################################################
#print sum of all sub arrays
'''
10 ---SUM-- 10

10 20 ---SUM-- 30

10 20 30 ---SUM-- 60

20 ---SUM-- 20

20 30 ---SUM-- 50

30 ---SUM-- 30
'''
for i in range(len(a)):#left bound
    for j in range(i,len(a)):#right bound
        sum=0
        for k in range(i,j+1):#all values
            print(a[k],end=" ")
            sum=sum+a[k]
        print("---SUM--",sum)
        print(" ")
####################################################################################
#count all subarrays with sum=k
#ans=2
Target=30
count=0
for i in range(len(a)):
     for j in range(i,len(a)):
          s=0
          for k in range(i,j+1):
               s+=a[k]
               print(a[k],end=" ")
          if(s==Target):
                count+=1
          print(" ")
print(count)

'''
Subarray concept

1.lock value of i(0-n)
2.lock value of j(i-n)
i and j are range
3.print no from i,j range using k
'''
###################################################################################
'''
0 0
[10]
0 1
[10, 20]
0 2
[10, 20, 30]
1 1
[20]
1 2
[20, 30]
2 2
[30]
 
'''
for i in range(len(a)):
     for j in range(i,len(a)):
          print(i,j)
          print(a[i:j+1])
     print(" ")
         

