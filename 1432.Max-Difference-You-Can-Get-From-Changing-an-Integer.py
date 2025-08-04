class Solution:
    def maxDiff(self, nums):

        
        max_=nums
        min=nums
        num = [int(digit) for digit in str(nums)]
        n=[]
        for p in num:
            if p not in n:
                n.append(p)


    
        for x in n:
                for y in [0,1,9]:
                    num = [int(digit) for digit in str(nums)]
                    for i in range(len(num)):
                        if num[i]==x:
                            num[i]=y

                    if num[0]!=0:
                        num=int("".join(map(str, num)))
                        if num>max_:
                            max_=num

                        elif num<min:
                            min=num

        return max_-min

        