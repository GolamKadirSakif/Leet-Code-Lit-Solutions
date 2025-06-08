# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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
                prev_prev=current
                current=current.next
             
            else:
                flag=0
                if prev!=head:
                    prev.next=current.next#ok

                    
                    current.next=prev
                    prev_prev.next=current
                    
                    current=prev.next #ok

                else:
                    head=current
                    prev.next=current.next#ok
                    current.next=prev
                    
                    
                    if prev.next!=None:

                        current=prev.next #ok
                    else:

                        current=None


        
        return head
def list_to_linked_list(lst):
    """Convert a Python list into a linked list."""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


lst = [1,2,3,4]
linked_list_heads = list_to_linked_list(lst)

x=Solution()
z=x.swapPairs(linked_list_heads)

print(z.val)
print(z.next.val)
print(z.next.next.val)
