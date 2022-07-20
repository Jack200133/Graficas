from gl import Renderer, V2

render = Renderer()
height = 700
width = 960
render.glCreateWindow(width, height)
render.glClearColor(0.5, 0.5, 0.5)
render.glColor(1, 1, 0)
render.glClear()
# render.glViewPort(440,440,200,200)


# for i in range(400):
#    render.glPoint(250, i)
render.glColor(1, 0, 0)
render.glPoint_VP(0, 0)
render.glPoint_VP(0, 1)
render.glPoint_VP(0, -1)
# for i in range(0,height,50):
#     render.glLine(int(width/2),int(height/2),width,i)
# render.glColor(0, 1, 0)
# for i in range(0,height,50):
#     render.glLine(int(width/2),int(height/2),0,i)
# render.glColor(1, 1, 0)
# for i in range(0,width,50):
#     render.glLine(int(width/2),int(height/2),i,height)
# render.glColor(0, 0, 1)
# for i in range(0,width,50):
#     render.glLine(int(width/2),int(height/2),i,0)

dy = height/100
dx = width/100

x = 0
y = height

# for i in range(100):
#     render.glLine(int(x), int(y), int(x+dx), int(y+dy))
#     x += dx
#     y -= dy


# render.glLine(int(width/2),int(height/2),int(500),int(height))
# render.glLine(int(width/2),int(height/2),int(width),int(height))
# render.glLine(int(width/2),int(height/2),int(width),int(height/2))
# Triangulo
render.glLine(100, 100, 200, 200)
render.glLine(200, 200, 300, 100)
render.glLine(300, 100, 100, 100)

# Cuadrado

render.glLine(400, 100, 500, 100)
render.glLine(500, 100, 500, 200)
render.glLine(500, 200, 400, 200)
render.glLine(400, 200, 400, 100)

# Pentagono

render.glLine(200, 500, 100, 400)
render.glLine(200, 500, 300, 400)
render.glLine(100, 400, 150, 300)
render.glLine(300, 400, 250, 300)
render.glLine(150, 300, 250, 300)

# HEXAGONO

render.glLine(500, 300, 400, 400)
render.glLine(500, 300, 600, 400)
render.glLine(400, 400, 400, 500)
render.glLine(600, 400, 600, 500)
render.glLine(600, 500, 500, 600)
render.glLine(400, 500, 500, 600)


# octagono

render.glLine(700, 100, 800, 100)
render.glLine(700, 100, 600, 200)
render.glLine(800, 100, 900, 200)

render.glLine(600, 200, 600, 300)
render.glLine(900, 200, 900, 300)

render.glLine(600, 300, 700, 400)
render.glLine(900, 300, 800, 400)

render.glLine(700, 400, 800, 400)

# render.glLineCarlos(v0,v1)
# render.glLineCarlos(v0,v2)
# render.glLineCarlos(v0,v3)

render.glFinish("finalen.bmp")
