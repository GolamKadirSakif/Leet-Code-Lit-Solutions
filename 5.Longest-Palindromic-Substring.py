def longestPalindrome(self, s):

        lps=""
        

        if len(s)==1:
            return s
        


        for i in range(len(s)):
            

            for j in range(i+1,len(s)):
                test=s[i:j+1]
                if test==test[::-1] and len(test)>len(lps):
       
                    lps=test    
            

        if len(lps)==0:
            return s[0]

        
        
        
        return lps

#One of the critical problem I solved, Taught me how to utilize memory space
#And That I am not dumb hehe 