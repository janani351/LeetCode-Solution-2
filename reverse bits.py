class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverse the bits of a 32-bit unsigned integer.
      
        Args:
            n: A 32-bit unsigned integer to reverse
          
        Returns:
            The integer with bits reversed
        """
        result = 0
      
        # Process all 32 bits
        for i in range(32):
            # Extract the least significant bit from n using AND operation
            # Shift it to its reversed position (31-i) and add to result using OR
            result |= (n & 1) << (31 - i)
          
            # Right shift n by 1 to process the next bit in the next iteration
            n >>= 1
          
        return result