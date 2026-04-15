#include <iostream>
#include "Backtracking.h"
#include <vector>


using namespace std;

static int podas = 0;

// Algoritmo Backtracking
 void encontrarSeamBackTracking_aux(const vector<vector<double>>& energia, int fila, int columna, vector<int>& actual_seam, vector<int>& mejor_seam, double& mejor_suma, double suma_actual) {
     int n = energia.size();    // n es cantidad de filas
     int m = energia[0].size(); // m es cantidad de columnas

    // Agregamos el índice de la columna actual a actual_seam
     actual_seam.push_back(columna);
    // Actualizamos suma_actual, más el valor de la celda actual
     suma_actual += energia[fila][columna];

    // Evaluamos la condición si suma_actual es mayor que la mejor_suma hasta el momento (Caso que queremos evitar)
     if(suma_actual >= mejor_suma){
        // Encontramos una poda
        podas++;
        // Eliminamos el indice actual
         actual_seam.pop_back();
         return;
    // Caso Base: Llegamos hasta última fila, por ende 'pasó' la prueba de las podas
     }else if(fila == n - 1){
        // Actualizamos mejor_suma y mejor_seam
         mejor_suma = suma_actual;   
         mejor_seam = actual_seam;
     }else{
         // Caso Recursivo:
         // Recorremos (hasta) los 3 vecinos de la celda actual, que están en la siguiente fila
         for(int adyacentes = -1; adyacentes <= 1; adyacentes++){
             int siguiente_columna = columna + adyacentes;
            // Chequeamos si se encuentra en un rango válido de la matriz
             if(siguiente_columna >= 0 && siguiente_columna < m){ 
                // Llamamos a la recursión con la siguiente fila
                encontrarSeamBackTracking_aux(energia, fila + 1, siguiente_columna, actual_seam, mejor_seam, mejor_suma, suma_actual);
             }
         }
     }

     actual_seam.pop_back(); // Implica hacer backtracking. Es decir, deshacer la decisión de elegir esa columna para probar con la siguiente columna adyacente
     return;
 }

 // Función Principal
 vector<int> encontrarSeamBacktracking(const vector<vector<double>>& energia) {
    // Inicializamos m como tamaño de fila (o cantidad de columnas)
     int m = energia[0].size();
     // Inicializamos con 0 podas
     podas = 0;

     // Inicializamos mejor_seam y actual_seam, que contendrán los índices
     vector<int> mejor_seam;
     vector<int> actual_seam;

    // Inicializamos mejor_suma con valor infinito
    int infinito = INT_MAX; // Inicializamos la variable infinito (con la forma vista en clase)    
    double mejor_suma = infinito;

    // Recorremos las columnas de la primera fila para identificar desde qué columna obtenemos la mejor solución
     for (int c = 0; c < m; c++) {
         encontrarSeamBackTracking_aux(energia, 0, c, actual_seam, mejor_seam, mejor_suma, 0.0);
     }

     // Devolvemos mejor_seam, con la solución final
     return mejor_seam;
 }

int obtenerPodas() {
    return podas;
}