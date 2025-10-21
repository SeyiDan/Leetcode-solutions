class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num =='.':
                    continue
                box_index = (row//3)* 3 + (col//3)
                
                if num in rows[row] or num in cols[col] or num in boxes[box_index]:
                    return False
                rows[row].add(num)
                cols[col].add(num)
                boxes[box_index].add(num)
        return True







































#  # THESE LINES ARE STILL NEEDED - sets are initialized here!
#     rows = [set() for _ in range(9)]
#     cols = [set() for _ in range(9)]
#     boxes = [set() for _ in range(9)]
    
#     # Then the compressed version:
#     for row in range(9):
#         for col in range(9):
#             num = board[row][col]
#             if num == '.':
#                 continue
                
#             box_index = (row // 3) * 3 + (col // 3)
            
#             # Check all three at once
#             if num in rows[row] or num in cols[col] or num in boxes[box_index]:
#                 return False
                
#             rows[row].add(num)  # .add() is a SET method!
#             cols[col].add(num)
#             boxes[box_index].add(num)
        
#         return True
