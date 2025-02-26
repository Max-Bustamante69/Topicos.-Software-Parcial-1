# Topicos.-Software-Parcial-1

Repositorio que tiene como objetivo la presentación y entrega del parcial #1 de la materia de Tópicos Especializados en Software en EAFIT.

## Descripción

Este proyecto es una aplicación web para gestionar la información de vuelos en la ciudad de Rionegro. Permite registrar, listar y obtener estadísticas de vuelos nacionales e internacionales.


## Instalación

1. Clona el repositorio:

    ```sh
    git clone https://github.com/tu-usuario/Topicos-Software-Parcial-1.git
    cd Topicos-Software-Parcial-1
    ```

2. Crea y activa un entorno virtual:

    ```sh
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias del proyecto:

    ```sh
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

## Uso

1. Inicia el servidor de desarrollo de Django:

    ```sh
    python manage.py runserver
    ```

2. Abre tu navegador y navega a `http://127.0.0.1:8000` para ver la aplicación en funcionamiento.

## Funcionalidades

- **Registrar Vuelo**: Permite registrar un nuevo vuelo con su nombre, tipo (Nacional o Internacional) y precio.
- **Listar Vuelos**: Muestra una lista de todos los vuelos registrados siguiendo especificaciones dadas por el profesor.
- **Estadísticas de Vuelos**: Proporciona estadísticas sobre el número de vuelos nacionales e internacionales y el precio promedio de los vuelos nacionales.

## Estructura del Proyecto

- [vuelos]: Contiene la aplicación principal.
  - `models.py`: Define los modelos de la base de datos.
  - `views.py`: Contiene las vistas de la aplicación.
  - `forms.py`: Define los formularios utilizados en la aplicación.
  - `templates/`: Contiene las plantillas HTML.
    - `base.html`: Plantilla base para la aplicación.
    - `registrar_vuelo.html`: Plantilla para registrar un nuevo vuelo.
    - `listar_vuelos.html`: Plantilla para listar los vuelos.
    - `estadisticas_vuelos.html`: Plantilla para mostrar las estadísticas de los vuelos.