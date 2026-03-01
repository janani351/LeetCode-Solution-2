from typing import List, Optional
from heapq import heapify, heappop, heappush

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into one sorted linked list.
      
        Args:
            lists: List of head nodes of k sorted linked lists
          
        Returns:
            Head of the merged sorted linked list
        """
        # Add comparison method to ListNode for heap operations
        # This allows heap to compare ListNode objects by their values
        setattr(ListNode, "__lt__", lambda self, other: self.val < other.val)
      
        # Initialize priority queue with all non-null head nodes
        priority_queue = [head for head in lists if head]
      
        # Convert list into a min-heap based on node values
        heapify(priority_queue)
      
        # Create dummy node to simplify list construction
        dummy_head = ListNode()
        current_node = dummy_head
      
        # Process nodes from heap until empty
        while priority_queue:
            # Extract node with minimum value
            min_node = heappop(priority_queue)
          
            # If extracted node has a next node, add it to heap
            if min_node.next:
                heappush(priority_queue, min_node.next)
          
            # Append the minimum node to result list
            current_node.next = min_node
            current_node = current_node.next
      
        # Return the head of merged list (skip dummy node)
        return dummy_head.next
