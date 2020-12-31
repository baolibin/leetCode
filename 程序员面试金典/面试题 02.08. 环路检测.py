'''
面试题 02.08. 环路检测
题目参考网址：
https://leetcode-cn.com/problems/linked-list-cycle-lcci/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        dict1 = {}
        while head:
            if head in dict1:
                return head
            dict1[head] = 1
            head = head.next
        return head

# 快慢指针
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:  # 开始走位
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # 相遇
                break

        # 若无相会处，则无环路
        if not fast or not fast.next:
            return None
        # 若两者以相同的速度移动，则必然在环路起始处相遇
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
'''
# 快慢指针的解题思路
解题思路
1. 链表是否存在环路

检测链表中是否存在环路有一个方法叫做快慢指针法，即设置两个指针从起点同时出发，慢指针每移动一步快指针移动两步，如果存在环路则它们终究会相遇。

难道快指针不会“越过”慢指针吗？

不会。利用反证法，假设快指针真的 越过 了满指针，且快指针处于位置 i+1，而慢指针处于位置 i，那么在前一步，快指针处于位置 i-1，慢指针也处于位置 i-1，它们相遇了。

2. 何时相遇

首先，快指针会离慢指针越来越远；后来，经过环路后，快指针会开始 追赶 慢指针，假设这时两者相距 kk 步，那么每经过一个单位时间，快指针就离慢指针近了一步，因此该时刻起两者经过 kk 个单位时间之后相遇。

3. 如何找到环路起点

设相遇点为 nodenode，相遇点与环路起点的距离 kk = headhead 与环路起点的距离 kk。
用一个指针指向 headhead，另一个指针指点 nodenode，以同样的速度移动 kk 步之后，两者会指向环路起点。

算法
创建指针 fast 和 slow；
slow 每走一步， fast 走两步；
两者相遇时，将 slow 指针指向 head；
以同样的速度移动 fast 和 slow，再次相遇的结点即为所求结果。

'''