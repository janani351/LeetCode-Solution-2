class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int) -> None:
            # Base case: all queens have been successfully placed
            if row == n:
                nonlocal solution_count
                solution_count += 1
                return
          
            # Try placing a queen in each column of the current row
            for col in range(n):
                # Calculate diagonal and anti-diagonal indices
                # Diagonal: row + col (constant along each diagonal)
                # Anti-diagonal: row - col + n (add n to ensure positive index)
                diagonal_idx = row + col
                anti_diagonal_idx = row - col + n
              
                # Check if current position conflicts with existing queens
                if columns_used[col] or diagonals_used[diagonal_idx] or anti_diagonals_used[anti_diagonal_idx]:
                    continue
              
                # Place the queen by marking column and diagonals as used
                columns_used[col] = True
                diagonals_used[diagonal_idx] = True
                anti_diagonals_used[anti_diagonal_idx] = True
              
                # Recursively place queens in the next row
                backtrack(row + 1)
              
                # Backtrack: remove the queen and unmark the positions
                columns_used[col] = False
                diagonals_used[diagonal_idx] = False
                anti_diagonals_used[anti_diagonal_idx] = False
      
        # Initialize tracking arrays for column and diagonal conflicts
        columns_used = [False] * n  # Track which columns have queens
        diagonals_used = [False] * (2 * n)  # Track main diagonals (row + col)
        anti_diagonals_used = [False] * (2 * n)  # Track anti-diagonals (row - col + n)
      
        # Counter for total number of valid solutions
        solution_count = 0
      
        # Start the backtracking from the first row
        backtrack(0)
      
        return solution_count
