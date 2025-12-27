def dot_product(u, v):
    if len(u) != len(v):
        print("Error! Vectors are not of the same dimension.")
        return None
    return sum(u[i]*v[i] for i in range(len(u)))

def scalar_product(c, u):
    return [c * x for x in u]

def vector_subtract(u, v):
    if len(u) != len(v):
        print("Error! Vectors are not of the same dimension.")
        return None
    return [u[i] - v[i] for i in range(len(u))]

def get_minor_matrix(matrix, i, j):
    return [row[:j] + row[j+1:] for row in matrix[:i]+matrix[i+1:]]

def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    result = 0
    for c in range(len(matrix)):
        result += pow(-1, c)*matrix[0][c]*determinant(get_minor_matrix(matrix, 0, c))
    return result

def gauss_algorithm(u, v):
    if dot_product(v, v) < dot_product(u, u):
        return gauss_algorithm(v, u)
    m = dot_product(u, v) // dot_product(u, u)
    if m == 0:
        return u, v
    v = vector_subtract(v, scalar_product(m, u))
    return gauss_algorithm(u, v)

v=(846835985,9834798552)
u=(87502093,123094980)

b1, b2 = gauss_algorithm(v, u)
print(dot_product(b1, b2))