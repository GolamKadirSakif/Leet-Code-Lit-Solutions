
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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

            
            ml=sorted(ml)
            x=self.list_to_linked_list(ml)
            return x