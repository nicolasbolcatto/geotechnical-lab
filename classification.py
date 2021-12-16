"""Esta funcion clasifica el suelo mediante el Sistema Unificado de Clasificacion
de Suelos (SUCS) y devuelve además la descripción según la Norma ASTM D2487"""


def SUCS(ll, lp, p4, p200, cu, cc):
    if ll > 0 and lp > 0:
        ip = ll - lp  # indice plástico
    else:
        ip = 0
    fg = 100 - p200  # fraccion gruesa
    F1 = p4 - p200  # material que pasa el #4 y queda retenido en el #200
    GF = 100 - p4  # fraccion de grava
    fa = p4 - p200  # fraccion de arena

    if p200 < 50:  # suelo de grano grueso
        if F1 <= fg * 0.5:  # grava
            if p200 < 5:
                if cu >= 4 and 1 <= cc <= 3:
                    # grava bien graduada
                    sucs = "GW"
                    Descripcion = "Grava bien graduada"
                else:
                    # grava mal graduada
                    sucs = "GP"
                    Descripcion = "Grava mal graduada"
            elif 5 <= p200 <= 12:
                # grava con finos
                if cu >= 4 and 1 <= cc <= 3:
                    # grava bien graduada con finos
                    if ip < 4 or ip < 0.73 * (ll - 20):
                        # grava bien graduada con limo y arena
                        sucs = "GW-GM"
                        if fa < 15:
                            Descripcion = "Grava bien graduada con limo"
                        else:
                            Descripcion = "Grava bien graduada con limo y arena"
                    elif 4 <= ip <= 7 and ip >= 0.73 * (ll - 20):
                        # grava bien graduada con arcilla limosa
                        sucs = "GW-GC"
                        if fa < 15:
                            Descripcion = "Grava bien graduada con arcilla limosa"
                        else:
                            Descripcion = "Grava bien graduada con arcilla limosa y arena"
                    else:
                        # grava bien graduada con arcilla
                        sucs = "GW-GC"
                        if fa < 15:
                            Descripcion = "Grava bien graduada con arcilla"
                        else:
                            Descripcion = "Grava bien graduada con arcilla y arena"
                else:
                    # grava mal graduada con finos
                    if ip < 4 or ip < 0.73 * (ll - 20):
                        # grava mal graduada con limo
                        sucs = "GP-GM"
                        if fa < 15:
                            Descripcion = "Grava mal graduada con limo"
                        else:
                            Descripcion = "Grava mal graduada con limo y arena"
                    elif 4 <= ip <= 7 and ip >= 0.73 * (ll - 20):
                        # grava mal graduada con arcilla limosa
                        sucs = "GP-GC"
                        if fa < 15:
                            Descripcion = "Grava mal graduada con arcilla limosa"
                        else:
                            Descripcion = "Grava mal graduada con arcilla limosa y arena"
                    else:
                        # grava mal graduada con arcilla
                        sucs = "GP-GC"
                        if fa < 15:
                            Descripcion = "Grava mal graduada con arcilla"
                        else:
                            Descripcion = "Grava mal graduada con arcilla y arena"
            else:
                # grava arcillosa o limosa
                if ip < 4 or ip < 0.73 * (ll - 20):
                    # grava limosa
                    sucs = "GM"
                    if fa < 15:
                        Descripcion = "Grava limosa"
                    else:
                        Descripcion = "Grava limosa con arena"
                elif 4 <= ip <= 7 and ip >= 0.73 * (ll - 20):
                    # grava arcillo-limosa
                    sucs = "GC-GM"
                    if fa < 15:
                        Descripcion = "Grava arcillo-limosa"
                    else:
                        Descripcion = "Grava arcillo-limosa con arena"
                else:
                    # grava arcillosa
                    sucs = "GC"
                    if fa < 15:
                        Descripcion = "Grava arcillosa"
                    else:
                        Descripcion = "Grava arcillosa con arena"
        else:  # arena
            if p200 < 5:
                if cu >= 6 and 1 <= cc <= 3:
                    # arena bien graduada
                    sucs = "SW"
                    Descripcion = "Arena bien graduada"
                else:
                    # arena mal graduada
                    sucs = "SP"
                    Descripcion = "Arena mal graduada"
            elif 5 <= p200 <= 12:
                # arena con finos
                if cu >= 6 and 1 <= cc <= 3:
                    # arena bien graduada con finos
                    if ip < 4 or ip < 0.73 * (ll - 20):
                        # arena bien graduada con limo
                        sucs = "SW-SM"
                        if GF < 15:
                            Descripcion = "Arena bien graduada con limo"
                        else:
                            Descripcion = "Arena bien graduada con limo y grava"
                    elif 4 <= ip <= 7 and ip >= 0.73 * (ll - 20):
                        # arena bien graduada con arcilla limosa
                        sucs = "SW-SC"
                        if GF < 15:
                            Descripcion = "Arena bien graduada con arcilla limosa"
                        else:
                            Descripcion = "Arena bien graduada con arcilla limosa y grava"
                    else:
                        # arena bien graduada con arcilla
                        sucs = "SW-SC"
                        if GF < 15:
                            Descripcion = "Arena bien graduada con arcilla"
                        else:
                            Descripcion = "Arena bien graduada con arcilla y grava"
                else:
                    # arena mal graduada con finos
                    if ip < 4 or ip < 0.73 * (ll - 20):
                        # arena mal graduada con limo
                        sucs = "SP-SM"
                        if GF < 15:
                            Descripcion = "Arena mal graduada con limo"
                        else:
                            Descripcion = "Arena mal graduada con limo y grava"
                    elif 4 <= ip <= 7 and ip >= 0.73 * (ll - 20):
                        # poorly-graded sand with silty-clayley fines
                        sucs = "SP-SC"
                        if GF < 15:
                            Descripcion = "Arena mal graduada con arcilla limosa"
                        else:
                            Descripcion = "Arena mal graduada con arcilla limosa y grava"
                    else:
                        # arena mal graduada con arcilla
                        sucs = "SP-SC"
                        if GF < 15:
                            Descripcion = "Arena mal graduada con arcilla"
                        else:
                            Descripcion = "Arena mal graduada con arcilla y grava"
            else:
                # arena limosa o arcillosa
                if ip < 4 or ip < 0.73 * (ll - 20):
                    # arena limosa
                    sucs = "SM"
                    if GF < 15:
                        Descripcion = "Arena limosa"
                    else:
                        Descripcion = "Arena limosa con grava"
                elif 4 <= ip <= 7 and ip >= 0.73 * (ll - 20):
                    # arena limo-arcillosa
                    sucs = "SC-SM"
                    if GF < 15:
                        Descripcion = "Arena limo-arcillosa"
                    else:
                        Descripcion = "Arena limo-arcillosa con grava"
                else:
                    # arena arcillosa
                    sucs = "SC"
                    if GF < 15:
                        Descripcion = "Arena arcillosa"
                    else:
                        Descripcion = "Arena arcillosa con grava"
    else:  # suelo de grano fino
        if ll < 50:  # baja plasticidad
            if ip < 4 or ip < 0.73 * (ll - 20):  # limo de baja plasticidad
                sucs = "ML"
                if fg < 30:
                    if fg < 15:
                        Descripcion = "Limo"
                    elif GF > fa:
                        Descripcion = "Limo con grava"
                    else:
                        Descripcion = "Limo con arena"
                elif GF > fa:
                    if fa < 15:
                        Descripcion = "Limo gravoso"
                    else:
                        Descripcion = "Limo gravoso con arena"
                else:
                    if GF < 15:
                        Descripcion = "Arena limosa"
                    else:
                        Descripcion = "Arena limosa con grava"
            elif 4 <= ip <= 7 and ip >= 0.73 * (ll - 20):  # arcilla limosa o limo arcilloso de baja plasticidad
                sucs = "CL-ML"
                if fg < 30:
                    if fg < 15:
                        Descripcion = "Arcilla limosa"
                    elif GF > fa:
                        Descripcion = "Arcilla limosa con grava"
                    else:
                        Descripcion = "Arcilla limosa con arena"
                elif GF > fa:
                    if fa < 15:
                        Descripcion = "Arcilla limo-gravosa"
                    else:
                        Descripcion = "Arcilla limo-gravosa con arena"
                else:
                    if GF < 15:
                        Descripcion = "Arcilla limo-arenosa"
                    else:
                        Descripcion = "Arcilla limo-arenosa con grava"
            else:  # arcilla de baja plasticidad
                sucs = "CL"
                if fg < 30:
                    if fg < 15:
                        Descripcion = "Arcilla de baja plasticidad"
                    elif GF > fa:
                        Descripcion = "Arcilla de baja plasticidad con grava"
                    else:
                        Descripcion = "Arcilla de baja plasticidad con arena"
                elif GF > fa:
                    if fa < 15:
                        Descripcion = "Arcilla gravosa de baja plasticidad"
                    else:
                        Descripcion = "Arcilla gravosa de baja plasticidad con arena"
                else:
                    if GF < 15:
                        Descripcion = "Arcilla arenosa de baja plasticidad"
                    else:
                        Descripcion = "Arcilla arenosa de baja plasticidad con grava"
        else:  # alta plasticidad
            if ip < 0.73 * (ll - 20):  # limo de alta plasticidad
                sucs = "MH"
                if fg < 30:
                    if fg < 15:
                        Descripcion = "Limo de alta plasticidad"
                    elif GF > fa:
                        Descripcion = "Limo de alta plasticidad con grava"
                    else:
                        Descripcion = "Limo de alta plasticidad con arena"
                elif GF > fa:
                    if fa < 15:
                        Descripcion = "Limo gravoso de alta plasticidad"
                    else:
                        Descripcion = "Limo gravoso de alta plasticidad con arena"
                else:
                    if GF < 15:
                        Descripcion = "Limo arenoso de alta plasticidad"
                    else:
                        Descripcion = "Limo arenoso de alta plasticidad con arena"
            else:  # arcilla de alta plasticidad
                sucs = "CH"
                if fg < 30:
                    if fg < 15:
                        Descripcion = "Arcilla de alta plasticidad"
                    elif GF > fa:
                        Descripcion = "Arcilla de alta plasticidad con grava"
                    else:
                        Descripcion = "Arcilla de alta plasticidad con arena"
                elif GF > fa:
                    if fa < 15:
                        Descripcion = "Arcilla gravosa de alta plasticidad"
                    else:
                        Descripcion = "Arcilla gravosa de alta plasticidad con arena"
                else:
                    if GF < 15:
                        Descripcion = "Arcilla arenosa de alta plasticidad"
                    else:
                        Descripcion = "Arcilla arenosa de alta plasticidad con grava"
    return sucs, Descripcion


