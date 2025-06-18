class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_=len(nums1)+len(nums2)
        main=[]
        i=0
        j=0

        while i<(len(nums1)) and j<(len(nums2)):
            print("active")

            
            

            if len(nums1)==0:
                main = nums2
                j=len(nums2)
                break
            elif len(nums2)==0:
                main = nums1
                i=len(nums1)
                break
            if nums1[i]>nums2[j]:
                main.append(nums2[j])
                j+=1
            elif nums1[i]<nums2[j]:
                main.append(nums1[i])
                i+=1
            elif nums1[i]==nums2[j]:
                main.append(nums2[j])
                main.append(nums1[i])
                i+=1
                j+=1
            
        if i!=len(nums1):
            for k in nums1[i:len(nums1)]:
                main.append(k)
        elif j!= len(nums2):
            for k in nums2[j:len(nums2)]:
                main.append(k)
        

        mid=len_/2
        

        if mid.is_integer():
            return (main[int(mid)-1]+main[int(mid+1)-1])/2

        else:
            if int(mid)==0:
                return main[0]
            else:    
                return main[int(mid)]






#Not the most efficient solution