def get_minor_matrix(matrix, i, j):
    return [row[:j] + row[j+1:] for row in matrix[:i]+matrix[i+1:]]

def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    result = 0
    for c in range(len(matrix)):
        result += pow(-1, c)*matrix[0][c]*determinant(get_minor_matrix(matrix, 0, c))
    return result

def volume(basis):
    return abs(determinant(basis))

matrix = [[6, 2, -3], [5, 1, 4], [2, 7, 1]]
print(volume(matrix))