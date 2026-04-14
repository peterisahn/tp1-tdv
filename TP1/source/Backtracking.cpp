#include "Backtracking.h"
#include <vector>
#include <limits>

using namespace std;

static int podas = 0;

 void encontrarSeamBackTracking_aux(const vector<vector<double>>& energia, int fila, int columna, vector<int>& actual, vector<int>& mejor, double& mejorSuma, double sumaActual) {
     int n = energia.size();
     int m = energia[0].size();

    
     actual.push_back(columna);
     sumaActual += energia[fila][columna];

     if(sumaActual >= mejorSuma){
        podas++;
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
     podas = 0;
     vector<int> mejor;
     vector<int> actual;
     double mejorSuma = numeric_limits<double>::infinity();

     // Probar cada columna como punto de partida en la fila 0
     for (int c = 0; c < m; c++) {
         encontrarSeamBackTracking_aux(energia, 0, c, actual, mejor, mejorSuma, 0.0);
     }

     return mejor;
 }

int obtenerPodas() {
    return podas;
}