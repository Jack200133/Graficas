from gl import Renderer, color


render = Renderer()
height = 540
width = 960
render.glCreateWindow(width, height)
render.glClearColor(0.5, 0.5, 0.5)
render.glColor(1, 1, 0)
render.glClear()


def drawPol(pol, crl=None):
    for i in range(len(pol)):
        render.glLine(pol[i][0], pol[i][1], pol[(i+1) %
                                                len(pol)][0], pol[(i+1) % len(pol)][1], crl)


pol1 = [[165, 380], [185, 360], [180, 330], [207, 345], [233, 330],
        [230, 360], [250, 380], [220, 385], [205, 410], [193, 383]]

pol2 = [[321, 335], [288, 286], [339, 251], [374, 302]]

pol3 = [[377, 249], [411, 197], [436, 249]]

pol4 = [[413, 177], [448, 159], [502, 88], [553, 53], [535, 36], [676, 37], [660, 52],
        [750, 145], [761, 179], [672, 192], [659, 214], [
            615, 214], [632, 230], [580, 230],
        [597, 215], [552, 214], [517, 144], [466, 180]]
pol5 = [[682, 175], [708, 120], [735, 148], [739, 170]]

bl = color(0.5, 0.5, 0.5)
rd = color(1, 0, 0)
gr = color(0, 1, 0)
bu = color(0, 0, 1)
ye = color(1, 1, 0)

drawPol(pol1, ye)
drawPol(pol2, rd)
drawPol(pol3, gr)
drawPol(pol4, bu)
drawPol(pol5, bl)

render.glFill(pol1, ye)
render.glFill(pol2, rd)
render.glFill(pol3, gr)
render.glFill(pol4, bu)
render.glFill(pol5, bl)
render.glFinish("lab01.bmp")
