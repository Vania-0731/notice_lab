
# News Project

Este proyecto consta de dos aplicaciones principales:

1. **News App**: Una plataforma de noticias con artículos, categorías, reporteros y etiquetas.
2. **Profiles App**: Una aplicación de perfiles de usuario que permite a los usuarios gestionar su perfil, guardar artículos, seguir temas y tener un historial de lectura.

## Requisitos

Asegúrate de tener instalados los siguientes requisitos para ejecutar el proyecto:

- Python 3.x
- Django 3.x o superior
- MySQL (si usas base de datos MySQL) o SQLite (si usas la base de datos por defecto de Django)
- Pillow (para manejar imágenes de perfil)

## Instalación

Sigue estos pasos para levantar el proyecto:

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/tu-usuario/proyecto-news.git
   cd proyecto-news
   ```

2. **Instalar las dependencias**:

   Crea un entorno virtual y activa el entorno.

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

   Luego, instala las dependencias con pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar la base de datos**:

   Si estás usando MySQL, asegúrate de configurar tu base de datos en el archivo `settings.py` de Django.

   Para SQLite, no necesitas hacer nada, ya que Django usará una base de datos local por defecto.

4. **Realizar las migraciones**:

   Aplica las migraciones para crear las tablas en la base de datos:

   ```bash
   python manage.py migrate
   ```

5. **Crear un superusuario (opcional)**:

   Si quieres acceder al panel de administración de Django, crea un superusuario:

   ```bash
   python manage.py createsuperuser
   ```

6. **Levantar el servidor de desarrollo**:

   Finalmente, ejecuta el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

   Ahora puedes acceder a la aplicación desde `http://127.0.0.1:8000/`.

## Funcionalidades Principales

### News App

- **Vista de inicio**: Muestra los artículos más recientes.
- **Detalle del artículo**: Muestra el contenido completo de un artículo y artículos relacionados.
- **Categorías**: Navega entre artículos de diferentes categorías.
- **Reporteros**: Visualiza el perfil de los reporteros y sus artículos.
- **Etiquetas**: Filtra artículos por etiquetas.

### Profiles App

- **Registro y login**: Permite a los usuarios registrarse, iniciar sesión y gestionar su perfil.
- **Perfil de usuario extendido**: Los usuarios pueden agregar información como avatar, biografía, ubicación, fecha de nacimiento.
- **Marcadores de artículos**: Los usuarios pueden guardar artículos como favoritos.
- **Seguir temas y reporteros**: Los usuarios pueden seguir categorías y reporteros.
- **Historial de lectura**: Registra los artículos leídos por los usuarios y su progreso de lectura.
- **Preferencias de usuario**: Los usuarios pueden configurar preferencias como notificaciones por correo y modo oscuro.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```
news/
├── migrations/
│   └── __init__.py
├── models.py
├── views.py
├── templates/
│   └── news/
├── urls.py
├── tests.py
profiles/
├── migrations/
│   └── __init__.py
├── models.py
├── views.py
├── templates/
│   └── profiles/
├── urls.py
```
