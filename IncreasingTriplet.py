#Increasing Triplet Subsequence
'''
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
1<2<3 - True

Two pointers + Unsorted array = Not works
 pre[1,1,1,1,1]#smallest value from 0 to last
 suf[5,5,5,5,5]#larget value from last to 0
'''
'''
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # first=float('inf')
        # second=float('inf')
        # for i in nums:
        #     if(i<=first):
        #         first=i
        #     elif(i<=second):
        #         second=i
        #     else:
        #         return True
        # return False
        
        if(len(nums)<3):
            return False
        pre=[0]*len(nums)
        pre[0]=nums[0]
        for i in range(1,len(nums)):
            pre[i]=min(nums[i],pre[i-1])
        suf=[0]*len(nums)
        suf[len(nums)-1]=nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            suf[i]=max(nums[i],suf[i+1]) 
        for i in range(1,len(nums)-1):
            if(pre[i-1]<nums[i] and nums[i]<suf[i+1]):
                return True
        return False
'''