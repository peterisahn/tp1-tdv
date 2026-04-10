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

// // usemos el mio
// void encontrarSeamFuerzaBruta_aux(const vector<vector<double>>& energia, int fila, int col, vector<int>& actual, vector<int>& mejor, double& mejorSuma, double sumaActual) {
//     int n = energia.size();
//     int m = energia[0].size();

//     actual.push_back(col);
//     sumaActual += energia[fila][col];
    
//     if(fila == n - 1){
//         // Caso base: última fila, comparar con el mejor seam encontrado
//         if (sumaActual < mejorSuma) {
//             mejorSuma = sumaActual;
//             mejor = actual;
//         }
//     }else{
//         // Caso recursivo: probar los (hasta 3) vecinos validos en la fila siguiente
//         for(int ady = -1; ady <= 1; ady++){
//             int newCol = col + ady;
//             if(newCol >= 0 && newCol < m){          // solo vecinos dentro de la imagen
//                 encontrarSeamFuerzaBruta_aux(energia, fila + 1, newCol, actual, mejor, mejorSuma, sumaActual);
//             }
//         }
//     }

//     actual.pop_back(); // deshacer para explorar otros caminos
// }

// vector<int> encontrarSeamFuerzaBruta(const vector<vector<double>>& energia) {
//     int m = energia[0].size();

//     vector<int> mejor;
//     vector<int> actual;
//     double mejorSuma = numeric_limits<double>::infinity();

//     // Probar cada columna como punto de partida en la fila 0
//     for (int c = 0; c < m; c++) {
//         encontrarSeamFuerzaBruta_aux(energia, 0, c, actual, mejor, mejorSuma, 0.0);
//     }

//     return mejor;
// }