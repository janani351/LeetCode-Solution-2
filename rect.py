class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        Determines if given rectangles form an exact cover of a rectangular region.
      
        The algorithm checks two conditions:
        1. Total area of all rectangles equals the area of the bounding rectangle
        2. Corner points appear with correct frequencies:
           - The 4 corners of the bounding rectangle appear exactly once
           - All other corners appear 2 or 4 times (shared by adjacent rectangles)
      
        Args:
            rectangles: List of rectangles, each as [x1, y1, x2, y2]
      
        Returns:
            True if rectangles form an exact cover, False otherwise
        """
        from collections import defaultdict
      
        # Initialize variables to track total area and bounding box
        total_area = 0
        min_x, min_y = rectangles[0][0], rectangles[0][1]
        max_x, max_y = rectangles[0][2], rectangles[0][3]
      
        # Dictionary to count occurrences of each corner point
        corner_count = defaultdict(int)
      
        # Process each rectangle
        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle
          
            # Add rectangle's area to total
            total_area += (x2 - x1) * (y2 - y1)
          
            # Update bounding box coordinates
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
          
            # Count occurrences of each corner of current rectangle
            corner_count[(x1, y1)] += 1  # Bottom-left corner
            corner_count[(x1, y2)] += 1  # Top-left corner
            corner_count[(x2, y2)] += 1  # Top-right corner
            corner_count[(x2, y1)] += 1  # Bottom-right corner
      
        # Check if total area matches bounding box area
        # and if the four corners of bounding box appear exactly once
        if (total_area != (max_x - min_x) * (max_y - min_y) or
            corner_count[(min_x, min_y)] != 1 or
            corner_count[(min_x, max_y)] != 1 or
            corner_count[(max_x, max_y)] != 1 or
            corner_count[(max_x, min_y)] != 1):
            return False
      
        # Remove the four outer corners from consideration
        del corner_count[(min_x, min_y)]
        del corner_count[(min_x, max_y)]
        del corner_count[(max_x, max_y)]
        del corner_count[(max_x, min_y)]
      
        # Check that all internal corners appear 2 or 4 times
        # 2 times: corner shared by 2 rectangles (edge point)
        # 4 times: corner shared by 4 rectangles (internal point)
        return all(count == 2 or count == 4 for count in corner_count.values())
