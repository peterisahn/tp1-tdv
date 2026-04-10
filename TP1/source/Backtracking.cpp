#include "Backtracking.h"
#include <vector>
#include <limits>

using namespace std;


 void encontrarSeamBackTracking_aux(const vector<vector<double>>& energia, int fila, int columna, vector<int>& actual, vector<int>& mejor, double& mejorSuma, double sumaActual) {
     int n = energia.size();
     int m = energia[0].size();

    
     actual.push_back(columna);
     sumaActual += energia[fila][columna];

     if(sumaActual >= mejorSuma){
         actual.pop_back();
         return;
     }else if(fila == n - 1){
         mejorSuma = sumaActual;   // ya sabemos que es menor porque sino hubiera entrado en la poda de optimalidad
         mejor = actual;
     }else{
         // Caso recursivo: probar los (hasta 3) vecinos validos en la fila siguiente
         for(int adyacentes = -1; adyacentes <= 1; adyacentes++){
             int siguiente_columna = columna + adyacentes;
             if(siguiente_columna >= 0 && siguiente_columna < m){          // solo vecinos dentro de la imagen
                 encontrarSeamBackTracking_aux(energia, fila + 1, siguiente_columna, actual, mejor, mejorSuma, sumaActual);
             }
         }
     }

     actual.pop_back(); // backtrack
     return;
 }

 vector<int> encontrarSeamBacktracking(const vector<vector<double>>& energia) {
     int m = energia[0].size();

     vector<int> mejor;
     vector<int> actual;
     double mejorSuma = numeric_limits<double>::infinity();

     // Probar cada columna como punto de partida en la fila 0
     for (int c = 0; c < m; c++) {
         encontrarSeamBackTracking_aux(energia, 0, c, actual, mejor, mejorSuma, 0.0);
     }

     return mejor;
 }


// --------------

//#include <iostream>
//#include "FuerzaBruta.h"
//#include <vector>
//#include <climits>
//using namespace std;
//
//double BackTracking(const vector<vector<double>>& energia, int fila, int col, vector<int>& res, double costoAcum, double& mejorCosto) {
//    int n = energia.size();
//    int m = energia[0].size();
//
//    costoAcum += energia[fila][col];
//    if (costoAcum >= mejorCosto) return INT_MAX;
//
//    // Caso base  
//    if (fila == n - 1) {
//        res.push_back(col);
//        mejorCosto = costoAcum; 
//        return energia[fila][col];
//    }
//    int infinito = INT_MAX;
//    double mejorCostoActual = infinito;
//
//    // Explorar los 3 vecinos de la fila siguiente
//    int i = -1;
//    while(i <= 1){
//    
//        int nextCol = col + i;
//        if (nextCol >= 0 && nextCol < m) {
//            vector<int> resAct;
//            double costo = BackTracking(energia, fila + 1, nextCol, resAct, costoAcum, mejorCosto);
//            if (costo < mejorCostoActual) {
//                mejorCostoActual = costo;
//                res = resAct;
//            }
//        }
//        i = i + 1;
//    }
//
//    res.insert(res.begin(), col); // agrego columna actual al inicio
//    return energia[fila][col] + mejorCostoActual;
//}
//
//// Función principal: prueba todas las columnas de la fila 0
//vector<int> encontrarSeamBacktracking(const vector<vector<double>>& energia) {
//    int m = energia[0].size();
//    double mejorCosto = INT_MAX;
//    vector<int> mejorRes;
//
//    for (int j = 0; j < m; j++) {
//        vector<int> res;
//        double costo = BackTracking(energia, 0, j, res, 0, mejorCosto);
//        if (costo < mejorCosto) {
//            mejorCosto = costo;
//            mejorRes = res;
//        }
//    }
//
//    return mejorRes;
//}