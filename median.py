class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of two sorted arrays.

        Args:
            nums1: First sorted array
            nums2: Second sorted array

        Returns:
            The median value of the combined sorted arrays
        """

        def find_kth_element(index1: int, index2: int, k: int) -> int:
            """
            Find the k-th smallest element in the union of nums1[index1:] and nums2[index2:].
            Uses binary search by eliminating k/2 elements at each step.

            Args:
                index1: Starting index in nums1
                index2: Starting index in nums2
                k: The k-th element to find (1-indexed)

            Returns:
                The k-th smallest element
            """
            # Base case: if nums1 is exhausted, return from nums2
            if index1 >= len_nums1:
                return nums2[index2 + k - 1]

            # Base case: if nums2 is exhausted, return from nums1
            if index2 >= len_nums2:
                return nums1[index1 + k - 1]

            # Base case: if k is 1, return the minimum of current elements
            if k == 1:
                return min(nums1[index1], nums2[index2])

            # Binary search: compare elements at position k/2 - 1 from current indices
            half_k = k // 2

            # Get the element at position (index + k/2 - 1) or infinity if out of bounds
            nums1_mid_value = nums1[index1 + half_k - 1] if index1 + half_k - 1 < len_nums1 else float('inf')
            nums2_mid_value = nums2[index2 + half_k - 1] if index2 + half_k - 1 < len_nums2 else float('inf')

            # Eliminate the smaller half and recursively find the (k - k/2)-th element
            if nums1_mid_value < nums2_mid_value:
                # Eliminate first half_k elements from nums1
                return find_kth_element(index1 + half_k, index2, k - half_k)
            else:
                # Eliminate first half_k elements from nums2
                return find_kth_element(index1, index2 + half_k, k - half_k)

        # Store array lengths
        len_nums1, len_nums2 = len(nums1), len(nums2)
        total_length = len_nums1 + len_nums2

        # For odd total length: find the middle element
        # For even total length: find the two middle elements and average them
        # Using (total + 1) / 2 and (total + 2) / 2 handles both cases elegantly
        left_median = find_kth_element(0, 0, (total_length + 1) // 2)
        right_median = find_kth_element(0, 0, (total_length + 2) // 2)

        # Return the average of the two middle values
        # For odd length, left_median == right_median
        return (left_median + right_median) / 2.0
