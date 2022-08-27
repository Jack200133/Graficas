from gl import Renderer, color
from shaders import flat,gourad,toon,glow,void,inverso,algo,wim,Nmap
from texture import Texture

render = Renderer()
height = 1080
width = 1080
render.glCreateWindow(width, height)
render.glClear()

render.background = Texture('./models/space.bmp')
#render.normal_map = Texture('models/orion/normal.bmp')

render.glClearBackground()


render.active_shader = gourad
#render.active_texture = Texture('models/orion/textura.bmp')
# render.glLookAt([1, 0,-10], [0,0,0])
# render.glLoadModel("models/astro/model.obj",
#                    translate=[-3, -3,-10],
#                    scale=[0.02, 0.02,0.02])

#render.active_shader = Nmap
#render.active_texture = Texture("models/ufo/mat.bmp")
render.glLoadModel("models/delorian/model.obj",
                   translate=[3, -3,-10],
                   scale=[0.02, 0.02,0.02])
render.glFinish("proyecto.bmp")