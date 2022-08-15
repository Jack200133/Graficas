from gl import Renderer, color
from shaders import flat,gourad
from texture import Texture

render = Renderer()
height = 1080
width = 2080
render.glCreateWindow(width, height)
render.glClearColor(0, 0, 0)
render.glColor(1, 1, 1)
render.glClear()

# render.active_shader = gourad
# render.active_texture = Texture("./rocket/rocket.bmp")
# render.glLoadModel("./rocket/rocket.obj",
#                    translate=[3, height/4, -10],
#                    rotate=[0, 180, 0],
#                    scale=[2, 2, 2])


# render.active_shader = flat
# render.active_texture = Texture("./models/model.bmp")
# render.glLoadModel("./models/model.obj",
#                    translate=[-3, 0,-15],
#                    rotate=[0, 90, 0],
#                    scale=[3, 3, 3])

modelP = [0,0,-10]
render.glLookAt(modelP, [-5,-2,0])

render.active_shader = gourad
render.active_texture = Texture("./models/model.bmp")
render.glLoadModel("./models/model.obj",
                   translate=modelP,
                   rotate=[0, 0, 0],
                   scale=[3, 3, 3])

#render.active_texture = Texture("./rocket/rocket.bmp")
# render.glLoadModel("./rocket/rocket.obj",
#                    translate=[-3, 0,-10],
#                    scale=[0.03, 0.03,0.03])
# render.glLoadModel("./rocket/rocket.obj",
#                    translate=[3, 0,-20],
#                    scale=[0.03, 0.03, 0.03])
#render.glFillTriangle([0, 0], [100, 100], [200, 0])
render.glFinish("sr5.bmp")
