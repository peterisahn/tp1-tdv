#include <iostream>
#include "FuerzaBruta.h"
#include <vector>

using namespace std;

// Algoritmo Fuerza Bruta
double FuerzaBruta(const vector<vector<double>>& energia, int fila, int columna, vector<int>& res) {
    int n = energia.size();     // n es cantidad de filas
    int m = energia[0].size();  // m es cantidad de columnas

    // Caso base: Si estamos en la ultima fila, retornamos el valor de energía de la celda
    if (fila == n - 1) {
        // Agregamos el índice de la columna al vector res
        res.push_back(columna);
        return energia[fila][columna];
    }

    // Caso General / Recursivo: 
    int infinito = INT_MAX;     // Inicializamos la variable infinito (con la forma vista en clase)
    double mejor_costo = infinito; //Inicializamos mejor_costo, que se va actualizando a medida que encuentre un menor costo de energía

    // El ciclo recorre (hasta) los 3 vecinos de la celda actual, que se encuentran en la siguiente fila
    int i = -1;
    while(i <= 1){
        int siguiente_columna = columna + i;
        // Chequeamos si se encuentra en un rango válido de la matriz
        if (siguiente_columna >= 0 && siguiente_columna < m) { 
            vector<int> res_actual;     // Iniciailizamos res_actual, que contiene los indices (columnas) del camino explorado a partir de la siguiente fila
           
            // Llamamos a la recursión, que nos devuelve el menor costo acumulado entre sus vecinos y se lo asignamos a costo
            double costo = FuerzaBruta(energia, fila + 1, siguiente_columna, res_actual);

            // Si el costo que encontramos es mejor que el mejor_costo que teníamos, actualizamos mejor_costo y res
            if (costo < mejor_costo) { 
                mejor_costo = costo;
                res = res_actual;
            }
        }
        i = i + 1;
    }
    // Una vez que recorrimos los vecinos, agregamos la columna actual al inicio
    res.insert(res.begin(), columna); 
    // Devolvemos la energía de la celda actual más el mejor_costo encontrado
    return energia[fila][columna] + mejor_costo;
}

// Función principal
vector<int> encontrarSeamFuerzaBruta(const vector<vector<double>>& energia) {
    // Inicializamos m como tamaño de fila (o cantidad de columnas)
    int m = energia[0].size();
    // Inicializamos mejor_costo
    double mejor_costo = INT_MAX;
    // Inicializamos el vector mejor_seam, que contiene la mejor solución encontrada hasta el momento
    vector<int> mejor_seam;

    // Recorremos las columnas de la primera fila para identificar desde qué columna obtenemos la mejor solución
    for (int j = 0; j < m; j++) {
        vector<int> actual_seam;   // Inicializamos el vector seam
        double costo = FuerzaBruta(energia, 0, j, actual_seam); //Llamamos a la función FuerzaBruta que devuelve el costo total acumulado de haber empezado por esa columna
        // Si el costo que encontramos es mejor que el mejor_costo que teníamos, actualizamos mejor_costo y mejor_seam
        if (costo < mejor_costo) {
            mejor_costo = costo;
            mejor_seam = actual_seam;
        }
    }
    // Devolvemos mejor_seam, que tiene la solución final
    return mejor_seam;
}
