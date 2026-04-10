#include "ProgramacionDinamica.h"
#include <vector>
#include <tuple>

using namespace std;

/*
5 6
9.0 3.0 1.0 2.0 8.0 7.0
5.0 2.0 0.5 4.0 6.0 3.0
7.0 1.0 2.0 0.8 5.0 4.0
3.0 4.0 1.5 1.0 2.0 6.0
8.0 2.0 3.0 1.5 1.0 5.0

9.0 3.0 1.0
5.0 2.0 0.5
7.0 1.0 2.0
                pepe = 1 --> res = {1}
                vecinos = {2.0, 3.0}
                pepe = pepe + min() - 1
                1 + 0 -1 = 0

{1.0, }
-1  -1  -1
-1  -1  -1
7.0 1.0 2.0

{2,3,3}12.0 4.0 1.0
6.0 3.0 1.5
7.0 1.0 2.0
{3,3,2}
    
*/


// Creamos una función auxiliar que devuelve el valor de la mínima energía entre los vecinos
double minimo_energia(const vector<double>& v){
    // Caso: tiene 2 elementos (vecinos)
    if(v.size() == 2){
        if(v[0] < v[1]){
            return v[0];
        }else{
            return v[1];
        }
    }else{ 
    // Caso: tiene 3 elementos (vecinos)
        if(v[0] <= v[1]){
            if(v[0] <= v[2]){
                return v[0];
            }else{
                return v[2];
            }
        }else{
            if(v[1]<=v[2]){
                return v[1];
            }else{
                return v[2];
            }
        }
    }
}

// Función Auxiliar: Toma la columna actual y rellena los valores de energía de la celda actual y de sus vecinos en el Memo. Recorre los vecinos recursivamente.
void encontrarSeamPD_aux(const vector<vector<double>>& energia, int fila, int columna, vector<vector<double>>& M) { // Creamos el memo utilizando el método de Top-Down
    int n = energia.size();     // n es cantidad de filas
    int m = energia[0].size();  // m es cantidad de columnas
    
    // Caso Base: llegamos a la última fila
    if(fila == n-1){
        return;
    }else if(M[fila][columna] != -1){ 
        return;
    }else{

        // Caso recursivo: probar los vecinos (a lo sumo 3) validos en la fila siguiente

        // Creamos un vector donde guardamos las energías de los vecinos adyacentes
        vector<double> vecinos_adyacentes;

        // Recorremos los vecinos adyacentes de la celda actual
        for(int columna_adyacente = -1; columna_adyacente <= 1; columna_adyacente++){
            int siguiente_columna = columna + columna_adyacente;
            // Si la siguiente columna (de la siguiente fila) a procesar se encuentra en un rango válido
            if(siguiente_columna >= 0 && siguiente_columna < m){
                encontrarSeamPD_aux(energia, fila+1, siguiente_columna, M);
                // Agregamos a vecinos_adyacentes los valores de energía de sus vecinos, que los obtuvimos en la recursión
                vecinos_adyacentes.push_back(M[fila+1][siguiente_columna]);
            }
        }
        // Actualizamos la celda i,j del Memo como el valor guardado de la posición i,j en energía, más la mínima energía entre sus vecinos
        M[fila][columna] = energia[fila][columna] + minimo_energia(vecinos_adyacentes);
    }
}

// Función Auxiliar: Recorre el Memo y agrega a res los índices de las columnas con los mínimos valores de energía para cada fila
void reconstruccion_res(const vector<vector<double>>& energia, vector<vector<double>>& M, vector<int>& res){
    int n = energia.size();     // n es cantidad de filas
    int m = energia[0].size();  // m es cantidad de columnas

    // Buscamos la columna que contiene la menor energía en la primer fila del Memo
    // Inicializamos minima_energia e indice de la primer fila
    double minima_energia = M[0][0];
    int indice = 0;
    // Recorremos la primer fila y buscamos el mínimo
    for(int j=1;j<m;j++){               
        if(minima_energia > M[0][j]){
            minima_energia = M[0][j];
            indice = j;
        }
    }
    
    // Agregamos el índice que encontramos (correspondiente a la primer fila) a res
    res.push_back(indice); 

    // Recorremos el resto de filas
    for(int i=1; i<n; i++){
        // Inicializamos mejor_valor, mejor_columna para guardar los valores relacionados a los vecinos
        double mejor_valor = 1e8;
        int mejor_columna = -1;
        // Recorremos los vecinos adyacentes de la celda actual
        for(int columna_adyacente = -1; columna_adyacente <= 1; columna_adyacente++){
            int siguiente_columna = indice + columna_adyacente;
            // Evaluamos si la siguiente columna a procesar cumple que está dentro del rango válido y si es menor al mejor valor (mínima energía) guardado entre sus vecinos
            if(siguiente_columna >= 0 && siguiente_columna < m && M[i][siguiente_columna] < mejor_valor){
                // Actualizamos mejor_valor, mejor_columna
                mejor_valor = M[i][siguiente_columna];
                mejor_columna = siguiente_columna;
            }
        }
        // Una vez que tenemos el índice de la mejor columna , actualizamos índice y lo agregamos a res
        indice = mejor_columna;
        res.push_back(indice);
    }
    return;
}

// Función Principal
vector<int> encontrarSeamPD(const vector<vector<double>>& energia){
    int n = energia.size();      // n es cantidad de filas
    int m = energia[0].size();   // m es cantidad de columnas

    // Creamos el Memo
    vector<vector<double>> M;

    // Recorremos hasta la anteúltima fila del Memo e inicializamos los celdas con -1
    for(int i=0;i<n-1;i++){
        vector<double> fila;
        for(int j=0;j<m;j++){
            fila.push_back(-1);
        }
        M.push_back(fila);  
    }
    // En la última fila del Memo copiamos la última fila de energía
    M.insert(M.end(), energia.back());
    

    // Recorre las columnas de la primer fila para llenar el Memo por columna y recorrer así todas las caminos  
    for (int c = 0; c < m; c++) {
        // Llama a la función encontrarSeamPD_aux que rellena la columna actual del Memo y todos los vecinos que son alcanzables desde esta columna
        encontrarSeamPD_aux(energia, 0, c, M);
    }
    
    // Inicializamos res, que es el vector que contiene los índices de las columnas con los mínimos valores de energía para cada fila
    vector<int> res;
    // Llamamos a la función reconstrucción_res, que agrega los índices a res
    reconstruccion_res(energia, M, res);

    // Devolvemos la solución final
    return res;
}
