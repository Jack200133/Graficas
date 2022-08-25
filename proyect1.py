from gl import Renderer, color
from shaders import flat,gourad,toon,glow,void,inverso,algo,wim,Nmap
from texture import Texture

render = Renderer()
height = 2080
width = 2080
render.glCreateWindow(width, height)
render.glClear()

render.background = Texture('./models/space.bmp')
render.normal_map = Texture('rocket/normal.bmp')

render.glClearBackground()


render.active_shader = gourad
render.active_texture = Texture("./rocket/rocket.bmp")
render.glLookAt([1, 0,-10], [0,0,0])
render.glLoadModel("./rocket/rocket.obj",
                   translate=[-3, -3,-10],
                   scale=[0.02, 0.02,0.02])

render.active_shader = Nmap
render.active_texture = Texture("./rocket/rocket.bmp")
render.glLookAt([1, 0,-10], [0,0,0])
render.glLoadModel("./rocket/rocket.obj",
                   translate=[3, -3,-10],
                   scale=[0.02, 0.02,0.02])
# render.active_shader = void
# render.glLoadModel("./rocket/rocket.obj",
#                    translate=[3, -3,-10],
#                    scale=[0.02, 0.02,0.02])
# render.active_shader = wim
# render.glLoadModel("./rocket/rocket.obj",
#                    translate=[0, -3,-10],
#                    scale=[0.02, 0.02,0.02])
# render.active_shader = inverso
# render.glLoadModel("./rocket/rocket.obj",
#                    translate=[6, -3,-10],
#                    scale=[0.02, 0.02,0.02])
render.glFinish("proyecto.bmp")