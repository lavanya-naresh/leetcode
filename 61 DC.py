from typing import Optional, Tuple
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 0:
            return head
        
        length, lastNode = self.getLength(head)
        nodesToRotate = k % length
        nodesToSkip = length - nodesToRotate
        
        lastNode.next = head
        newTail, newHead = self.traverseNodesFromHead(head, nodesToSkip)
        newTail.next = None
        return newHead

    def getLength(self, head) -> Tuple[int, ListNode]:
        
        count, currNode, prevNode = 0, head, ListNode(0, None)
        while currNode:
            prevNode = currNode
            currNode = currNode.next
            count += 1
        
        return (count, prevNode)
    
    def traverseNodesFromHead(self, head, count) -> Tuple[ListNode, ListNode]:
        
        prevNode, currNode = ListNode(0, None), head
        for i in range(count):
            prevNode = currNode
            currNode = currNode.next
        return (prevNode, currNode)