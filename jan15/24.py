class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while head and head.next:
            firstNode = head
            secondNode = head.next 

            prev.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode 

            prev = firstNode 
            head = firstNode.next 

        return dummy.next
    
# Time Complexity: O(n), where n is the number of nodes in the linked list

# Space Complexity: O(1), we are only using a couple variables, but no extra data structures

# Solution:
# First of all, because this is a linked list question, I would like to create a dummyNode first to keep track 
# of the new head that we would want to return later on after running our algorithm
# I also want to create a prev variable, that will keep track of the prev node we were on, which will initialized to None
# Afterwards, we want to iterate until the second to last node, as the last node will be swapped during that iteration.
# Now, we want to get the currentNode, as well the nextNode to be swapped.
# We see here that we want our currentNode's next pointer to point to the nextNextNode(i.e. nextNode.next) and the nextNode's 
# next pointer to point to our currentNode. We also want out prev node's next pointer to point to the nextNode, effectively swapping these two nodes.
# Afterwards, we can simply set prev to currentNode, and then set our currentNode to the nextNextNode(o.e. nextNode.next)
# Afterwards, just return dummy.next, as that will store the new head of our linked list.