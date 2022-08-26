from mate import producto_punto, inversa,normal_vector3,producto_matriz_vector


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

def void(render, **kwargs):

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
    antiglowAmount = producto_punto(triangleNormal, camFoward)

    color = [1,0.5,0]
    if glowAmount < antiglowAmount:
        color = [0,0,0]
        r,g,b= 0,0,0

    #if glowAmount <= 0: glowAmount = 0


    b += color[2] * glowAmount
    g += color[1] * glowAmount
    r += color[0] * glowAmount

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if intensidad > 0:
        return r, g, b
    else:
        return 0,0,0

def inverso(render, **kwargs):

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

    b = 1 - b
    g = 1 - g
    r = 1 - r

    if intensidad > 0:
        return r, g, b
    else:
        return 0,0,0


def algo(render, **kwargs):

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

    b *= (abs(nA[0])*abs(nB[0])*abs(nC[0]))*intensidad %1
    g *= (abs(nA[1])*abs(nB[1])*abs(nC[1]))*intensidad %1
    r *= (abs(nA[2])*abs(nB[2])*abs(nC[2]))*intensidad %1

    if intensidad > 0:
        return r, g, b
    else:
        return 0,0,0

def wim(render, **kwargs):

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

    if intensidad < -0.9:
        b = (1*intensidad)%1
        g = (1 *intensidad)%1
        r = (1 *intensidad)%1 
    elif intensidad < -0.8:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]) * abs(intensidad))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]))
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]))
    elif intensidad < -0.7:
        b = (1*intensidad)%1
        g = (1 *intensidad)%1
        r = (1 *intensidad)%1 
    elif intensidad < -0.6:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]) * abs(intensidad))
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]))
    elif intensidad < -0.5:
        b = (1*intensidad)%1
        g = (1 *intensidad)%1
        r = (1 *intensidad)%1 
    elif intensidad < -0.4:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]))
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]) * abs(intensidad))
    elif intensidad < -0.3:
        b = (1*intensidad)%1
        g = (1 *intensidad)%1
        r = (1 *intensidad)%1 
    elif intensidad < -0.2:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]) * abs(intensidad))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]))
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2])) 
    elif intensidad < -0.1:
        b = (1*abs(intensidad))
        g = (1 *abs(intensidad))
        r = (1 *abs(intensidad))
    elif intensidad < 0:
        b = 0
        g = 0
        r = 0   
    elif intensidad < 0.1:
        b = (1*intensidad)%1
        g = (1 *intensidad)%1
        r = (1 *intensidad)%1
    elif intensidad < 0.2:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]) * intensidad)
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]))
    elif intensidad < 0.3:
        b = (1*intensidad)%1
        g = (1 *intensidad)%1
        r = (1 *intensidad)%1
    elif intensidad < 0.4:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]))
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]) *intensidad)
    elif intensidad < 0.5:
        b = (1*intensidad)%1
        g = (1 *intensidad)%1
        r = (1 *intensidad)%1
    elif intensidad < 0.6:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]) * intensidad)
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]))
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]))
    elif intensidad < 0.7:
        b = (1*intensidad)%1
        g = (1 *intensidad)%1
        r = (1 *intensidad)%1
    elif intensidad < 0.6:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]) * intensidad)
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]))
    elif intensidad < 0.8:
        b = (1*intensidad)%1
        g = (1 *intensidad)%1
        r = (1 *intensidad)%1
    elif intensidad < 0.9:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]))
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]) *intensidad)
    elif intensidad <= 1:
        b = (1*intensidad)%1
        g = (1 *intensidad)%1
        r = (1 *intensidad)%1

    return r, g, b


def Nmap(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vcolor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    tangent = kwargs["tangent"]
    bitangent = kwargs["bitangent"]

    b /= 255
    g /= 255
    r /= 255

    # P = Au + Bv + Cw
    tU = tA[0] * u + tB[0] * v + tC[0] * w
    tV = tA[1] * u + tB[1] * v + tC[1] * w
    if render.active_texture:

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w]
    luz = inversa(render.dirLight)
    if render.normal_map:
        texNormal = render.normal_map.getColor(tU, tV)
        texNormal = [texNormal[0] * 2 - 1,
                    texNormal[1] * 2 - 1,
                    texNormal[2] * 2 - 1]
        texNormal = normal_vector3(texNormal)

        tangentMatrix = [[tangent[0], bitangent[0], triangleNormal[0]],
                        [tangent[1], bitangent[1], triangleNormal[1]],
                        [tangent[2], bitangent[2], triangleNormal[2]]]
        
        texNormal = producto_matriz_vector(tangentMatrix, texNormal)
        texNormal = normal_vector3(texNormal)

        intensidad = producto_punto(texNormal, luz)
    else:
        intensidad = producto_punto(triangleNormal, luz)

    b *= intensidad
    g *= intensidad
    r *= intensidad

    if intensidad > 0:
        return r, g, b
    else:
        return 0,0,0
