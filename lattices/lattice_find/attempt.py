from Crypto.Util.number import inverse, long_to_bytes

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

def decrypt(q, h, f, g, e):
    a = (f*e) % q
    m = (a*inverse(f, g)) % g
    return m

q = 7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257
h = 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800
e = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523

b1 = (q, 0)
b2 = (h, 1)

u1, u2 = gauss_algorithm(b1, b2)
# u1 is the SVP answer
g, f = u1

m = decrypt(q, h, f, g, e)

flag = long_to_bytes(m)
print(flag)
