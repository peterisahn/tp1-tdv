from math import inf


def back_tracking(energia, fila, col, costo_acum, mejor_costo):
    """
    Retorna (costo_minimo_desde_aqui, camino) desde (fila, col) hasta la última fila.
    mejor_costo[0] es la poda global.
    """
    n = len(energia)
    m = len(energia[0])

    costo_acum += energia[fila][col]

    # Poda: si el acumulado ya supera o iguala el mejor conocido, cortar
    if costo_acum >= mejor_costo[0]:
        return inf, []

    # Caso base
    if fila == n - 1:
        mejor_costo[0] = costo_acum
        return energia[fila][col], [col]

    mejor_costo_actual = inf
    mejor_sub_res = []

    i = -1
    while i <= 1:
        next_col = col + i
        if 0 <= next_col < m:
            costo, res_act = back_tracking(energia, fila + 1, next_col, costo_acum, mejor_costo)
            if costo < mejor_costo_actual:
                mejor_costo_actual = costo
                mejor_sub_res = res_act
        i += 1

    return energia[fila][col] + mejor_costo_actual, [col] + mejor_sub_res


def encontrar_seam_backtracking(energia):
    m = len(energia[0])
    mejor_costo = [inf]  # lista para simular paso por referencia
    mejor_res = []
    mejor_total = inf

    for j in range(m):
        costo, res = back_tracking(energia, 0, j, 0, mejor_costo)
        if costo < mejor_total:
            mejor_total = costo
            mejor_res = res

    return mejor_res



# URL chat con IA --> https://claude.ai/share/9d32cc2f-64eb-4dfb-bde7-6c8ddefafdde