from typing import List


def dfs(grid, i, j, rows, cols):
   """
    i (int): Current row index
    j (int): Current column index 
    rows (int): Number of rows in grid
    cols (int): Number of columns in grid
   """
   if (i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0):
       return
       
   grid[i][j] = 0  # marking as visited
   
   # 4 directions
   dfs(grid, i+1, j, rows, cols)  # Down
   dfs(grid, i-1, j, rows, cols)  # Up
   dfs(grid, i, j+1, rows, cols)  # Right
   dfs(grid, i, j-1, rows, cols)  # Left



def count_islands(grid: List[List[int]], dim: list) -> int:
   """count number of islands"""
   if not grid:
       return 0
       
   rows, cols = dim
   islands = 0
   
   for i in range(rows):
       for j in range(cols):
           if grid[i][j] == 1:
               islands += 1
               dfs(grid, i, j, rows, cols)
               
   return islands