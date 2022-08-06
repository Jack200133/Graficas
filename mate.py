from math import sqrt


def producto_matrices(a, b):
    filas_a = len(a)
    filas_b = len(b)
    columnas_a = len(a[0])
    columnas_b = len(b[0])
    if columnas_a != filas_b:
        return None
    # Asignar espacio al producto. Es decir, rellenar con "espacios vacíos"
    producto = []
    for i in range(filas_b):
        producto.append([])
        for j in range(columnas_b):
            producto[i].append(None)
    # Rellenar el producto
    for c in range(columnas_b):
        for i in range(filas_a):
            suma = 0
            for j in range(columnas_a):
                suma += a[i][j]*b[j][c]
            producto[i][c] = suma
    return producto


def producto_matriz_vector(a, b):
    filas_a = len(a)
    columnas_a = len(a[0])
    if columnas_a != len(b):
        return None
    producto = []
    for i in range(filas_a):
        suma = 0
        for j in range(columnas_a):
            suma += a[i][j]*b[j]
        producto.append(suma)
    return producto


def producto_cruz(a, b):
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]


def resta_vectores(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]


def normal_vector3(a):
    return [a[0]/sqrt(a[0]**2 + a[1]**2 + a[2]**2),
            a[1]/sqrt(a[0]**2 + a[1]**2 + a[2]**2),
            a[2]/sqrt(a[0]**2 + a[1]**2 + a[2]**2)]


def producto_punto(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]


def inversa(a):
    for i in range(len(a)):
        a[i] = -a[i]
    return a
