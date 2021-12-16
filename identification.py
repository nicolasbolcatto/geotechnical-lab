import math

"""Esta funcion calcula la humedad de una muestra secada al horno en base al peso humedo inicial,
el peso seco y el peso del pesafiltro"""


def humedad(pf, msh, mss):
    agua = msh - mss
    suelo_seco = mss - pf
    w = round(100 * agua / suelo_seco, 1)
    return w


"""Esta funcion calcula el limite liquido a partir de los resultados del ensayo en el cascador
de Casagrande. Permite utilizar la funcion de extrapolacion para el ensayo de un punto
o bien utilizar dos puntos para interpolar el resultado a 25 golpes"""


def limite_liquido(n1, msh1, mss1, pf1, n2, msh2, mss2, pf2):
    if math.isnan(n2):
        w = 100 * (msh1 - mss1) / (mss1 - pf1)
        ll = w / (1.419 - 0.3 * (math.log(n1, 10)))
        return ll
    else:
        w1 = (msh1 - mss1) / (mss1 - pf1)
        w2 = (msh2 - mss2) / (mss2 - pf2)
        ll = w1 + (n1 - 25) * ((w2 - w1) / (n1 - n2))
        return ll


"""Esta funcion calcula el limite plástico de una muestra secada al horno en base al promedio
de dos muestras"""


def limite_plastico(pf1, msh1, mss1, pf2, msh2, mss2):
    agua1 = msh1 - mss1
    suelo_seco1 = mss1 - pf1
    w1 = round(100 * agua1 / suelo_seco1, 1)
    agua2 = msh2 - mss2
    suelo_seco2 = mss2 - pf2
    w2 = round(100 * agua2 / suelo_seco2, 1)
    w = 0.5 * (w1 + w2)
    return w


"""Esta funcion determina y grafica la curva granulometrica de un suelo
 según los tamices de la norma ASTM Standard D422"""


def analisis_granulometrico(peso_total, retenidos):
    i = 0
    acumulado = 0
    p = []
    while i < len(retenidos):
        acumulado = acumulado + retenidos[i]
        p.append(round((100 * (peso_total - acumulado) / peso_total), 1))
        i += 1
    return p


"""Este scripto recibe la curva granulométrica de un suelo y devuelve los coeficientes
de uniformidad y curvatura"""


def CU_CC(p):
    tamices = [75, 50, 37.5, 25, 19, 12.7, 9.5, 4.75, 2, 0.85, 0.425, 0.25, 0.15, 0.075]
    D60 = 0
    D30 = 0
    D10 = 0

    for i in range(len(tamices) - 1):
        if p[i] >= 60 and p[i + 1] <= 60:
            a = (p[i] - p[i + 1])
            b = (tamices[i] - tamices[i + 1])
            m = b / a
            D60 = tamices[i] - m * (p[i] - 60)
        if p[i] >= 30 and p[i + 1] <= 30:
            a = (p[i] - p[i + 1])
            b = (tamices[i] - tamices[i + 1])
            m = b / a
            D30 = tamices[i] - m * (p[i] - 30)
        if p[i] >= 10 and p[i + 1] <= 10:
            a = (p[i] - p[i + 1])
            b = (tamices[i] - tamices[i + 1])
            m = b / a
            D10 = tamices[i] - m * (p[i] - 10)

    if D60 > 0 and D10 > 0:
        CU = D60 / D10
    else:
        CU = "ND"
    if D60 > 0 and D30 > 0 and D10 > 0:
        CC = D30 * D30 / D60 / D10
    else:
        CC = "ND"

    if D10 == 0:
        D10 = "ND"
    if D30 == 0:
        D30 = "ND"
    if D60 == 0:
        D60 = "ND"

    return D10, D30, D60, CU, CC


"""Este script recibe los porcentajes pasantes por cada tamiz de una muestra de suelo
y grafica la curva granulométrica según la Norma ASTM D422"""


def plot_analisis_granulometrico(p):
    import matplotlib.pyplot as plt

    # Definicion de tamices en mm
    astm_mm = [75, 50, 37.5, 25, 19, 12.7, 9.5, 4.75, 2, 0.85, 0.425, 0.25, 0.15, 0.075]
    plt.semilogx(astm_mm, p, color="black", linewidth=2.0, linestyle="-")
    plt.title("Análisis granulométrico")
    plt.xlabel("Abertura del tamiz (mm)")
    plt.ylabel("% Pasa")
    plt.xlim(0.01, 100)
    plt.ylim(0, 100)
    plt.xticks((100, 10, 1, 0.1, 0.01), ["100", "10", "1.0", "0.1", "0.01"])
    plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    plt.gca().invert_xaxis()
    plt.grid(True, color="grey", linewidth=0.5)

    # Barras verticales
    plt.text(0.07, 90, "#200", rotation=90)
    plt.plot((0.075, 0.075), (0, 100), color="black", linewidth=1.0, linestyle="--")
    plt.text(0.14, 90, "#100", rotation=90)
    plt.plot((0.15, 0.15), (0, 100), color="black", linewidth=1.0, linestyle="--")
    plt.text(0.24, 90, "#60", rotation=90)
    plt.plot((0.25, 0.25), (0, 100), color="black", linewidth=1.0, linestyle="--")
    plt.text(0.41, 2, "#40", rotation=90)
    plt.plot((0.425, 0.425), (0, 100), color="black", linewidth=1.0, linestyle="--")
    plt.text(0.84, 2, "#20", rotation=90)
    plt.plot((0.85, 0.85), (0, 100), color="black", linewidth=1.0, linestyle="--")
    plt.text(1.9, 2, "#10", rotation=90)
    plt.plot((2, 2), (0, 100), color="black", linewidth=1.0, linestyle="--")
    plt.text(4.7, 2, "#4", rotation=90)
    plt.plot((4.75, 4.75), (0, 100), color="black", linewidth=1.0, linestyle="--")
    plt.text(9.2, 2, "3/8''", rotation=90)
    plt.plot((9.5, 9.5), (0, 100), color="black", linewidth=1.0, linestyle="--")
    plt.text(12.7, 2, "1/2''", rotation=90)
    plt.plot((12.7, 12.7), (0, 100), color="black", linewidth=1.0, linestyle="--")
    plt.text(18.5, 2, "3/4''", rotation=90)
    plt.plot((19, 19), (0, 100), color="black", linewidth=1.0, linestyle="--")
    plt.text(24.6, 2, "1''", rotation=90)
    plt.plot((25, 25), (0, 100), color="black", linewidth=1.0, linestyle="--")
    plt.text(37.2, 2, "1.5''", rotation=90)
    plt.plot((37.5, 37.5), (0, 100), color="black", linewidth=1.0, linestyle="--")
    plt.text(49.6, 2, "2''", rotation=90)
    plt.plot((50, 50), (0, 100), color="black", linewidth=1.0, linestyle="--")
    plt.text(74.6, 2, "3''", rotation=90)
    plt.plot((75, 75), (0, 100), color="black", linewidth=1.0, linestyle="--")

    plt.show()
