class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
      
        # dp[i][j][char_idx] = number of distinct palindromic subsequences 
        # in s[i:j+1] that start and end with character at index char_idx
        # where char_idx: 0='a', 1='b', 2='c', 3='d'
        dp = [[[0] * 4 for _ in range(n)] for _ in range(n)]
      
        # Base case: single characters are palindromes
        for i, char in enumerate(s):
            char_index = ord(char) - ord('a')
            dp[i][i][char_index] = 1
      
        # Process substrings of increasing length
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
              
                # Try each possible character as start/end of palindrome
                for char in 'abcd':
                    char_index = ord(char) - ord('a')
                  
                    if s[start] == s[end] == char:
                        # Both ends match the current character
                        # Count: empty string + single char + all palindromes from inner substring
                        dp[start][end][char_index] = 2 + sum(dp[start + 1][end - 1])
                    elif s[start] == char:
                        # Only start matches - exclude the end character
                        dp[start][end][char_index] = dp[start][end - 1][char_index]
                    elif s[end] == char:
                        # Only end matches - exclude the start character
                        dp[start][end][char_index] = dp[start + 1][end][char_index]
                    else:
                        # Neither end matches - look at inner substring
                        dp[start][end][char_index] = dp[start + 1][end - 1][char_index]
      
        # Return total count of distinct palindromic subsequences
        return sum(dp[0][n - 1]) % MOD
