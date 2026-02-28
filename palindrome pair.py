class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Create a dictionary mapping each word to its index for O(1) lookup
        word_to_index = {word: index for index, word in enumerate(words)}
        result = []
      
        # Check each word for potential palindrome pairs
        for current_index, current_word in enumerate(words):
            # Try splitting the current word at every possible position
            for split_pos in range(len(current_word) + 1):
                # Split current word into prefix and suffix
                prefix = current_word[:split_pos]
                suffix = current_word[split_pos:]
              
                # Get reversed versions of prefix and suffix
                reversed_prefix = prefix[::-1]
                reversed_suffix = suffix[::-1]
              
                # Case 1: If reversed_prefix exists in words and suffix is palindrome
                # Then current_word + words[reversed_prefix_index] forms a palindrome
                if reversed_prefix in word_to_index and word_to_index[reversed_prefix] != current_index and suffix == reversed_suffix:
                    result.append([current_index, word_to_index[reversed_prefix]])
              
                # Case 2: If reversed_suffix exists in words and prefix is palindrome
                # Then words[reversed_suffix_index] + current_word forms a palindrome
                # Note: split_pos > 0 prevents duplicate when both prefix and suffix are empty
                if split_pos > 0 and reversed_suffix in word_to_index and word_to_index[reversed_suffix] != current_index and prefix == reversed_prefix:
                    result.append([word_to_index[reversed_suffix], current_index])
      
        return result
