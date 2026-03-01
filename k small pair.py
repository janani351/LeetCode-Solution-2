class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count_pairs_with_distance_at_most(max_distance):
            """
            Count the number of pairs with distance <= max_distance.
            For each element, find how many elements before it have
            distance <= max_distance from it.
            """
            pair_count = 0

            # For each element at position i
            for i, current_num in enumerate(nums):
                # Find the smallest element that satisfies:
                # current_num - element <= max_distance
                # which means: element >= current_num - max_distance
                min_valid_value = current_num - max_distance

                # Binary search for the leftmost position where
                # nums[j] >= min_valid_value in range [0, i)
                left_bound_index = bisect_left(nums, min_valid_value, 0, i)

                # All elements from left_bound_index to i-1 form valid pairs with current_num
                pair_count += i - left_bound_index

            return pair_count

        # Sort the array to enable binary search
        nums.sort()

        # Binary search on the answer space [0, max_difference]
        # Find the smallest distance where count_pairs_with_distance_at_most(distance) >= k
        # Using the template: feasible(mid) = count >= k
        left, right = 0, nums[-1] - nums[0]
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2

            if count_pairs_with_distance_at_most(mid) >= k:
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return first_true_index
