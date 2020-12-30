
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        docking = []
        for i in lists:
            for j in i:
                docking.append(j)

        docking.sort()
        return docking

if __name__ == '__main__':
    l = Solution.mergeKLists("",[[1,4,5],[1,3,4],[2,6]])
    print(l)