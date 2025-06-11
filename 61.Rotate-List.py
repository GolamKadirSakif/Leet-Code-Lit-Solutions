
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
        
        #Corner Case
        if head==None:
            return None



        l=0
        current=head
        last=None
        while current!=None:
            l+=1
            if current.next==None: #last node
                last=current
            current=current.next
        
            



        #Corner Case
        if l==1:
            return head


        #making a circular list
        last.next=head
  
        current=head
        for i in range((l-(k%l))):
            if i==((l-(k%l))-1):
                head=current.next
                current.next=None
                break
            current=current.next
            
            
            

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



lst = [1,2,3,4,5]
linked_list_heads = list_to_linked_list(lst)



x=Solution()
z=x.rotateRight(linked_list_heads,5)

current=z
while current!=None:
    print(current.val)
    current=current.next