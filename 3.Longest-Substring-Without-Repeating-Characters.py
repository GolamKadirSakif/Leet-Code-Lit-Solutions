from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        queue=deque()
        max_size=0
        size=0

        if len(s)==0:
            return 0

        

        for i in s:
            
            if i in queue:

                if size>max_size:
                    max_size=size

                while True:
                    item=queue.popleft()
                    size-=1
                    if item==i:
                        break
                queue.append(i)
                size+=1

            else:

                queue.append(i)
                size+=1
        if size>max_size:
            return size
        return max_size


#Explanation: 
#Two Varaiables size and max_size
#And a queue
#For loop iterating through the string
#And inserting it in the queue 
#If an element is already present in the queue
#Elemts are dequeued, Not all elements of the queue
# Only till the repeated element
#Example:
#Queue:{abcdefgh} here let's say the repeated elemenmt is "d"
#ony "abcd" will be dequeued in the while loop
#Updated Queue: {efgh}
#Every time an element is added to the queue --> size+=1
#And everytime a repeated character is found max_size is updated to size, only if size is greater than max_size
#After dequeuing, the repeated character is inserted in the queue and the size is again updated +=1
#If no elemnt is repeated the size is returned