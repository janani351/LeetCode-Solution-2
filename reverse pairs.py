class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
        Count reverse pairs where i < j and nums[i] > 2 * nums[j]
        using modified merge sort algorithm.
      
        Args:
            nums: List of integers
          
        Returns:
            Count of reverse pairs
        """
      
        def merge_sort_and_count(left: int, right: int) -> int:
            """
            Recursively divide array and count reverse pairs during merge.
          
            Args:
                left: Left boundary index (inclusive)
                right: Right boundary index (inclusive)
              
            Returns:
                Count of reverse pairs in range [left, right]
            """
            # Base case: single element or invalid range
            if left >= right:
                return 0
          
            # Divide the array into two halves
            mid = (left + right) // 2
          
            # Recursively count pairs in left half, right half, and across halves
            count = merge_sort_and_count(left, mid) + merge_sort_and_count(mid + 1, right)
          
            # Count reverse pairs across the two sorted halves
            # For each element in left half, count elements in right half
            # where nums[i] > 2 * nums[j]
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= 2 * nums[j]:
                    i += 1
                else:
                    # All elements from i to mid satisfy the condition
                    # with current nums[j]
                    count += mid - i + 1
                    j += 1
          
            # Merge the two sorted halves
            temp = []
            i, j = left, mid + 1
          
            # Merge elements in sorted order
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
          
            # Add remaining elements from left half
            temp.extend(nums[i:mid + 1])
          
            # Add remaining elements from right half
            temp.extend(nums[j:right + 1])
          
            # Copy sorted elements back to original array
            nums[left:right + 1] = temp
          
            return count
      
        # Start merge sort from entire array
        return merge_sort_and_count(0, len(nums) - 1)
