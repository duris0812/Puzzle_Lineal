# Puzzle Solver - DFS

Sistema web para resolver puzzles lineales usando búsqueda en profundidad (DFS).

## Características

✨ Frontend interactivo con Django
🧩 Algoritmo DFS para resolver puzzles
📊 Visualización de estadísticas (pasos, nodos visitados)
🚀 Listo para desplegar en Render

## Instalación Local

### Requisitos
- Python 3.11+
- pip

### Pasos

1. **Navega a la carpeta Puzzle**:
```bash
cd Puzzle
```

2. **Instala las dependencias**:
```bash
pip install -r requirements.txt
```

3. **Ejecuta las migraciones**:
```bash
python manage.py migrate
```

4. **Inicia el servidor**:
```bash
python manage.py runserver
```

5. **Abre tu navegador**:
```
http://localhost:8000
```

## Uso

1. Ingresa el **Estado Inicial** como una lista de 4 números (ej: `[4, 2, 3, 1]`)
2. Ingresa el **Nodo Solución** como una lista de 4 números (ej: `[1, 2, 3, 4]`)
3. Haz clic en "Resolver Puzzle"
4. Visualiza:
   - El camino completo desde el estado inicial hasta la solución
   - Número de pasos necesarios
   - Número de nodos visitados

## Despliegue en Render 🚀

Para desplegar tu aplicación en Render, lee el archivo **[DEPLOY_RENDER.md](DEPLOY_RENDER.md)** con instrucciones paso a paso.

O resume rápido:
1. Sube el código a GitHub
2. Conecta Render a tu repositorio
3. Configura las variables de entorno
4. ¡Listo! Tu app estará en línea

## Estructura del Proyecto

```
Puzzle/
├── manage.py                      # Gestor de Django
├── Procfile                       # Configuración para Render
├── runtime.txt                    # Versión de Python
├── requirements.txt               # Dependencias
├── build.sh                       # Script de construcción
├── .gitignore                     # Archivos a ignorar en Git
├── README.md                      # Este archivo
├── DEPLOY_RENDER.md              # Guía de despliegue
├── arbol.py                       # Clase Nodo
├── puzzle_dfs.py                 # Algoritmo DFS
├── puzzle_project/               # Configuración Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── puzzle_app/                   # Aplicación principal
    ├── views.py
    ├── urls.py
    ├── models.py
    ├── apps.py
    └── templates/
        └── index.html            # Frontend interactivo
```

## Algoritmo DFS

### Funcionamiento
- Usa una **pila** para explorar el espacio de búsqueda
- Expande **tres operadores** por nodo:
  - **Izquierdo**: Intercambia posiciones 0 y 1
  - **Central**: Intercambia posiciones 1 y 2
  - **Derecho**: Intercambia posiciones 2 y 3

### Características
- ✓ Evita nodos visitados
- ✓ Evita ciclos en la frontera
- ✓ Reconstruye el camino completo
- ✓ Retorna estadísticas de búsqueda

## Ejemplo

**Input:**
```
Estado Inicial: [4, 2, 3, 1]
Objetivo:       [1, 2, 3, 4]
```

**Output:**
```
Pasos: 4
Nodos Visitados: 12
Camino:
  Paso 0: [4, 2, 3, 1]
  Paso 1: [2, 4, 3, 1]
  Paso 2: [2, 3, 4, 1]
  Paso 3: [2, 3, 1, 4]
  Paso 4: [1, 2, 3, 4]  ✓ SOLUCIÓN
```

## Tecnologías

- **Backend**: Django 6.0.3
- **Server**: Gunicorn (producción)
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Despliegue**: Render (PaaS)

## Contacto & Créditos

Desarrollado como proyecto educativo para la clase de Autómatas II.

---

**¿Necesitas ayuda?** Consulta la guía de despliegue: [DEPLOY_RENDER.md](DEPLOY_RENDER.md)
