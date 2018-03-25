from collections import deque

class Node():
    def __init__(self, row, col, path=None):
        self.row = row
        self.col = col
        if not path:
            self.path = []
        else:
            self.path = path
# O(len(grid[0]) * len(grid)) or O(rows * cols)
def find_path(grid):
    start = Node(0,0)
    dim_rows = len(grid) - 1
    dim_cols = len(grid[0]) - 1
    end = Node(dim_rows, dim_cols)
    queue = deque()
    queue.append(start)

    while queue:
        current_node = queue.pop()
        if current_node.row == end.row and current_node.col == end.col:
            current_node.path.append((current_node.row, current_node.col))
            return current_node.path

        if current_node.row + 1 <= dim_rows and grid[current_node.row + 1][current_node.col] != 1:
            new_node = Node(current_node.row + 1, current_node.col, current_node.path)
            new_node.path.append((current_node.row, current_node.col))
            queue.appendleft(new_node)

        if current_node.col + 1 <= dim_cols and grid[current_node.row][current_node.col + 1] != 1:
            new_node = Node(current_node.row, current_node.col + 1, current_node.path)
            new_node.path.append((current_node.row, current_node.col))
            queue.appendleft(new_node)

    return False

# O(len(grid[0]) * len(grid)) or O(rows * cols)
def find_path_recursive(grid):
    start = Node(0,0)
    dim_rows = len(grid) - 1
    dim_cols = len(grid[0]) - 1
    end = Node(dim_rows, dim_cols)
    return find_path_rec(grid, start, end)

def find_path_rec(grid, start_node, end_node):
    if start_node.row == end_node.row and start_node.col == end_node.col:
        start_node.path.append((end_node.row, end_node.col))
        return start_node.path
    else:
        if start_node.row + 1 <= end_node.row and grid[start_node.row + 1][start_node.col] != 1:
            new_node = Node(start_node.row + 1, start_node.col, start_node.path)
            new_node.path.append((start_node.row, start_node.col))
            return find_path_rec(grid, new_node, end_node)

        if start_node.col + 1 <= end_node.col and grid[start_node.row][start_node.col + 1] != 1:
            new_node = Node(start_node.row, start_node.col + 1, start_node.path)
            new_node.path.append((start_node.row, start_node.col))
            return find_path_rec(grid, new_node, end_node)
