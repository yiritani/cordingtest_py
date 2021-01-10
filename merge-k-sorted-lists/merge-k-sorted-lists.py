
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = ListNode(None)

    def mergeKLists(self, lists) :
        tmp = self.head.next
        while tmp:
            print(tmp.val)
            tmp = tmp.next

if __name__ == '__main__':
    s = Solution()
    l = ListNode
    l = [[1,4,5],[1,3,4],[2,6]]

    print(s.mergeKLists(l))
