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

modelP = [0,0,-10]

# render.active_texture = Texture("./models/model.bmp")
# render.glLoadModel("./models/model.obj",
#                    translate=modelP,
#                    rotate=[0, 0, 0],
#                    scale=[3, 3, 3])

#render.glLookAt(modelP, [-5,-2,0])

render.active_shader = gourad
#render.glLookAt([-3, -4,-10], [3,-4,1])

render.active_texture = Texture("./rocket/rocket.bmp")
render.glLookAt([0, 0,-10], [0,0,-3])
render.glLoadModel("./rocket/rocket.obj",
                   translate=[0, -3,-10],
                   scale=[0.02, 0.02,0.02])
render.glFinish("sr5-medium.bmp")
render.glClear()

render.glLookAt([0, 0,-10], [0,-1,-4])
render.glLoadModel("./rocket/rocket.obj",
                   translate=[0, 0,-10],
                   rotate=[-30, 0, 0],
                   scale=[0.02, 0.02,0.02])
render.glFinish("sr5-low.bmp")
render.glClear()
render.glLookAt([0, 0,-10], [0,2,-3])
render.glLoadModel("./rocket/rocket.obj",
                   translate=[0, -3,-10],
                   rotate=[30, 0, 0],
                   scale=[0.02, 0.02,0.02])
render.glFinish("sr5-high.bmp")
render.glClear()

render.glLookAt([0, 0,-10], [0,0,-3])
render.glLoadModel("./rocket/rocket.obj",
                   translate=[0, -3,-10],
                   rotate=[0, 0, -15],
                   scale=[0.02, 0.02,0.02])
# render.glLoadModel("./rocket/rocket.obj",
#                    translate=[3, 0,-20],
#                    scale=[0.02, 0.02, 0.02])
#render.glFillTriangle([0, 0], [100, 100], [200, 0])
render.glFinish("sr5-dutch.bmp")
