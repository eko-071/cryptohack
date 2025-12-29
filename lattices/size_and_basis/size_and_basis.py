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

def size(u):
    return sqrt(dot_product(u, u))

def unit_vector(v):
    return scalar_product(1/size(v), v)

v = (4,6,2,5)
print(size(v))
