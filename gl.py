import struct
from collections import namedtuple

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

            # El punto que se esta biendo está dentro de la figura tomando en cuenta la pendiente de  los puntos
            if ((poly[i][1] > y) != (poly[j][1] > y)):
                slope = (x-poly[i][0])*(poly[j][1]-poly[i][1]) - \
                    (poly[j][0]-poly[i][0])*(y-poly[i][1])
                if slope == 0:
                    return True
                # REvisa si el slope es una linea horizontal y por lo tanto seria considerado un boundary
                if (slope < 0) != (poly[j][1] < poly[i][1]):
                    # Revisa si el punto que se está viendo está dentro de la figura
                    c = not c
            j = i
        return c

    def glFill(self, poly, clr=None):
        for i in range(self.height):
            for j in range(self.width):
                if self.boundaries(i, j, poly):
                    self.glPoint(i, j, clr)

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
