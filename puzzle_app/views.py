from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from puzzle_dfs import buscar_solucuion_DFS, obtener_camino
import json


def index(request):
    """Página principal con el formulario"""
    return render(request, 'index.html')


@csrf_exempt
def resolver_puzzle(request):
    """Vista para resolver el puzzle"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Parse del estado inicial
            estado_inicial_str = data.get('estado_inicial', '')
            solucion_str = data.get('solucion', '')
            
            # Convertir strings a listas
            estado_inicial = eval(estado_inicial_str)
            solucion = eval(solucion_str)
            
            # Validar que sean listas de 4 elementos
            if not isinstance(estado_inicial, list) or len(estado_inicial) != 4:
                return JsonResponse({
                    'error': 'El estado inicial debe ser una lista de 4 elementos',
                    'success': False
                })
            
            if not isinstance(solucion, list) or len(solucion) != 4:
                return JsonResponse({
                    'error': 'El nodo solución debe ser una lista de 4 elementos',
                    'success': False
                })
            
            # Resolver el puzzle
            nodo_solucion, nodos_visitados = buscar_solucuion_DFS(estado_inicial, solucion)
            
            if nodo_solucion is None:
                return JsonResponse({
                    'error': 'No se encontró solución para el puzzle',
                    'success': False,
                    'nodos_visitados': len(nodos_visitados)
                })
            
            # Obtener el camino
            camino = obtener_camino(nodo_solucion)
            
            return JsonResponse({
                'success': True,
                'camino': camino,
                'pasos': len(camino) - 1,
                'nodos_visitados': len(nodos_visitados),
                'encontrado': True
            })
        
        except ValueError as e:
            return JsonResponse({
                'error': f'Error al parsear los datos: {str(e)}',
                'success': False
            })
        except Exception as e:
            return JsonResponse({
                'error': f'Error en la búsqueda: {str(e)}',
                'success': False
            })
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)
