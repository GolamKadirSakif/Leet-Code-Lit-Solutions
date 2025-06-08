import heapq
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def list_to_linked_list(self,lst):
            if not lst: #Safety
                return None
            head = ListNode(lst[0])  # Create first node
            current = head
            for value in lst[1:]:
                current.next = ListNode(value)  # create the next node and connect it to the current node
                current = current.next
            return head

    def mergeKLists(self, list):
            """
            :type lists: List[Optional[ListNode]]
            :rtype: Optional[ListNode]
            """
            ml=[]
            for i in list:
                head=i
                current=i
                while current!=None:
                    ml.append(current.val)
                    current=current.next

            
            heapq.heapify(ml)
            x=self.list_to_linked_list(ml)
            return x
    
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


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
linked_list_heads = [list_to_linked_list(lst) for lst in lists]

x=Solution()
x.mergeKLists(linked_list_heads)