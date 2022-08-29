from gl import Renderer, color
from shaders import flat,gourad,toon,glow,void,inverso,algo,wim,Nmap
from texture import Texture

render = Renderer()
aspect = [16,9,240]
height = aspect[1]*aspect[2]
width = aspect[0]*aspect[2]
render.glCreateWindow(width, height)
render.glClear()

render.background = Texture('./models/space.bmp')

render.glClearBackground()

render.active_shader = algo
render.active_texture = Texture('models/nasa/texture.bmp')
render.glLoadModel("models/nasa/model.obj",
                   translate=[0, -3,-10],
                   rotate =[0,90,45],
                   scale=[0.5,0.5,0.5])


render.active_shader = glow
render.active_texture = Texture('models/ufo/texture.bmp')
render.glLoadModel("models/ufo/model.obj",
                   translate=[-3, 2,-10],
                   rotate =[0,0,0],
                   scale=[0.5,0.5,0.5])

render.normal_map = Texture('models/raven/normal.bmp')
render.active_shader = Nmap
render.active_texture = Texture('models/raven/texture.bmp')
render.glLoadModel("models/raven/model.obj",
                   translate=[5, 3,-10],
                   rotate =[0,45,45],
                   scale=[0.004,0.004,0.004])
render.active_shader = void
render.active_texture = Texture('models/rocket/texture.bmp')
render.glLoadModel("models/rocket/model.obj",
                   translate=[-6, -3,-10],
                   rotate =[0,45,45],
                   scale=[0.01,0.01,0.01])

render.active_shader = glow
render.active_texture = Texture('models/norw/texture.bmp')
render.glLoadModel("models/norw/model.obj",
                   translate=[1, -5,-10],
                   rotate =[0,45,45],
                   scale=[2,2,2])
render.active_shader = wim
render.glLoadModel("models/alien/model.obj",
                   translate=[6, -3,-10],
                   rotate =[0,45,0],
                   scale=[0.5,0.5,0.5])
render.glFinish("proyecto.bmp")