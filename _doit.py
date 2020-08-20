class Solution:
    def updateMatrix(self, matrix):
        queue = []
        # distance = [([0] * (len(matrix[0]))) * len(matrix)]
        distance = [[] for i in range(len(matrix))]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def value_at(p):
            return matrix[p[0]][p[1]]

        def is_valid(p):
            return 0 <= p[0] < len(matrix) and 0 <= p[1] < len(matrix[0])

        def set_distance_at(p, d):
            distance[p[0]][p[1]] = d

        def distance_at(p):
            return distance[p[0]][p[1]]

        for i in range(len(matrix)):
            distance[i] = [0 for j in range(len(matrix[0]))]
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    queue.append((i, j))
                    distance[i][j] = None
                else:
                    distance[i][j] = 0

        while len(queue) != 0:
            size = len(queue)
            for i in range(size):
                this_point = queue.pop(0)
                good_to_go = False

                for d in directions:
                    next_point = (this_point[0] + d[0], this_point[1] + d[1])

                    if is_valid(next_point):
                        if value_at(next_point) == 0:
                            set_distance_at(this_point, 1)
                            good_to_go = True
                            break
                        else:  # value = 1
                            if distance_at(next_point) != None:
                                if distance_at(this_point) == None:
                                    set_distance_at(
                                        this_point, distance_at(next_point) + 1)
                                    good_to_go = True
                                else:
                                    set_distance_at(this_point, min(distance_at(
                                        this_point), distance_at(next_point) + 1))
                                    good_to_go = True

                if not good_to_go:
                    queue.append(this_point)

        return distance

# ---------------------------------------------------------------------


def print_matrix(m):
    for i in m:
        print(i)

    print()


# s = Solution().updateMatrix([[0, 0, 0],
#                              [0, 1, 0],
#                              [0, 0, 0]])
# print(s)

# s = Solution().updateMatrix([[0, 0, 0],
#                              [0, 1, 0],
#                              [1, 1, 1]])
# print(s)

matrix = [[1, 1, 0, 0, 1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0], [
    1, 1, 1, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], [0, 1, 0, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]]

expected = [[2, 1, 0, 0, 1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 0, 1, 1, 2, 2, 1], [1, 1, 1, 0, 0, 1, 2, 2, 1, 0], [0, 1, 2, 1, 0, 1, 2, 3, 2, 1], [0, 0, 1, 2, 1, 2, 1, 2, 1, 0], [
    1, 1, 2, 3, 2, 1, 0, 1, 1, 1], [0, 1, 2, 3, 2, 1, 1, 0, 0, 1], [1, 2, 1, 2, 1, 0, 0, 1, 1, 2], [0, 1, 0, 1, 1, 0, 1, 2, 2, 3], [1, 2, 1, 0, 1, 0, 1, 2, 3, 4]]
print_matrix(matrix)
s = Solution().updateMatrix(matrix)
print_matrix(s)
print_matrix(expected)
