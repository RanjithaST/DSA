'''
Docstring for DSA.BruteForceMethod.
Brute force method - not optimised but we can get the output.
Try every single combination-very slow
'''
#Generating all the pairs of array
'''
a=[1,2,3,4,5]   25 combinations
1,1 2,1
1,2 2,2
1,3  .
1,4  .
1,5  . so on
'''
a=[1,2,3,4,5]
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i],a[j])
    print(" ")

#i<j then j starts from i+1
for i in range(len(a)):
    for j in range(i+1,len(a)):
        print(a[i],a[j])
    print(" ")

'''
Two types of bruteforce
1.With repetation
a=[1,2,3,4,5]
a=[1] - 1,2,3,4,5 (combine with all) = 25 combinations

2.without repetation like 1,1 or 1,2 and 2,1-only single value
a=[1,2,3,4,5]
condition i<j
i=0 j=1,2,3,4
i=1 j=2,3,4
when i starts from 0 then j starts from i+1
'''

#Sum of all pairs from i and j
total=0
for i in range(len(a)):
    for j in range(len(a)):
        print(f"{a[i]}+{a[j]}={a[i]+a[j]}")
    print(" ")

#Sum of all pairs from i and j without repetation
total=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        print(f"{a[i]}+{a[j]}={a[i]+a[j]}")
    print(" ")

#print all pairs (i,j) where sum=k and i<j
a=[10,20,30,40,50]
target=60
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]+a[j]==target):
            print(a[i],a[j])

#triplet sum a[i]+a[j]+a[k]==sum and i<j<k
#i=0 j=i+k k=j+k
a=[10,20,30]
sum=60
for i in range(len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            if(a[i]+a[j]+a[k]==sum):
                print(f"{a[i]}+{a[j]}+{a[k]}={a[i]+a[j]+a[k]}")
#Not optimized-time complexity error

#find pairs such that a[j]-a[i]==k i<j
a=[10,20,30,40,50,70]
target=60
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[j]-a[i]==target):
            print(a[i],a[j])
#*****************************************************************************
a=[3,4,1,2,3,4,5]
k=1
'''
3-1=1
2-1=1
4-3=1
'''

#1<k<10^9
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(abs(a[j]-a[i])==k):
            print(f"{a[j]}-{a[i]}={a[j]-a[i]}")
print("###################################################")

#k<1 - negative k is allowed
a=[2,3,1,4]
a.sort()
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[j]-a[i]==k):
            print(f"{a[j]}-{a[i]}={a[j]-a[i]}")
print("###############################################################")


a=[2,3,1,4]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(abs(a[j]-a[i])==k):
            print(f"{a[j]}-{a[i]}={a[j]-a[i]}")

print("#########################################################")
'''
Two sum
2 numbers=i<j
'''

'''
3 sum
'''
nums=[-1,0,1,2,-1,-4]
a=[]
for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if(nums[i]+nums[j]+nums[k]==0):
                       temp = sorted([nums[i],nums[j],nums[k]])  # sort triplet
                    if temp not in a:   # avoid duplicate
                         a.append(temp)
print(a)
        