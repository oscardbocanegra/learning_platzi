# Manejo de Datos Faltantes

Este proyecto tiene como objetivo explorar y manejar datos faltantes en conjuntos de datos utilizando herramientas de análisis de datos en Python. El proyecto incluye ejemplos prácticos y una librería personalizada para facilitar el análisis exploratorio de datos (EDA).

## Estructura del Proyecto

```
.
├── diabetes.csv                # Conjunto de datos de ejemplo
├── manejo_datos_faltantes.ipynb # Notebook con ejemplos prácticos
├── riskfactors.rda             # Archivo de datos en formato R
├── libreria_eda/               # Librería personalizada para EDA
│   ├── README.md               # Documentación de la librería
│   ├── requirements.txt        # Dependencias de la librería
│   ├── setup.py                # Script de instalación de la librería
│   ├── build/                  # Archivos generados durante la construcción
│   │   ├── bdist.win-amd64/    # Archivos binarios
│   │   └── lib/                # Código fuente compilado
│   │       └── libreria_eda/   # Código fuente de la librería
│   │           └── __init__.py
│   ├── libreria_eda/           # Código fuente de la librería
│   │   └── __init__.py
│   └── libreria_eda.egg-info/  # Metadatos de la librería
│       ├── dependency_links.txt
│       ├── PKG-INFO
│       ├── requires.txt
│       ├── SOURCES.txt
│       └── top_level.txt
```

## Requisitos

- Python 3.8 o superior
- Entorno virtual configurado (recomendado)
- Librerías necesarias (ver `requirements.txt` en la carpeta `libreria_eda`)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd manejo_datos_faltantes
   ```

3. Activa el entorno virtual:
   ```bash
   # En Windows
   .\venv\Scripts\activate
   ```

4. Instala las dependencias:
   ```bash
   pip install -r libreria_eda/requirements.txt
   ```

5. Instala la librería personalizada:
   ```bash
   pip install -e libreria_eda/
   ```

## Uso

- Abre el archivo `manejo_datos_faltantes.ipynb` para explorar ejemplos prácticos de manejo de datos faltantes.
- Utiliza la librería `libreria_eda` para realizar análisis exploratorio de datos.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para sugerir mejoras o reportar problemas.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.