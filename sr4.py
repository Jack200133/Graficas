from gl import Renderer, color
from shaders import flat,gourad
from texture import Texture

render = Renderer()
height = 1080
width = 1080
render.glCreateWindow(width, height)
render.glClearColor(0.5, 0.5, 0.5)
render.glColor(1, 1, 1)
render.glClear()

render.active_shader = gourad
render.active_texture = Texture("./rocket/rocket.bmp")
render.glLoadModel("./rocket/rocket.obj",
                   translate=[width/2, height/2, 0],
                   rotate=[0, 180, 0],
                   scale=[2, 2, 2])
#render.glFillTriangle([0, 0], [100, 100], [200, 0])
render.glFinish("sr4.bmp")
