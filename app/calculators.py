import math


def calcular_ibu(alpha_acido, cantidad_g, volumen_l, gravedad_og, tiempo_min):
    if cantidad_g <= 0 or volumen_l <= 0 or tiempo_min <= 0:
        return 0

    fg = max(gravedad_og - 0.015, 1.010) if gravedad_og > 1.050 else 1.010
    bigness_factor = 1.65 * (0.000125 ** (gravedad_og - 1))
    boil_time_factor = (1 - math.exp(-0.04 * tiempo_min)) / 4.15

    utilization = bigness_factor * boil_time_factor

    ibu = (alpha_acido * utilization * cantidad_g * 1000) / (volumen_l * 10)
    return round(ibu * 0.9, 1)


def calcular_abv(og, fg):
    if og is None or fg is None:
        return 0
    return round((og - fg) * 131.25, 1)


def sg_to_plato(sg):
    return (135.997 * sg ** 3 - 630.272 * sg ** 2 + 1111.14 * sg - 616.868)


def plato_to_sg(plato):
    return 1 + (plato / (258.6 - 0.88 * plato))


def calcular_mcu(lovibond, peso_lbs, volumen_gal):
    if volumen_gal <= 0 or lovibond <= 0:
        return 0
    return (lovibond * peso_lbs) / volumen_gal


def calcular_srm_morey(lovibond, peso_lbs, volumen_gal):
    mcu = calcular_mcu(lovibond, peso_lbs, volumen_gal)
    if mcu <= 0:
        return 0
    return round(1.4922 * (mcu ** 0.6859), 1)


def calcular_eficiencia(og, fg_objetivo, volumen):
    pass


def calcular_atenuacion_aparente(og, fg):
    if og is None or fg is None or og <= 1:
        return 0
    return round(((og - fg) / (og - 1)) * 100, 1)


def kg_a_lbs(kg):
    return kg * 2.20462


def litros_a_galones(l):
    return l * 0.264172


def parse_gravedad(valor):
    if valor is None:
        return None
    valor = str(valor).strip()
    if valor.startswith('1.'):
        return float(valor)
    try:
        return float(valor)
    except ValueError:
        return None
