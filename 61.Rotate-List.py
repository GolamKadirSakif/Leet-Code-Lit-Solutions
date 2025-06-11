import numpy as np
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def list_to_linked_list(arr):
        """Convert a NumPy array (or list) into a linked list."""
        if arr is None or len(arr) == 0:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        if head==None:
            return None
        l=0
        current=head
        while current!=None:
            l+=1
            current=current.next

        if l==1:
            return head


  

        for i in range(k%l):
            
            current=head
            g=1
            s_l=None

            while current!=None:
                if g==l-1:#second last
                    s_l=current
                elif g==l: #last
                    s_l.next=None
                    current.next=head
                    head=current
                    break


                current=current.next
                g+=1
            

        return head

    

 
        
def list_to_linked_list(arr):
    """Convert a NumPy array (or list) into a linked list."""
    if arr is None or len(arr) == 0:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head



lst = [1,2,3]
linked_list_heads = list_to_linked_list(lst)



x=Solution()
z=x.rotateRight(linked_list_heads,2)

current=z
while current!=None:
    print(current.val)
    current=current.next