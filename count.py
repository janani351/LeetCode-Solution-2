from typing import List


class BinaryIndexedTree:
    """
    Binary Indexed Tree (Fenwick Tree) for efficient prefix sum queries and updates.
    Supports O(log n) updates and range sum queries.
    """
  
    def __init__(self, n: int) -> None:
        """
        Initialize a Binary Indexed Tree with size n.
      
        Args:
            n: The size of the tree (1-indexed)
        """
        self.size = n
        self.tree = [0] * (n + 1)  # 1-indexed array for BIT
  
    @staticmethod
    def lowbit(x: int) -> int:
        """
        Get the lowest set bit of x using bit manipulation.
        This determines the range of responsibility for each node.
      
        Args:
            x: The input number
          
        Returns:
            The value of the lowest set bit
        """
        return x & -x
  
    def update(self, index: int, delta: int) -> None:
        """
        Add delta to the element at position index.
        Updates all affected nodes in the tree.
      
        Args:
            index: The position to update (1-indexed)
            delta: The value to add
        """
        while index <= self.size:
            self.tree[index] += delta
            index += BinaryIndexedTree.lowbit(index)
  
    def query(self, index: int) -> int:
        """
        Calculate the prefix sum from position 1 to index.
      
        Args:
            index: The end position of the prefix sum (1-indexed)
          
        Returns:
            The sum of elements from position 1 to index
        """
        prefix_sum = 0
        while index > 0:
            prefix_sum += self.tree[index]
            index -= BinaryIndexedTree.lowbit(index)
        return prefix_sum


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        Count the number of smaller elements to the right of each element.
      
        Uses coordinate compression and a Binary Indexed Tree to efficiently
        count inversions while processing the array from right to left.
      
        Args:
            nums: List of integers
          
        Returns:
            List where result[i] is the count of smaller elements after nums[i]
        """
        # Step 1: Coordinate compression - map values to ranks
        # Sort unique values and create a mapping to compressed indices
        unique_sorted_values = sorted(set(nums))
        value_to_rank = {value: rank for rank, value in enumerate(unique_sorted_values, 1)}
      
        # Step 2: Initialize Binary Indexed Tree with compressed range
        fenwick_tree = BinaryIndexedTree(len(value_to_rank))
      
        # Step 3: Process array from right to left
        result = []
        for value in reversed(nums):
            # Get the compressed rank of current value
            rank = value_to_rank[value]
          
            # Update the tree to mark this value as seen
            fenwick_tree.update(rank, 1)
          
            # Query how many values smaller than current value we've seen
            # (rank - 1) gives us all ranks strictly less than current rank
            smaller_count = fenwick_tree.query(rank - 1)
            result.append(smaller_count)
      
        # Step 4: Reverse result since we processed array backwards
        return result[::-1]
