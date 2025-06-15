class Solution(object):
    def minMaxDifference(self, nums):
        """
        :type num: int
        :rtype: int
        """
        num = [int(digit) for digit in str(nums)]
        visited=[]
        maxu=num.copy()
        minu=num.copy()

        for j in range(len(num)):

            if num[j] not in visited:
                max=num.copy()
                min=num.copy()

                visited.append(num[j])

                for i in range(j,len(num)):

                    if num[i] == num[j]:

                        max[i]=9
                        min[i]=0

                if max>maxu:
                    maxu=max
                if min<minu:
                    minu=min

        maxu=int("".join(map(str, maxu)))
        minu=int("".join(map(str, minu)))

        return maxu-minu