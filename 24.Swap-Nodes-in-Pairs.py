# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):

        current=head
        prev=None
        prev_prev=None
        
        flag=0

        while current!=None:

            if flag==0:
                flag=1
                prev=current
                
                current=current.next
             
            else:
                flag=0
                if prev!=head:
                    prev.next=current.next#ok

                    
                    current.next=prev
                    prev_prev.next=current
                    prev_prev=prev
                    
                    if prev.next!=None:

                        current=prev.next #ok
                    else:

                        current=None
                else:
                    head=current
                    prev.next=current.next#ok
                    current.next=prev
                    prev_prev=prev
                    
                    
                    if prev.next!=None:

                        current=prev.next #ok
                    else:

                        current=None


        
        return head