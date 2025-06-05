# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1=list1
        head2=list2

        if head1==None and head2==None:
            return None

        elif head1==None:
            head=ListNode(head2.val)
            head2=head2.next
        elif head2==None:
            head=ListNode(head1.val)
            head1=head1.next

            
        elif head1.val>head2.val:
            head=ListNode(head2.val)
            head2=head2.next
        else:
            head=ListNode(head1.val)
            head1=head1.next


        current=head 
        while head1!=None and head2!=None:

            if head1.val>head2.val:
                current.next=head2
                head2=head2.next
                current=current.next
            elif head1.val<head2.val:
                current.next=head1
                head1=head1.next
                current=current.next
            else:
                current.next=head1
                head1=head1.next
                current=current.next

                current.next=head2
                head2=head2.next
                current=current.next


        if head1==None and head2==None:
            pass
        elif head2==None:
            current.next=head1
        elif head1==None:
            current.next=head2

        return head


                    