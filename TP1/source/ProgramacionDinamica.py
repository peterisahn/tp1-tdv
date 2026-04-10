def minimo_energia(v):
    # Caso: tiene 2 elementos (vecinos)
    if len(v) == 2:
        return v[0] if v[0] < v[1] else v[1]
    else:
        # Caso: tiene 3 elementos (vecinos)
        if v[0] <= v[1]:
            return v[0] if v[0] <= v[2] else v[2]
        else:
            return v[1] if v[1] <= v[2] else v[2]


def encontrar_seam_pd_aux(energia, fila, columna, M):
    n = len(energia)
    m = len(energia[0])

    # Caso Base: llegamos a la última fila
    if fila == n - 1:
        return 
    elif M[fila][columna] != -1:
        return 
    else:
        # Caso recursivo: probar los vecinos válidos en la fila siguiente
        vecinos_adyacentes = []

        for columna_adyacente in range(-1, 2):
            siguiente_columna = columna + columna_adyacente
            if 0 <= siguiente_columna < m:
                encontrar_seam_pd_aux(energia, fila + 1, siguiente_columna, M)
                vecinos_adyacentes.append(M[fila+1][columna])    
        M[fila][columna] = energia[fila][columna] + minimo_energia(vecinos_adyacentes)


def reconstruccion_res(energia, M, res):
    n = len(energia)
    m = len(energia[0])

    # Buscamos la columna con menor energía en la primera fila del Memo
    minima = M[0][0]
    indice = 0
    for j in range(1, m):
        if minima > M[0][j]:
            minima = M[0][j]
            indice = j

    res.append(indice)

    # Recorremos el resto de filas
    for i in range(1, n):
        mejor_valor = 1e8
        mejor_columna = -1
        for columna_adyacente in range(-1, 2):
            siguiente_columna = indice + columna_adyacente
            if 0 <= siguiente_columna < m and M[i][siguiente_columna] < mejor_valor:
                mejor_valor = M[i][siguiente_columna]
                mejor_columna = siguiente_columna
        indice = mejor_columna
        res.append(indice)


def encontrar_seam_pd(energia):
    n = len(energia)
    m = len(energia[0])

    # Creamos el Memo: filas 0..n-2 inicializadas en -1, última fila = última fila de energía
    M = [[-1.0] * m for _ in range(n - 1)]
    M.append(energia[n - 1][:])  # copia de la última fila

    # Rellenamos el Memo empezando desde cada columna de la primera fila
    for c in range(m):
        encontrar_seam_pd_aux(energia, 0, c, M)

    res = []
    reconstruccion_res(energia, M, res)
    return res
