class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Initialize tracking structures for rows, columns, and 3x3 sub-boxes
    # Create 9 empty sets for rows
        rows = []
        for i in range(9):
            rows.append(set())
        
        # Create 9 empty sets for columns
        cols = []
        for i in range(9):
            cols.append(set())
        
        # Create 9 empty sets for 3x3 boxes
        boxes = []
        for i in range(9):
            boxes.append(set())
        
        # Iterate through each cell in the board
        for r in range(9):
            for c in range(9):
                # Skip empty cells
                if board[r][c] == '.':
                    continue
                
                # Get the current value
                val = board[r][c]
                
                # Calculate which 3x3 box we're in
                box_idx = (r // 3) * 3 + (c // 3)
                
                # Check if this value already exists in current row, column, or box
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                
                # Add the value to our tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
        
        # If we've made it through the entire board without finding any violations
        return True

