# Taller Django - Videogames Center CRUD

**Autores:**
- **Edwin Vélez**
- **José Díaz**

Proyecto Django con arquitectura **MVT** para la gestión de videojuegos (CRUD completo) persistidos en **SQLite**, con interfaz personalizada usando **Tailwind CSS v4** y una estética inspirada en Cyberpunk 2077 de CDPR.

## Tabla de contenido

1. [Descripción general](#descripción-general)
2. [Tecnologías utilizadas](#tecnologías-utilizadas)
3. [Arquitectura MVT](#arquitectura-mvt)
4. [Estructura del proyecto](#estructura-del-proyecto)
5. [Modelo de datos](#modelo-de-datos)
6. [Flujo CRUD y rutas](#flujo-crud-y-rutas)
7. [Interfaz y estilos](#interfaz-y-estilos)
8. [Instalación y ejecución local](#instalación-y-ejecución-local)
9. [Scripts disponibles](#scripts-disponibles)
10. [Pruebas](#pruebas)
11. [Estado actual](#estado-actual)

## Descripción general

La aplicación permite:

- Listar videojuegos registrados.
- Ver el detalle de un videojuego.
- Crear nuevos videojuegos.
- Editar videojuegos existentes.
- Eliminar videojuegos con confirmación previa.

La persistencia se realiza sobre `db.sqlite3` y el enrutamiento principal del proyecto delega la raíz a la app `videogames`.

## Tecnologías utilizadas

- **Python** (entorno virtual local en `.venv`).
- **Django 6.0.3**.
- **SQLite3** como base de datos local.
- **Tailwind CSS v4.2.2**.
- **@tailwindcss/cli v4.2.2** para compilación de estilos.
- **Templates Django** para render server-side.

## Arquitectura MVT

El proyecto implementa el patrón **Model-View-Template** de Django:

- **Model**: define la estructura de datos (`Videogame`).
- **View**: funciones que manejan lógica de negocio, validaciones y respuestas HTTP.
- **Template**: vistas HTML para representar los datos y formularios al usuario.

Separación concreta en este proyecto:

- **M**: `videogames/models.py`
- **V**: `videogames/views.py`
- **T**: `videogames/templates/videogames/*.html`

## Estructura del proyecto

```text
Taller2Django/
|- architecture/
|  |- settings.py
|  |- urls.py
|  |- asgi.py
|  |- wsgi.py
|- videogames/
|  |- migrations/
|  |  |- 0001_initial.py
|  |- static/css/
|  |  |- input.css
|  |  |- output.css
|  |- templates/videogames/
|  |  |- base.html
|  |  |- list.html
|  |  |- detail.html
|  |  |- form.html
|  |  |- confirm_delete.html
|  |- admin.py
|  |- apps.py
|  |- models.py
|  |- urls.py
|  |- views.py
|  |- tests.py
|- db.sqlite3
|- manage.py
|- package.json
```

## Modelo de datos

Entidad principal: **Videogame**

Campos:

- `id`: `BigAutoField` (PK autogenerada).
- `title`: `CharField(max_length=200)`.
- `description`: `TextField`.
- `launch_date`: `DateField`.

Adicionalmente, `__str__` retorna el título para facilitar visualización en admin y shell.

## Flujo CRUD y rutas

Rutas definidas en `videogames/urls.py`:

- `GET /` -> lista (`videogame_list`).
- `GET /<pk>/` -> detalle (`videogame_detail`).
- `GET|POST /create/` -> creación (`videogame_create`).
- `GET|POST /<pk>/update/` -> actualización (`videogame_update`).
- `GET|POST /<pk>/delete/` -> confirmación y borrado (`videogame_delete`).

Aspectos destacados de implementación:

- Uso de `get_object_or_404` para detalle/edición/eliminación.
- Validación server-side en create/update para evitar registros vacíos aunque falle o se manipule la validación del cliente.
- Eliminación mediante POST (patrón tradicional de Django con formularios HTML).
- Registro del modelo en el admin para gestión manual.

## Interfaz y estilos

La UI usa Tailwind v4 con un enfoque visual cyberpunk/HUD:

- Variables CSS para paleta de colores (`--cp-cyan`, `--cp-yellow`, `--cp-danger`, etc.).
- Efectos visuales: glitch, scanlines, transiciones de reveal y componentes tipo panel terminal.
- Fuentes: `Orbitron` para títulos y tipografía monospace para sensación de consola.
- Diseño responsive con ajustes por breakpoints y grid tipo masonry para tarjetas.

Compilación de estilos:

- Entrada: `videogames/static/css/input.css`
- Salida: `videogames/static/css/output.css`
- Escaneo de templates con `@source "../../templates/**/*.html"`.

## Instalación y ejecución local

### 1. Activar entorno virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Instalar dependencias de Python

```powershell
pip install django
```

### 3. Instalar dependencias de frontend

```powershell
npm install
```

### 4. Compilar CSS

```powershell
npm run build:css
```

### 5. Aplicar migraciones

```powershell
python manage.py migrate
```

### 6. Levantar servidor de desarrollo

```powershell
python manage.py runserver
```

Aplicación disponible en:

- `http://127.0.0.1:8000/`

## Scripts disponibles

Definidos en `package.json`:

- `npm run build:css`: compila y minifica CSS una vez.
- `npm run dev:css`: compila en modo watch para desarrollo.

## Pruebas

Actualmente el archivo `videogames/tests.py` está vacío, por lo que aún no hay cobertura automatizada.

Comando para ejecutar tests cuando existan:

```powershell
python manage.py test
```

## Estado actual

Estado actual:

- CRUD funcional sobre SQLite.
- Separación MVT correcta.
- Integración Tailwind v4 operativa.
- Validaciones básicas server-side en formularios.


