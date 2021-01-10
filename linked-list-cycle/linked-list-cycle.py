
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False

        p1, p2 = head, head.next

        while p1 != p2:  # we automatically break if a cycle is found
            try:
                p1 = p1.next
                p2 = p2.next.next
            except:
                return False  # we will get an error thrown if no cycle exists

        return True


if __name__ == '__main__':
    head = [3, 2, 0, -4]
    s = ListNode(head)
    print(Solution.hasCycle("",s))
