# Redes Neuronales - Proyecto de aprendizaje (Platzi)

## Información del proyecto

- **Nombre**: Redes Neuronales - Practicas con TensorFlow / Keras
- **Resumen**: Colección de notebooks, modelos preentrenados, y datasets orientados al reconocimiento de imágenes (ej. lenguaje de señas). Incluye ejemplos de carga de múltiples datasets, entrenamiento con checkpoints y resultados de Keras Tuner.
- **Objetivos**:
  - Proveer notebooks reproducibles para entrenar y evaluar modelos de clasificación de imágenes.
  - Enseñar el flujo completo: carga de datos, preprocesamiento, definición de modelos, entrenamiento con checkpoints, evaluación y guardado de modelos (`.h5`).
  - Facilitar experimentación con `keras-tuner` y reuso de checkpoints.
- **Estado**: Proyecto en estado de experimentación/educacional. Contiene modelos entrenados (`*.h5`) y múltiples checkpoints; no está empaquetado para producción.
- **Autor / Ubicación**: Trabajo local en `d:\\david\\learning_platzi\\machine_learning\\redes_neuronales_tensorflow`.

## Estructura principal (resumen)

- Archivos raíz notables: `best_model.h5`, `my_model.h5`, `main_project.ipynb`, `multiples_datasets_keras.ipynb`, `cargar_multiples_datasets.ipynb`.
- Notebooks principales:
  - `main_project.ipynb` — flujo principal (preprocesamiento → entrenamiento → evaluación → guardado).
  - `multiples_datasets_keras.ipynb` — cómo combinar y usar múltiples datasets en Keras.
  - `cargar_multiples_datasets.ipynb` — utilidades para cargar datos desde `databasesLoadData/`.
- Carpetas de modelos / checkpoints:
  - `model_checpoints/`, `model_checpoints_complete/`, `model_complete/`, `model_manul/` — checkpoints y modelos completos.
  - `models/platzi-tunner/` — resultados de Keras Tuner (trials, `build_config.json`, y `checkpoint.weights.h5`).
- Datasets y recursos:
  - `sign-language-img/Train/` y `sign-language-img/Test/` — imágenes organizadas por etiqueta (A..Y).
  - `databasesLoadData/` — incluye `sign_mnist_base64/`, `sign_mnist_json/`, `sign_mnist_test/`, `sign_mnist_train/`.
  - `bad_images/` — imágenes marcadas como problemáticas que conviene revisar/limpiar.

## Requisitos recomendados

- Python 3.8+ (ajusta según la versión de TensorFlow que prefieras).
- Paquetes sugeridos:
  - `tensorflow` (o `tensorflow-gpu` si tienes GPU y drivers instalados)
  - `numpy`, `pandas`, `matplotlib`, `scikit-learn`
  - `opencv-python` (si utilizas OpenCV para procesar imágenes)
  - `jupyter` o `jupyterlab`
  - `keras-tuner` (opcional, para explorar `models/platzi-tunner`)

Instalación rápida (PowerShell)

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install --upgrade pip
pip install tensorflow numpy pandas matplotlib scikit-learn opencv-python jupyter keras-tuner
```

Notas:
- Para soporte GPU sigue la guía oficial de TensorFlow para tu versión de CUDA/cuDNN.
- Si quieres reproducir exactamente un entorno, puedo generar un `requirements.txt` con versiones específicas.

## Uso básico / Ejecutar notebooks

- Activar entorno e iniciar Jupyter:

```powershell
.\.venv\Scripts\Activate.ps1
jupyter notebook
```

- Abre `main_project.ipynb` para seguir el flujo principal del proyecto.

## Ejemplo rápido: cargar un modelo y hacer inferencia

```python
from tensorflow.keras.models import load_model
import numpy as np

# Cargar modelo
model = load_model('best_model.h5')

# Ejemplo: preprocesar una imagen (placeholder)
# img = ... # cargar y preprocesar a la forma esperada por el modelo
# pred = model.predict(np.expand_dims(img, axis=0))
```

## Cómo reproducir entrenamiento

1. Preparar datos: asegurarte que `sign-language-img/Train` y `.../Test` estén organizados por carpetas por clase.
2. Abrir `main_project.ipynb` o convertir secciones a `train.py` para ejecución por script.
3. Usar checkpoints en `model_checpoints/` para retomar entrenamientos si es necesario.

Ejemplo de carga de dataset desde carpetas con TF:

```python
import tensorflow as tf
train_ds = tf.keras.utils.image_dataset_from_directory(
    'sign-language-img/Train',
    image_size=(64,64),
    batch_size=32,
    label_mode='categorical'
)
```
