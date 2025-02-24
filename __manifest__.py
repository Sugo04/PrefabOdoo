{
    "name": "[Nombre de tu módulo]",
    "version": "1.0", # Versión del módulo
    "summary": "[Breve resumen de tu módulo]",
    "category": "Productivity", # categoría del módulo
    "author": "[Tu nombre]",
    "website": "https://tuweb.com",
    "license": "LGPL-3",
    "depends": ["base", "mail"], # este módulo dependerá de:
    "icon": "[Ruta al icono de tu módulo]", # Generalmente static/description/icon.png
    "data": [
        "[Ruta al views de tu módulo]",
        "[security/ir.model.access.csv]" # ruta al archivo de seguridad
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}