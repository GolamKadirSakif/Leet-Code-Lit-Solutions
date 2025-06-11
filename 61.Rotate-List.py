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


        
        list_node=np.array([0]*l)

        i=0
        current=head
        while current!=None:
            
            list_node[i]=current.val
            i+=1
            current=current.next

        
        

        for p in range(k):
            temp=list_node[l-1]
            for g in range(l-2,-1,-1):
                list_node[g+1]=list_node[g]

            list_node[0]=temp
            






        


        

        head=list_to_linked_list(list_node)
        

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