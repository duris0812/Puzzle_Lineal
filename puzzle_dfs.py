# Puzzle lineal con búsqueda en profundidad
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from arbol import Nodo

def buscar_solucuion_DFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    
    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop()
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo)
        
        if nodo.get_datos() == solucion:
            # Solución encontrada
            return nodo, nodos_visitados
        else:
            # Expandir nodos Hijo
            dato_nodo = nodo.get_datos()

            # Operador Izquierdo
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo)
            if not hijo_izquierdo.en_lista(nodos_visitados) and not hijo_izquierdo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo)     

            # Operador Central
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = Nodo(hijo)
            if not hijo_central.en_lista(nodos_visitados) and not hijo_central.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_central)

            # Operador Derecho
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_derecho = Nodo(hijo)
            if not hijo_derecho.en_lista(nodos_visitados) and not hijo_derecho.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecho)   
            
            nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])
    
    return None, nodos_visitados


def obtener_camino(nodo_solucion):
    """
    Obtiene el camino desde el estado inicial hasta la solución
    """
    if nodo_solucion is None:
        return []
    
    resultado = []
    nodo = nodo_solucion
    
    while nodo is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    
    resultado.reverse()
    return resultado
