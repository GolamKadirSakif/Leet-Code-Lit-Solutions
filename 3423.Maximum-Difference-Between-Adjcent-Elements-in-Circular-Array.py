class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l=len(nums)
        max=0
        i=0
        j=1
        while i!=l:
            sum=nums[i]-nums[j]
            if sum<0:
                sum=sum*-1

            if sum>max:
                max=sum
            
            i+=1
            if j==l-1:
                j=0
            else:
                j+=1


        return max


        
        
        

#What I learned here is circular array is basically a regular array where if you hit the last index you just travel back to the first element 