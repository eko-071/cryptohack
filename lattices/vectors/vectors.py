from math import sqrt

def vector_add(u, v):
    if len(u) != len(v):
        print("Error! Vectors are not of the same dimension.")
        return None
    return [u[i] + v[i] for i in range(len(u))]

def vector_subtract(u, v):
    if len(u) != len(v):
        print("Error! Vectors are not of the same dimension.")
        return None
    return [u[i] - v[i] for i in range(len(u))]

def scalar_product(c, u):
    return [c * x for x in u]

def dot_product(u, v):
    if len(u) != len(v):
        print("Error! Vectors are not of the same dimension.")
        return None
    return sum(u[i]*v[i] for i in range(len(u)))

v = (2,6,3)
w = (1,0,0)
u = (7,7,2)

answer = 6 * dot_product(vector_subtract(scalar_product(2, v), w), u)
print(answer)