class Solution(object):
    def deleteDuplicates(self, head):
        curr = head
        while curr and curr.next:
            rear = curr
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            rear.next = curr.next
            curr = curr.next
        return head
