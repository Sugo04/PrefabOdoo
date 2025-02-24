# Prefab Odoo

## Introducción
Durante el desarrollo de este módulo, hemos observado que muchos laboratorios abordan técnicamente los mismos archivos de manera repetitiva. No lo consideramos una mera práctica, ya que en ocasiones se han utilizado archivos nuevos (como en el **Laboratorio 56**).

Con el objetivo de prepararme para el examen de desarrollo de módulos en Odoo, he decidido crear esta plantilla. Su propósito es proporcionar una estructura organizada y datos relevantes para facilitar el desarrollo en Odoo.

## Estructura del Proyecto
El proyecto sigue la siguiente estructura de archivos y carpetas:

```
.
├── __init__.py
├── __manifest__.py
├── models
│   ├── archivo_principal.py
│   └── __init__.py
├── README.md
├── security
│   └── ir.model.access.csv
├── static
│   ├── description
│   │   └── icon53.png
│   └── src
└── views
    └── archivo_principal_views.xml
```

### Descripción de Archivos y Carpetas

- `__init__.py`: Permite que el directorio sea tratado como un módulo de Python.
- `__manifest__.py`: Archivo de definición del módulo, donde se establecen metadatos como nombre, versión, dependencias y archivos incluidos.
- `models/`: Contiene la lógica de negocio del módulo.
  - `archivo_principal.py`: Define los modelos de datos y su comportamiento.
  - `__init__.py`: Importa los modelos del módulo.
- `views/`: Contiene las vistas XML para la interfaz de usuario.
  - `archivo_principal_views.xml`: Define la estructura y comportamiento de las vistas.
- `security/`: Contiene configuraciones de acceso y seguridad.
  - `ir.model.access.csv`: Define los permisos de acceso a los modelos.
- `static/`: Archivos estáticos del módulo.
  - `description/icon53.png`: Icono del módulo.
  - `src/`: Carpeta para otros recursos estáticos como CSS, JavaScript o imágenes adicionales.

