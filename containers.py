"""Este script busca el número de pesafiltro en la base de datos de calibración y devuelve
el peso del pesafiltro según su numero. Valido para pesafiltros de campo"""


def pesafiltros_campo(num_pf):
    import pandas as pd
    pesafiltros_df = pd.read_csv('C:\\Python\\laboratorio\\pesafiltros_campo.csv')
    pf_campo = list(pesafiltros_df['pesafiltro'])
    pesos_campo = list(pesafiltros_df['peso'])
    zip_obj = zip(pf_campo, pesos_campo)
    diccionario = dict(zip_obj)
    peso = diccionario[num_pf]
    return peso


"""Este script busca el número de pesafiltro en la base de datos de calibración y devuelve
el peso del pesafiltro según su numero. Valido para pesafiltros de laboratorio"""


def pesafiltros_lab(num_pf):
    import pandas as pd
    pesafiltros_df = pd.read_csv('C:\\Python\\laboratorio\\pesafiltros_laboratorio.csv')
    pf_lab = list(pesafiltros_df['pesafiltro'])
    pesos_lab = list(pesafiltros_df['peso'])
    zip_obj = zip(pf_lab, pesos_lab)
    diccionario = dict(zip_obj)
    peso = diccionario[num_pf]
    return peso
