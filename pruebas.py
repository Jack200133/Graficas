from gl import Renderer, color


render = Renderer()
height = 1080
width = 1080
render.glCreateWindow(width, height)
render.glClearColor(0.5, 0.5, 0.5)
render.glColor(0, 0, 0)
render.glClear()

width = 960
height = 540

render.glLoadModel("cube.obj",
                   translate=[width/2, height/2, 0],
                   rotate=[0, 0, 0],
                   scale=[15, 15, 15])
#render.glFillTriangle([0, 0], [100, 100], [200, 0])
render.glFinish("final.bmp")
