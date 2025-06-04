# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        


        arr1=""
        head1=l1
        while head1!=None:
            arr1=str(head1.val)+arr1
            head1=head1.next


        

        arr2=""
        head2=l2
        while head2!=None:
            arr2=str(head2.val)+arr2
            head2=head2.next
        
        val= int(arr1)+int(arr2)
        ans=[]
        val = list(str(val)[::-1])

        for i in val:
            ans.append(int(i))

        def list_to_linked_list(lst):
            if not lst: #Safety
                return None
            head = ListNode(lst[0])  # Create first node
            current = head
            for value in lst[1:]:
                current.next = ListNode(value)  # Append next node
                current = current.next
            return head

        # Instead of returning a list, return the head of the linked  to match the output format

        return list_to_linked_list(ans)


       




#Below is an Example 
#l1 & l2 is already provided as a linked list 
# this example will not generate a valid output in you local ide. Works Only in leetcode
l1 = [2,4,3]
l2 = [5,6,4]
x=Solution()
print(x.addTwoNumbers(l1,l2))