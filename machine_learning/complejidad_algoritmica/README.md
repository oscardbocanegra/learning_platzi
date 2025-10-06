# Complejidad Algoritmica

Repositorio de ejemplos y pequeñas implementaciones para estudiar la complejidad algorítmica (curso/ejercicios). Los scripts incluidos muestran implementaciones clásicas de búsquedas, ordenamientos, un problema de mochila y utilidades para graficar resultados.

## Estructura de la carpeta

- `busqueda_lineal.py` - Implementación y ejemplo de búsqueda lineal (O(n)).
- `busqueda_binaria.py` - Implementación y ejemplo de búsqueda binaria (O(log n)).
- `ordenamiento_burbuja.py` - Implementación del algoritmo de burbuja (O(n^2)).
- `ordenamiento_mezcla.py` - Implementación del algoritmo merge sort / mezcla (O(n log n)).
- `morral.py` - Implementación del problema de la mochila (knapsack), suele usarse para comparar enfoques voraces/dinámicos.
- `complejidad_algoritmica.py` - Script principal/recopilatorio que puede contener ejemplos o ejecuciones de comparación entre algoritmos.
- `graficado/` - Carpeta con utilidades de graficado.
  - `graficado_simple.py` - Ejemplo para graficar tiempos o curvas de complejidad.
  - `graficado_simple.html` - Salida HTML si se genera una visualización estática.

> Si algún nombre o contenido difiere, verifique los scripts individuales para el comportamiento exacto.

## Requisitos

- Python 3.8 o superior.
- Dependencias opcionales (para graficado):
  - `matplotlib` (si `graficado_simple.py` usa matplotlib u otra librería de graficado).

Puede instalar dependencias con pip si las necesita:

```powershell
# crear un entorno virtual (opcional)
python -m venv .venv; .\.venv\Scripts\Activate.ps1

# instalar matplotlib si lo necesita
pip install matplotlib

# (alternativamente) crear un requirements.txt con las dependencias y ejecutar:
pip install -r requirements.txt
```

## Cómo ejecutar los ejemplos

Ejecute cada script directamente con Python desde la carpeta raíz del proyecto. Ejemplos (PowerShell):

```powershell
# Búsqueda lineal
python .\busqueda_lineal.py

# Búsqueda binaria
python .\busqueda_binaria.py

# Ordenamiento burbuja
python .\ordenamiento_burbuja.py

# Ordenamiento por mezcla (merge sort)
python .\ordenamiento_mezcla.py

# Problema de la mochila
python .\morral.py

# Script recopilatorio / comparaciones
python .\complejidad_algoritmica.py

# Graficado (si requiere matplotlib)
python .\graficado\graficado_simple.py
```

Algunos scripts pueden esperar entradas por consola o tener ejemplos embebidos; abra los archivos para ver cómo proporcionan sus datos de prueba.

## Contrato (rápido)

- Entradas: usualmente listas de números o parámetros simples (tamaños, semilla aleatoria, capacidad para `morral`).
- Salidas: resultados impresos en consola, comparaciones de tiempos y/o archivos de salida (por ejemplo: `graficado_simple.html`).
- Errores: los scripts deben manejar entradas vacías o mal formateadas; revise cada archivo para ampliaciones específicas.

## Casos borde a considerar

- Listas vacías o con un solo elemento.
- Búsqueda de elementos no presentes.
- Datos ya ordenados o inversamente ordenados (peor/caso mejor para algunos algoritmos).
- Para `morral.py`: capacidades cero o items con valor/peso cero.

## Sugerencias y próximos pasos

- Añadir un `requirements.txt` con dependencias exactas si desea reproducibilidad.
- Añadir tests automáticos (por ejemplo, con `unittest` o `pytest`) para validar los algoritmos con casos conocidos.
- Añadir ejemplos de entrada/salida en una carpeta `examples/` para facilitar la experimentación.
- Añadir scripts de benchmarking para medir tiempos y generar las gráficas automáticamente.

