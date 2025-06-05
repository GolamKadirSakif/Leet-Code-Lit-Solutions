class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        i=0
        head=head
        prev=None
        current=head
        while current!=None:

            if i==n:
                prev.next=current.next
                current.next=None
                current=prev.next
            else:
                prev=current
                current=current.next

            i+=1

        head=head
        current=head
        while current!=None:
            print(current.val)
            current=current.next


            

    def list_to_linked_list(self, lst):
            if not lst: #Safety
                return None
            head = ListNode(lst[0])  # Create first node
            current = head
            for value in lst[1:]:
                current.next = ListNode(value)  # Append next node
                current = current.next
            return head



            
l1 = [2,4,3]
l2 = [5,6,4]
x=Solution()
ll=x.list_to_linked_list(l1)
print(x.removeNthFromEnd(ll,1))