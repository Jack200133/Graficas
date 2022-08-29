from math import sqrt,pow


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
    r = []
    for i in range(len(a)):
        r.append(a[i] - b[i])
    return r


def normal_vector3(a):
    try:
        return [a[0]/pow(a[0]**2 + a[1]**2 + a[2]**2,0.5),
                a[1]/pow(a[0]**2 + a[1]**2 + a[2]**2,0.5),
                a[2]/pow(a[0]**2 + a[1]**2 + a[2]**2,0.5)]
    except:
        return [0,0,0]


def producto_punto(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]


def inversa(a):
    result = []
    for i in range(len(a)):
        result.append(-a[i])
    return result


def invert_matrix(matrix):
    """
    Invert a matrix (adapted from http://www.mathsisfun.com/algebra/matrix-inverse.html)
    """
    n = len(matrix)
    inverted = []
    for i in range(n):
        inverted.append([])
        for j in range(n):
            inverted[i].append(0)
    for i in range(n):
        inverted[i][i] = 1
    for i in range(n):
        for j in range(n):
            if i != j:
                inverted[j][i] = -matrix[i][j]/matrix[i][i]
    return inverted

def nx2n(n_Rows, n_Columns):
    Zeros = []
    for i in range(n_Rows):
        Zeros.append([])
        for j in range(n_Columns*2):
            Zeros[i].append(0)
    return Zeros

# Applying matrix coefficients
def update(inputs, n_Rows, n_Columns, Zero):
    for i in range(n_Rows):
        for j in range(n_Columns):
            Zero[i][j] = inputs[i][j]
    return Zero

# Augmenting Identity Matrix of Order n
def identity(n_Rows, n_Columns, Matrix):
    for i in range(n_Rows):
        for j in range(n_Columns):
            if i == j:
                Matrix[i][j+n_Columns] = 1
    return Matrix

# Applying & implementing the GJE algorithm
def Gussain_Jordan_Elimination(n_Rows, n_Columns, Matrix):
    for i in range(n_Rows):
        if Matrix[i][i] == 0:
            print('error cannot divide by "0"')
    
        for j in range(n_Columns):
            if i != j:
                ratio = Matrix[j][i]/Matrix[i][i]

                for k in range(2*n_Columns):
                    Matrix[j][k] = Matrix[j][k] - ratio * Matrix[i][k]
    return Matrix

# Row Operation to make Principal Diagonal Element to '1'
def row_op(n_Rows, n_Columns, Matrix):
    for i in range(n_Rows):
        divide = Matrix[i][i]
        for j in range(2*n_Columns):
            Matrix[i][j] = Matrix[i][j]/divide
    return Matrix

# Display Inversed Matix
def getMatrixInverse(Matrix):
    returnable = []
    number_Rows = int(len(Matrix))
    number_Columns = int(len(Matrix[0]))
    Inversed_Matrix = (row_op(number_Rows, number_Columns, 
        Gussain_Jordan_Elimination(number_Rows, number_Columns, 
        identity(number_Rows, number_Columns, 
        update(Matrix, number_Rows, number_Columns, 
        nx2n(number_Rows, number_Columns))))))

    for i in range(number_Rows):
        returnable.append([])
        for j in range(number_Columns, 2*number_Columns):
            returnable[i].append(Inversed_Matrix[i][j])
    return returnable
