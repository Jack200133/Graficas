from gl import Renderer, color
from shaders import flat

render = Renderer()
height = 1080
width = 1080
render.glCreateWindow(width, height)
render.glClearColor(0.5, 0.5, 0.5)
render.glColor(1, 1, 1)
render.glClear()

render.active_shader = flat

render.glLoadModel("face.obj",
                   translate=[width/2, height/2, 0],
                   rotate=[0, 180, 0],
                   scale=[20, 20, 20])
#render.glFillTriangle([0, 0], [100, 100], [200, 0])
render.glFinish("final.bmp")
