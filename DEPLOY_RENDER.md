# Despliegue en Render

## Pasos para desplegar tu aplicación Django en Render

### 1. Preparar tu repositorio Git

Primero, inicializa un repositorio Git en tu carpeta Puzzle (si no lo has hecho):

```bash
cd Puzzle
git init
git add .
git commit -m "Initial commit - Puzzle Solver Django App"
```

### 2. Subir a GitHub

Crea un repositorio en GitHub y sube tu código:

```bash
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git branch -M main
git push -u origin main
```

### 3. Crear cuenta en Render

1. Ve a [https://render.com](https://render.com)
2. Regístrate o inicia sesión
3. Conecta tu cuenta de GitHub

### 4. Crear nuevo servicio web

1. En el dashboard de Render, haz clic en **"New +"**
2. Selecciona **"Web Service"**
3. En GitHub, busca tu repositorio del Puzzle
4. Conecta el repositorio

### 5. Configurar el servicio

- **Name**: puzzle-solver (o el nombre que prefieras)
- **Environment**: Python 3.11
- **Region**: Elige la más cercana
- **Branch**: main
- **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --no-input`
- **Start Command**: `gunicorn puzzle_project.wsgi:application`

### 6. Agregar variables de entorno

En la sección **"Environment"**, agrega:

```
DEBUG=False
SECRET_KEY=tu-clave-secreta-super-especial-aqui
DATABASE_URL=sqlite:///db.sqlite3
```

Puedes generar una SECRET_KEY segura aquí: https://djecrety.ir/

### 7. Desplegue

Haz clic en **"Create Web Service"**

Render automáticamente:
- Instalará las dependencias de `requirements.txt`
- Ejecutará las migraciones (`python manage.py migrate`)
- Iniciará el servidor con gunicorn
- Asignará una URL pública como: `https://puzzle-solver.onrender.com`

### 8. Actualizaciones futuras

Para actualizar tu aplicación:

```bash
git add .
git commit -m "Actualización del código"
git push origin main
```

Render detectará automáticamente los cambios y redesplegará.

## Archivos incluidos para Render

- **Procfile**: Define cómo ejecutar la aplicación
- **runtime.txt**: Especifica la versión de Python
- **build.sh**: Script de construcción personalizado
- **requirements.txt**: Todas las dependencias necesarias

## Troubleshooting

Si hay errores:

1. Consulta los **Render Logs** en el dashboard
2. Verifica que todas las variables de entorno estén configuradas
3. Asegúrate que el repositorio Git esté sincronizado

¡Tu aplicación estará en línea en minutos! 🚀
