import struct
import numpy as np
from collections import namedtuple
from obj import Obj

V2 = namedtuple('Vertex2', ['x', 'y'])


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

        dx2 = dx << 1
        dy2 = dy << 1

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

    def glFillTriangle(self, v0,v1,v2, clr=None):
        #Scan Algorithm

        if v0[1] < v1[1]:
            v0, v1 = v1, v0
        if v0[1] < v2[1]:
            v0, v2 = v2, v0
        if v1[1] < v2[1]:
            v1, v2 = v2, v1

        def flattBottom(vA,vB,vC):
            try:
                slopeAB = (vB[0]-vA[0])/(vB[1]-vA[1])
                slopeAC = (vC[0]-vA[0])/(vC[1]-vA[1])
            except ZeroDivisionError:
                pass
            else:
            #slopeAB = (vB[1]-vA[1])/(vB[0]-vA[0])
            #slopeAC = (vC[1]-vA[1])/(vC[0]-vA[0])

                x0 = v1[0]
                x1 = v2[1]

                for y in range(v1[1],v0[1]+1):
                    self.glLine(int(x0), y, int(x1), y, clr)
                    x0 += slopeAB
                    x1 += slopeAC
                    if x0 > x1:
                        x0, x1 = x1, x0

        def flattTop(vA,vB,vC):
            try:
                slopeCA = (vC[0]-vA[0])/(vC[1]-vA[1])
                slopeCB = (vC[0]-vB[0])/(vC[1]-vB[1])
            except ZeroDivisionError:
                pass
            else:
                x0 = vA[0]
                x1 = vB[0]

                for y in range(vA[1],vC[1],-1):
                    self.glLine(int(x0), y, int(x1), y, clr)
                    x0 -= slopeCA
                    x1 -= slopeCB
                    if x0 > x1:
                        x0, x1 = x1, x0

        if v1[1] == v2[1]:
            #Parte plana abajo
            flattBottom(v0,v1,v2)
            
        elif v0[1] == v1[1]:
            #Parte plana arriba

            flattTop(v0,v1,v2)
        else:
            # Se parte 
            #Teorema de intercepto

            vD = [v0[0] + ((v1[1]-v0[1])/(v2[1]-v0[1])) * (v2[0]-v0[0]),v1[1]]

            flattBottom(v0,v1,vD)
            flattTop(v1,vD,v2)
            pass

        self.glLine(v0[0],v0[1],v1[0],v1[1],clr)
        self.glLine(v1[0],v1[1],v2[0],v2[1],clr)
        self.glLine(v2[0],v2[1],v0[0],v0[1],clr)

    def glLoadModel2(self,filename):
        model = Obj(filename)

        for face in model.faces:
            vcount = len(face)
            for j in range(vcount):
                f1 = face[j][0]
                f2 = face[(j+1) % vcount][0]
                x1 = model.vertices[f1 - 1][0]
                y1 = model.vertices[f1 - 1][1]
                x2 = model.vertices[f2 - 1][0]
                y2 = model.vertices[f2 - 1][1]
                self.glLine(x1, y1, x2, y2)


    def glLoadModel(self,filename,translate,rotate,scale):
        model = Obj(filename)
        modelMatrix = self.glCreateObjectMatrix(translate, rotate, scale)

        for face in model.faces:
            vertCount = len(face)
            for vert in range(vertCount):
                v0 = model.vertices[ face[vert][0] - 1]
                v1 = model.vertices[ face[(vert + 1) % vertCount][0] - 1]

                v0 = self.glTransform(v0, modelMatrix)
                v1 = self.glTransform(v1, modelMatrix)

                self.glLine(v0[0], v0[1], v1[0], v1[1])

    def glCreateObjectMatrix2(self, translate, rotate, scale):
        modelMatrix = np.identity(4)
        modelMatrix = self.glTranslate(modelMatrix, translate)
        modelMatrix = self.glRotate(modelMatrix, rotate)
        modelMatrix = self.glScale(modelMatrix, scale)
        return modelMatrix

    def glTransform(self, vertex, matrix):

        v = V4(vertex[0], vertex[1], vertex[2], 1)
        vt = matrix @ v
        vt = vt.tolist()[0]
        vf = V3(vt[0] / vt[3],
                vt[1] / vt[3],
                vt[2] / vt[3])

        return vf

    def glCreateObjectMatrix(self, translate, rotate , scale):

            translation = np.matrix([[1, 0, 0, translate.x],
                                    [0, 1, 0, translate.y],
                                    [0, 0, 1, translate.z],
                                    [0, 0, 0, 1]])

            rotation = np.identity(4)

            scaleMat = np.matrix([[scale.x, 0, 0, 0],
                                [0, scale.y, 0, 0],
                                [0, 0, scale.z, 0],
                                [0, 0, 0, 1]])

            return translation * rotation * scaleMat

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
        