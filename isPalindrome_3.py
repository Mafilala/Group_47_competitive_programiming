class Solution:
    def isPalindrome(self, head):
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next
        return node_list == node_list[:: -1]
