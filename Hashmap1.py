'''
Docstring for Hashmap1
hashmap-<key,value>
key follows set data structure - unordered,no duplicated allowed
values will be linked to corresponding key and duplication is allowed
'''
#Optimization of insertion and accessing elements using hashmap
'''
Using 1 loop we perform both operation and insertion
O(n)
'''
'''
287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
'''
#Not optimized - Time Limit Exceeded ncz of 2 loops -O(n^2)
'''
i=1,i<=100,i++
    for j=1.j<=100,j++
when i=1, j runs 100 times
when i=2, j runs 100 times
....
when i=100, j runs 100 times
Total i=100*j=100=10000 times-this is avg
'''
nums = [1,3,4,2,2]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]==nums[j]):
             print(nums[i])

'''
Optimization:
Observation:
In ans if they tell to ask no of time its repeating  then we need to use hashmap
But if they ask only name of the repeating value then we can use set as we only require key

Approach:
nums=[1,2,3,2,4]
To print value-for each = for i in nums:
To print index also then-for loop(range())= for i in range(len(nums))
'''

nums=[1,2,3,1,4]
h={}
for i in nums:
    #was it present in if
    #1 is already present so print 1
    if(i in h.keys()):
        print(i)
    #else new element
    else:
        h[i]=0 #{1:0,2:0,3:0} 

#If interviewer ask why using hashmap if value if not at all used.so we can do using list if focus is only on duplicate
        nums=[1,2,1,3,3]
        a=[]
        for i in nums:
            if(i in a): #calculation
                print(i)
            else:#insertion
                a.append(i)

#If we need only keys and dont need values then we can use set{]}
#Hashmap and set takes same complexity so use hashmap