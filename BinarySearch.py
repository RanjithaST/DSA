#Binary search: works only on sorted array
#works on 2 pointers and array must be sorted whenever we take 2 pointers
'''
[a b c d e f g h i j k l m n o p]
 l++                           r--
 array is strictly incrasing and find a[l]+a[r]==target
 if a[l]+a[r]>target: then decrement right,if we increment left again it becomes more than target
 l pointer -> l++ :sum increases
 r pointer -> r-- :sum decreases
 a[l]+a[r]<target: increment left pointer.
 a[l]+a[r]>target: decrement right pointer.
 until(l<r) we need to increment and decrease
'''

numbers=[10,20,30,40,60] #[2,4]
target=60
a=[0,0]
i=0
j=len(numbers)-1
while(i<j):
    if(numbers[i]+numbers[j]==target):
        a[0]=i+1
        a[1]=j+1
        break
    elif(numbers[i]+numbers[j]>target):
        j=j-1
    else: 
        i=i+1
print(a)

                
'''
1.Hashmap:
Used for,
1.duplicates
2.occurances
3.sub array sum
4.unsorted arrays

2.Two pointers
Used for,
1.Sorted arrays
2.Triplet sum
3.search in sorted array

2pointers + binary search + hashmap = 60% of problems
'''

'''
Happy no:
2*2=4
4*4=16
1+36=37
9+49=58
25+64=89
.
.
.
2*2=4

If the previous sum repeats then that will be end and return false as that particular sequence never generate 1
'''
'''
Example 1:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false
'''
'''
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        h=set()
        while(n!=1):
            sum=0
            while(n!=0): #run while loop until we didnt gt 1
                x=n%10
                n=n//10
                sum=sum+(x*x)
            if sum in h:
                return False
            else:
                h.add(sum)
            n=sum
        return True 
'''
