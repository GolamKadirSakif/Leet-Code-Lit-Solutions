# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]

        """
        head=head
        current=head
        k=0
        while current!=None:
            k+=1
            current=current.next


        i=0
        head=head
        prev=head
        current=head
        
        while current!=None:

            if i==((k-n)) and i==0:
                head=current.next
                prev.next=current.next
                current.next=None
                
                current=prev.next

            elif i==((k-n)):
                
                prev.next=current.next
                current.next=None
                
                current=prev.next
            else:
                prev=current
                current=current.next

            i+=1

        

        
        return head
        


            

    
        