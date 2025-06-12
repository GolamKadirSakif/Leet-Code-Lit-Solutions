class Solution(object):
    def firstMissingPositive(self, nums):
        

       
        if len(nums)>10**5 or len(nums)<1:
            return None
        
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]>nums[j]:
                    x=nums[i]
                    nums[i]=nums[j]
                    nums[j]=x
        
       


        

        max_int=nums[len(nums)-1]
        

        
        val=None
        for i in range(1, max_int+1):
            if i in nums:
                pass
            else:
                val=i
                break

            
        if val==None:
            return max_int+1

        else:
            return val