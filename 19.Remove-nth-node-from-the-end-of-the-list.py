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

        head=head
        current=head
        while current!=None:
            print(current.val)
            current=current.next

        if n==1 and k==1:
            return None
        else:
            return head

        


            

    def list_to_linked_list(self, lst):
            if not lst: #Safety
                return None
            head = ListNode(lst[0])  # Create first node
            current = head
            for value in lst[1:]:
                current.next = ListNode(value)  # Append next node
                current = current.next
            return head



            
l1 = [1,2]
l2 = [5,6,4]
x=Solution()
ll=x.list_to_linked_list(l1)
print(x.removeNthFromEnd(ll,2))