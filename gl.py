import struct
import math
import random
from collections import namedtuple
from mate import producto_matrices, producto_matriz_vector
from obj import Obj

#V2 = namedtuple('Vertex2', ['x', 'y'])


def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))


def word(w):
    # 2 bytes
    return struct.pack('=h', w)


def dword(d):
    # 4 bytes
    return struct.pack('=i', d)


def color(r, g, b):
    return bytes([int(b*255), int(g*255), int(r*255)])


def bc(A, B, C, P):

    areaABC = (B[1] - C[1])*(A[0]-C[0]) + (C[0]-B[0])*(A[1]-C[1])

    areaPBC = (B[1]-C[1])*(P[0]-C[0]) + (C[0]-B[0])*(P[1]-C[1])

    areaPAC = (C[1]-A[1])*(P[0]-A[0]) + (A[0]-C[0])*(P[1]-A[1])

    u = areaPBC / areaABC
    v = areaPAC / areaABC
    w = 1 - u - v

    return u, v, w


class Renderer(object):
    def __init__(self):

        self.width = 4
        self.height = 4

        self.glViewPort(0, 0, 4, 4)

        self.clearColor = color(0, 0, 0)
        self.currentColor = color(1, 1, 1)
        self.glClear()

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glViewPort(0, 0, width, height)

    def glClearColor(self, r, g, b):
        self.clearColor = color(r, g, b)

    def glViewPort(self, x, y, width, height):
        self.mx_width = (x+width)
        self.mx_height = (y+height)
        self.min_width = x
        self.min_height = y

    def glColor(self, r, g, b):
        self.currentColor = color(r, g, b)

    def glPoint(self, x, y, crl=None):
        if(self.min_width <= x < self.mx_width) and (self.min_height <= y < self.mx_height):
            self.pixels[x][y] = crl or self.currentColor

    def glPoint_VP(self, ndcx, ndcy, crl=None):
        x = (ndcx+1) * ((self.mx_width-self.min_width)/2) + self.min_width
        y = (ndcy+1) * ((self.mx_height-self.min_height)/2) + self.min_height

        x = int(x)
        y = int(y)

        self.glPoint(x, y, crl)

    def glClear(self):
        self.pixels = [[self.clearColor for y in range(
            self.height)] for x in range(self.width)]

    def glLine(self, x0, y0, x1, y1, crl=None):
        dx = x1 - x0
        dy = y1 - y0

        if dx < 0:
            dx = -dx
            stepx = -1
        else:
            stepx = 1

        if dy < 0:
            dy = -dy
            stepy = -1
        else:
            stepy = 1

        dx2 = int(dx) << 1
        dy2 = int(dy) << 1

        if dx > dy:
            fraction = dy2 - dx
            while x0 != x1:
                self.glPoint(x0, y0, crl)
                if fraction >= 0:
                    y0 += stepy
                    fraction -= dx2
                x0 += stepx
                fraction += dy2
        else:
            fraction = dx2 - dy
            while y0 != y1:
                self.glPoint(x0, y0, crl)
                if fraction >= 0:
                    x0 += stepx
                    fraction -= dy2
                y0 += stepy
                fraction += dx2

    def glLineC(self, x0, y0, x1, y1, clr=None):
        # Bresenham line algorithm
        # y = m * x + b

        # Si el punto0 es igual al punto 1, dibujar solamente un punto
        if x0 == x1 and y0 == y1:
            self.glPoint(x0, y0, clr)
            return

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx

        # Si la linea tiene pendiente mayor a 1 o menor a -1
        # intercambio las x por las y, y se dibuja la linea
        # de manera vertical
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        # Si el punto inicial X es mayor que el punto final X,
        # intercambio los puntos para siempre dibujar de
        # izquierda a derecha
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        limit = 0.5
        m = dy / dx
        y = y0

        for x in range(x0, x1 + 1):
            if steep:
                # Dibujar de manera vertical
                self.glPoint(y, x, clr)
            else:
                # Dibujar de manera horizontal
                self.glPoint(x, y, clr)

            offset += m

            if offset >= limit:
                if y0 < y1:
                    y += 1
                else:
                    y -= 1

                limit += 1

    def boundaries(self, x: int, y: int, poly) -> bool:
        num = len(poly)
        j = num - 1
        c = False
        for i in range(num):
            if (x == poly[i][0]) and (y == poly[i][1]):
                # El punto que se esta viendo es una esquina
                return True

            # El punto que se esta viendo está dentro de la figura tomando en cuenta la pendiente de  los puntos
            if ((poly[i][1] > y) != (poly[j][1] > y)):
                slope = (x-poly[i][0])*(poly[j][1]-poly[i][1]) - \
                    (poly[j][0]-poly[i][0])*(y-poly[i][1])
                if slope == 0:
                    return True
                # Revisa si el slope es una linea horizontal y por lo tanto seria considerado un boundary
                if (slope < 0) != (poly[j][1] < poly[i][1]):
                    # Revisa si el punto que se está viendo está dentro de la figura
                    c = not c
            j = i
        return c

    def glFill(self, poly, clr=None):
        for i in range(self.width):
            for j in range(self.height):
                if self.boundaries(i, j, poly):
                    self.glPoint(i, j, clr)

    def glFillTriangle(self, v0, v1, v2, clr=None):
        # Scan Algorithm

        if v0[1] < v1[1]:
            v0, v1 = v1, v0
        if v0[1] < v2[1]:
            v0, v2 = v2, v0
        if v1[1] < v2[1]:
            v1, v2 = v2, v1

        def flattBottom(vA, vB, vC):
            try:
                slopeAB = (vB[0]-vA[0])/(vB[1]-vA[1])
                slopeAC = (vC[0]-vA[0])/(vC[1]-vA[1])
            except ZeroDivisionError:
                pass
            else:
                x0 = vB[0]
                x1 = vC[0]

                for y in range(int(vB[1]), int(vA[1])):
                    self.glLineC(int(x0), y, int(x1), y, color(
                        random.random(), random.random(), random.random()))
                    x0 += slopeAB
                    x1 += slopeAC

        def flattTop(vA, vB, vC):
            try:
                slopeCA = (vC[0]-vA[0])/(vC[1]-vA[1])
                slopeCB = (vC[0]-vB[0])/(vC[1]-vB[1])
            except ZeroDivisionError:
                pass
            else:
                x0 = vA[0]
                x1 = vB[0]

                for y in range(int(vA[1]), int(vC[1]), -1):

                    self.glLineC(int(x0), y, int(x1), y, color(
                        random.random(), random.random(), random.random()))
                    x0 -= slopeCA
                    x1 -= slopeCB

        if v1[1] == v2[1]:
            # Parte plana abajo
            flattBottom(v0, v1, v2)

        elif v0[1] == v1[1]:
            # Parte plana arriba

            flattTop(v0, v1, v2)
        else:
            # Se parte
            # Teorema de intercepto

            vD = [v0[0] + ((v1[1]-v0[1])/(v2[1]-v0[1])) * (v2[0]-v0[0]), v1[1]]

            flattBottom(v0, v1, vD)
            flattTop(v1, vD, v2)
            pass

        # self.glLine(int(v0[0]), int(v0[1]), int(
        #     v1[0]), int(v1[1]), color(0, 0, 0))
        # self.glLine(int(v1[0]), int(v1[1]), int(
        #     v2[0]), int(v2[1]), color(0, 0, 0))
        # self.glLine(int(v2[0]), int(v2[1]), int(
        #     v0[0]), int(v0[1]), color(0, 0, 0))

    def gloutTriangle(self, v0, v1, v2, clr=None):
        # Scan Algorithm
        if v0[1] < v1[1]:
            v0, v1 = v1, v0
        if v0[1] < v2[1]:
            v0, v2 = v2, v0
        if v1[1] < v2[1]:
            v1, v2 = v2, v1
        self.glLine(int(v0[0]), int(v0[1]), int(
            v1[0]), int(v1[1]), clr)
        self.glLine(int(v1[0]), int(v1[1]), int(
            v2[0]), int(v2[1]), clr)
        self.glLine(int(v2[0]), int(v2[1]), int(
            v0[0]), int(v0[1]), clr)

    def glLoadModel(self, filename, translate=[0, 0, 0], rotate=[0, 0, 0], scale=[1, 1, 1]):
        model = Obj(filename)

        modelMatrix = self.glCreateObjectMatrix(translate, rotate, scale)

        for face in model.faces:

            vertCount = len(face)
            v0 = model.vertices[face[0][0] - 1]
            v1 = model.vertices[face[1][0] - 1]
            v2 = model.vertices[face[2][0] - 1]

            v0 = self.glTransform(v0, modelMatrix)
            v1 = self.glTransform(v1, modelMatrix)
            v2 = self.glTransform(v2, modelMatrix)

            self.glFillTriangle(v0, v1, v2, self.currentColor)

    def glTransform(self, vertex, matrix):

        v = [vertex[0], vertex[1], vertex[2], 1]
        vt = producto_matriz_vector(matrix, v)

        vf = [vt[0] / vt[3],
              vt[1] / vt[3],
              vt[2] / vt[3]]

        return vf

    def glCreateRotationMatrix(self, pitch, yaw, roll):
        pitch *= math.pi / 180
        yaw *= math.pi / 180
        roll *= math.pi / 180

        pitchMatrix = [[1, 0, 0, 0],
                       [0, math.cos(pitch), -math.sin(pitch), 0],
                       [0, math.sin(pitch), math.cos(pitch), 0],
                       [0, 0, 0, 1]]
        yawnMatrix = [[math.cos(yaw), 0, math.sin(yaw), 0],
                      [0, 1, 0, 0],
                      [-math.sin(yaw), 0, math.cos(yaw), 0],
                      [0, 0, 0, 1]]
        rollMatrix = [[math.cos(roll), -math.sin(roll), 0, 0],
                      [math.sin(roll), math.cos(roll), 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]]

        return producto_matrices(producto_matrices(pitchMatrix, yawnMatrix), rollMatrix)

    def glCreateObjectMatrix(self, translate, rotate, scale):

        translation = [[1, 0, 0, translate[0]],
                       [0, 1, 0, translate[1]],
                       [0, 0, 1, translate[2]],
                       [0, 0, 0, 1]]

        rotation = self.glCreateRotationMatrix(*rotate)

        scaleMat = [[scale[0], 0, 0, 0],
                    [0, scale[1], 0, 0],
                    [0, 0, scale[2], 0],
                    [0, 0, 0, 1]]

        tr = producto_matrices(translation, rotation)
        final = producto_matrices(tr, scaleMat)
        return final

    def glFinish(self, filenames):

        with open(filenames, "wb") as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + (self.width*self.height*3)))
            file.write(dword(0))
            file.write(dword(14 + 40))

            # InfoHeader
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width*self.height*3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # Color Table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])