"""Esta funcion clasifica el suelo mediante el Sistema HRB (AASTHO) y obtiene el índice
de grupo según la Norma ASTM D3282"""


def HRB(p10, p40, p200, ll, lp):
    ip = ll - lp
    a = p200 - 35
    b = p200 - 15
    c = ll - 40
    d = ip - 10

    IG = a * (0.2 + 0.005 * c) + 0.01 * b * d
    if IG <= 0:
        IG = 0
    IG = round(IG)

    if p10 <= 50 and p40 <= 30 and p200 <= 15 and ip <= 6:
        Clasif = "A-1-a"
        IG = 0
        return Clasif, IG
    elif p40 <= 50 and p200 <= 25 and ip <= 6:
        Clasif = "A-1-b"
        IG = 0
        return Clasif, IG
    elif p40 >= 51 and p200 <= 10 and ip == 0:
        Clasif = "A-3"
        IG = 0
        return Clasif, IG
    elif p200 <= 35 and ll <= 40 and ip <= 10:
        Clasif = "A-2-4"
        IG = 0
        return Clasif, IG
    elif p200 <= 35 and ll > 40 and ip <= 10:
        Clasif = "A-2-5"
        IG = 0
        return Clasif, IG
    elif p200 <= 35 and ll <= 40 and ip > 10:
        Clasif = "A-2-6"
        IG = round(0.01 * b * d)
        return Clasif, IG
    elif p200 <= 35 and ll > 40 and ip > 10:
        Clasif = "A-2-7"
        IG = round(0.01 * b * d)
        return Clasif, IG
    elif p200 >= 36 and ll <= 40 and ip <= 10:
        Clasif = "A-4"
        return Clasif, IG
    elif p200 >= 36 and ll > 40 and ip <= 10:
        Clasif = "A-5"
        return Clasif, IG
    elif p200 >= 36 and ll <= 40 and ip > 10:
        Clasif = "A-6"
        return Clasif, IG
    elif p200 >= 36 and ll > 40 and 10 < ip <= (ll - 30):
        Clasif = "A-7-5"
        return Clasif, IG
    elif p200 >= 36 and ll > 40 and ip > 10 and ip > (ll - 30):
        Clasif = "A-7-6"
        return Clasif, IG
