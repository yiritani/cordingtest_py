# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head=None) -> None:
        self.head = ListNode(None)

    def addTwoNumbers(self, l1, l2) :
        self.head = ListNode(l1)
        self.head.next = ListNode(l2)
        docking = []
        tmp = self.head
        while tmp:
            print(tmp.val)
            tmp = tmp.next

        return docking

if __name__ == '__main__':
    l1 = ListNode()
    l2 = ListNode()
    s = Solution()
    l1 = [2,4,3]
    l2 = [5,6,4]
    print(s.addTwoNumbers(l1, l2))

    # https://leetcode.com/problems/add-two-numbers/