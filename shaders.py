from mate import producto_punto, inversa


def flat(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    r, g, b = kwargs["vcolor"]
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255
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
