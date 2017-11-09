def find_path(food, grid):

    n = len(grid)

    def worker(cost, path):
        row, col = path[-1]
        if row == n - 1 and col == n - 1:
            # we reached the bottom right corner, exit now
            return cost, path

        possible_paths = []
        if row < n - 1:
            # we can go down
            cost_down = cost + grid[row+1][col]
            path_down = list(path)
            path_down.append((row+1, col))
            possible_paths.append(worker(cost_down, path_down))
        if col < n - 1:
            # we can go to the right
            cost_right = cost + grid[row][col+1]
            path_right = list(path)
            path_right.append((row, col+1))
            possible_paths.append(worker(cost_right, path_right))

        # a path is valid, if its cost is
        # less or equal to the food available
        valid_paths = [item for item in possible_paths
                       if item is not None
                       and item[0] <= food]

        if valid_paths:
            return max(valid_paths, key=lambda x: x[0])

        return None

    return worker(grid[0][0], [(0, 0)])

print(find_path(121, [[0, 2, 5],
                     [1, 1, 3],
                     [2, 1, 1]]))
# (11, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])

