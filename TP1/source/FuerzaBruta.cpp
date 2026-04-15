#include <iostream>
#include "FuerzaBruta.h"
#include <vector>

using namespace std;

double FuerzaBruta(const vector<vector<double>>& energia, int fila, int col, vector<int>& res) {
    int n = energia.size();
    int m = energia[0].size();

    // Caso base. Si ya estamos en la ultima columna, retornar su valor.
    if (fila == n - 1) {
        res.push_back(col);
        return energia[fila][col];
    }
    int infinito = INT_MAX; // forma utilizada para poner infinito como vimos en clase
    double mejorCosto = infinito;

    // Explorar los 3 vecinos de la fila siguiente
    int i = -1;
    while(i <= 1){
        int nextCol = col + i;
        if (nextCol >= 0 && nextCol < m) { // esta dentro de la matriz
            vector<int> resAct;
            double costo = FuerzaBruta(energia, fila + 1, nextCol, resAct);
            if (costo < mejorCosto) {
                mejorCosto = costo;
                res = resAct;
            }
        }
        i = i + 1;
    }
    
    res.insert(res.begin(), col); // agrego columna actual al inicio
    return energia[fila][col] + mejorCosto;
}

// prueba todas las columnas de la fila 0 para saber desde que columna hacer el corte
vector<int> encontrarSeamFuerzaBruta(const vector<vector<double>>& energia) {
    int m = energia[0].size();
    double mejorCosto = INT_MAX;
    vector<int> mejorSeam;

    for (int j = 0; j < m; j++) {
        vector<int> seam;
        double costo = FuerzaBruta(energia, 0, j, seam);
        if (costo < mejorCosto) {
            mejorCosto = costo;
            mejorSeam = seam;
        }
    }

    return mejorSeam;
}
