class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        points = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    points.append([i, j])

        for point in points:
            for i in range(len(matrix)):
                matrix[i][point[1]] = 0
            for i in range(len(matrix[0])):
                matrix[point[0]][i] = 0