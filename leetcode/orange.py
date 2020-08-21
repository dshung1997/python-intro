class Solution:
    def orangesRotting(self, grid):
        queue = []
        visited = []
        result = 0
        fresh_orange = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] is 2:
                    queue.append([i, j])
                if grid[i][j] is 1:
                    fresh_orange += 1
        if fresh_orange is 0:
            return 0
        while len(queue) > 0:
            size = len(queue)
            flag = False
            while size > 0:
                size -= 1
                current_rotten = queue.pop(0)
                visited.append(current_rotten)
                if current_rotten[0] + 1 < len(grid):
                    new_rotten = [current_rotten[0] + 1, current_rotten[1]]
                    if new_rotten not in visited and grid[new_rotten[0]][new_rotten[1]] is 1:
                        flag = True
                        queue.append(new_rotten)
                        visited.append(new_rotten)
                        grid[new_rotten[0]][new_rotten[1]] = 2
                if current_rotten[0] - 1 >= 0:
                    new_rotten = [current_rotten[0] - 1, current_rotten[1]]
                    if new_rotten not in visited and grid[new_rotten[0]][new_rotten[1]] is 1:
                        flag = True
                        queue.append(new_rotten)
                        visited.append(new_rotten)
                        grid[new_rotten[0]][new_rotten[1]] = 2
                if current_rotten[1] - 1 >= 0:
                    new_rotten = [current_rotten[0], current_rotten[1] - 1]
                    if new_rotten not in visited and grid[new_rotten[0]][new_rotten[1]] is 1:
                        flag = True
                        queue.append(new_rotten)
                        visited.append(new_rotten)
                        grid[new_rotten[0]][new_rotten[1]] = 2
                if current_rotten[1] + 1 < len(grid[0]):
                    new_rotten = [current_rotten[0], current_rotten[1] + 1]
                    if new_rotten not in visited and grid[new_rotten[0]][new_rotten[1]] is 1:
                        flag = True
                        queue.append(new_rotten)
                        visited.append(new_rotten)
                        grid[new_rotten[0]][new_rotten[1]] = 2

            result += flag
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] is 1:
                    return -1
        return result


s = Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(s)
