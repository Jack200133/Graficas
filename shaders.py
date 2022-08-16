from mate import producto_punto, inversa


def flat(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    r, g, b = kwargs["vcolor"]
    tA, tB, tC = kwargs["texCoords"]
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    # me quede en 1:10:58 m,artes 2 de agosto
    intensidad = producto_punto(triangleNormal, inversa(render.dirLight))

    # dirLight = np.array(render.dirLight)
    # triangleNormal = np.array(triangleNormal)
    # intensity = np.dot(triangleNormal, -dirLight)


    b *= intensidad
    g *= intensidad
    r *= intensidad

    if intensidad > 0:
        return r, g, b
    else:
        return 0, 0, 0



def gourad(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vcolor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w]

    intensidad = producto_punto(triangleNormal, inversa(render.dirLight))

    b *= intensidad
    g *= intensidad
    r *= intensidad

    if intensidad > 0:
        return r, g, b
    else:
        return 0,0,0

def toon(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vcolor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w]

    intensidad = producto_punto(triangleNormal, inversa(render.dirLight))
    if intensidad < 0.2:
        intensidad = 0.1
    elif intensidad < 0.5:
        intensidad = 0.3
    elif intensidad < 0.8:
        intensidad = 0.6
    elif intensidad <=1:
        intensidad = 1

    b *= intensidad
    g *= intensidad
    r *= intensidad

    if intensidad > 0:
        return r, g, b
    else:
        return 0,0,0


def glow(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vcolor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w]

    intensidad = producto_punto(triangleNormal, inversa(render.dirLight))

    b *= intensidad
    g *= intensidad
    r *= intensidad

    camFoward = render.camMatrix[0][2], render.camMatrix[1][2], render.camMatrix[2][2]
    glowAmount = 1 - producto_punto(triangleNormal, camFoward)
    if glowAmount <= 0: glowAmount = 0

    green = [0,1,0]

    b += green[2] * glowAmount
    g += green[1] * glowAmount
    r += green[0] * glowAmount

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if intensidad > 0:
        return r, g, b
    else:
        return 0,0,0
