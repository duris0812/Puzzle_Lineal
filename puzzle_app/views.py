from django.shortcuts import render
from puzzle_dfs import buscar_solucuion_DFS, obtener_camino


def index(request):
    """Página principal con el formulario"""
    resultado = None
    error = None
    
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            estado_inicial_str = request.POST.get('estado_inicial', '').strip()
            solucion_str = request.POST.get('solucion', '').strip()
            
            # Limpiar entrada
            estado_inicial_str = estado_inicial_str.strip('[]').replace(' ', '')
            solucion_str = solucion_str.strip('[]').replace(' ', '')
            
            # Convertir a listas
            estado_inicial = [int(x) for x in estado_inicial_str.split(',')]
            solucion = [int(x) for x in solucion_str.split(',')]
            
            # Validar que sean listas de 4 elementos
            if len(estado_inicial) != 4:
                error = 'El estado inicial debe tener exactamente 4 números'
            elif len(solucion) != 4:
                error = 'El estado objetivo debe tener exactamente 4 números'
            else:
                # Resolver el puzzle
                nodo_solucion, nodos_visitados = buscar_solucuion_DFS(estado_inicial, solucion)
                
                if nodo_solucion is None:
                    error = f'No se encontró solución. Se visitaron {len(nodos_visitados)} nodos.'
                else:
                    # Obtener el camino
                    camino = obtener_camino(nodo_solucion)
                    resultado = {
                        'camino': camino,
                        'pasos': len(camino) - 1,
                        'nodos_visitados': len(nodos_visitados),
                        'encontrado': True
                    }
        
        except ValueError:
            error = 'Ingresa solo números separados por comas. Ej: 4,2,3,1'
        except Exception as e:
            error = f'Error: {str(e)}'
    
    context = {
        'resultado': resultado,
        'error': error
    }
    
    return render(request, 'index.html', context)
