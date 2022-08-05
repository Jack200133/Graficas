from gl import Renderer, color


render = Renderer()
height = 1080
width = 1080
render.glCreateWindow(width, height)
render.glClearColor(0.5, 0.5, 0.5)
render.glColor(1, 1, 0)
render.glClear()

render.glLoadModel("model.obj",
                   translate=[width/2, height/2, 0],
                   rotate=[0, 180, 0],
                   scale=[200, 200, 200])
#render.glFillTriangle([0, 0], [100, 100], [200, 0])
render.glFinish("final.bmp")
