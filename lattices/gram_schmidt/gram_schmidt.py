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

def gram_schmidt(v):
    n = len(v)
    u = [None]*n
    u[0] = v[0][:]

    for i in range(1, n):
        u[i] = v[i][:]
        subtract = [0]*len(u[i])
        for j in range(i):
            projection = dot_product(v[i], u[j])/dot_product(u[j], u[j])
            subtract = vector_add(subtract, scalar_product(projection, u[j]))
        u[i] = vector_subtract(u[i], subtract)

    return [unit_vector(x) for x in u]

v = [[4,1,3,-1], [2,1,-3,4], [1,0,-2,7], [6,2,9,-5]]

u = gram_schmidt(v)
for x in u:
    print(x)