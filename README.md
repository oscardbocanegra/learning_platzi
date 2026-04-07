# 🧠 Ruta de Estudio — Platzi

Repositorio de aprendizaje personal basado en el currículo de Platzi.  
Foco principal en **Inteligencia Artificial, Machine Learning y Data Science**, con base sólida en backend y lenguajes de programación.

---

## 🗺️ Estructura

```
learning_platzi/
│
├── 01_languages/          # Fundamentos de lenguajes de programación
├── 02_backend/            # Desarrollo backend y frameworks web
├── 03_data_science/       # Ciencia de datos, estadística y matemáticas
├── 04_machine_learning/   # Machine Learning, Deep Learning, NLP y MLOps
└── 05_best_practices/     # Ingeniería de software: testing, SOLID, algoritmos
```

---

## 🤖 04 — Machine Learning & IA _(foco principal)_

> El núcleo de la ruta. Desde fundamentos matemáticos hasta modelos en producción.

### Fundamentos
| Curso | Contenido |
|-------|-----------|
| `fundamentos/fundamentos_ml` | Introducción a ML, tipos de aprendizaje, flujo de trabajo |
| `fundamentos/principios_ml` | Principios y pensamiento en ML |
| `fundamentos/regresion_lineal` | Regresión lineal desde cero |
| `fundamentos/algebra_lineal_vectores` | Vectores, funciones lineales, proyecciones |

### Scikit-learn
| Curso | Contenido |
|-------|-----------|
| `sklearn/ml_sklearn` | ML con scikit-learn: clasificación, regresión, clustering |
| `sklearn/regresion_lineal_sklearn` | Regresión lineal con scikit-learn |
| `sklearn/regresion_lineal_sklearn2` | Regresión lineal avanzada |
| `sklearn/regresion_logistica` | Regresión logística |
| `sklearn/arbol_decision` | Árboles de decisión, datasets: Titanic, Pima, Car Evaluation |
| `sklearn/clustering` | K-Means y clustering |
| `sklearn/algebra_lineal_ml` | Álgebra lineal aplicada con scikit-learn |

### Deep Learning
| Curso | Contenido |
|-------|-----------|
| `deep_learning/redes_neuronales` | Fundamentos de redes neuronales |
| `deep_learning/redes_neuronales_tensorflow` | Implementación con TensorFlow/Keras |

### NLP
| Curso | Contenido |
|-------|-----------|
| `nlp/procesamiento_lenguaje_natural` | Fundamentos de NLP |
| `nlp/algoritmos_clasificacion_texto` | Clasificación de texto con ML |

### MLOps
| Curso | Contenido |
|-------|-----------|
| `mlops/mlops` | Ciclo de vida de modelos, despliegue y monitoreo |

---

## 📊 03 — Data Science

> Base matemática y herramientas para análisis de datos.

### Matemáticas para DS/ML
| Curso | Contenido |
|-------|-----------|
| `estadistica/estadistica_descriptiva_ds` | Medidas de tendencia central, dispersión |
| `estadistica/estadistica_descriptiva_py` | Estadística descriptiva con Python |
| `estadistica/estadistica_inferencial` | Pruebas de hipótesis, intervalos de confianza |
| `estadistica/estadistica_computacional` | Simulaciones y estadística computacional |
| `algebra_lineal/algebra_lineal_ml_ds` | Transformaciones lineales, SVD, PCA |
| `algebra_lineal/algebra_lineal_py` | Álgebra lineal con NumPy |
| `calculo_diferencial` | Derivadas, funciones de activación |

### Herramientas y Datos
| Curso | Contenido |
|-------|-----------|
| `python_ciencia_datos` | NumPy, Pandas, Matplotlib |
| `visualizacion/visualizacion_datos` | Pyplot y Seaborn |
| `transformacion_datos_pandas_numpy` | Transformación y limpieza de datos |
| `analisis_exploratorio_datos` | EDA: análisis exploratorio de datos |
| `manejo_datos_faltantes` | Técnicas para datos faltantes, librería EDA propia |
| `datos_faltantes_imputacion` | Imputación de datos |
| `bases_datos/sql_basico` | SQL desde cero |
| `bases_datos/sql_datascience` | SQL aplicado a ciencia de datos |
| `bases_datos/postgresql_datascience` | PostgreSQL para DS |
| `herramientas_ia` | Herramientas modernas de IA |
| `entorno_trabajo_config` | Configuración con cookiecutter para proyectos DS |

---

## ⚙️ 02 — Backend

> APIs, frameworks web y automatización. Complementa la ruta de IA para deploys y servicios.

### FastAPI _(recomendado para ML APIs)_
| Proyecto | Contenido |
|----------|-----------|
| `fastapi/curso_fastapi` | FastAPI con JWT, SQLite, arquitectura por capas |
| `fastapi/fastapi_avanzado` | Middlewares, routers, schemas, servicios |
| `fastapi/intro_twitter_api` | API estilo Twitter con FastAPI |
| `fastapi/proyecto_fastapi` | Proyecto integrador con tests |

### Django & Flask
| Proyecto | Contenido |
|----------|-----------|
| `django/intro_django` | Primer contacto con Django, app de encuestas |
| `django/primer_proyecto` | Proyecto Django con modelos, vistas, templates |
| `django/django_rest` | Django REST Framework: doctors/patients API |
| `flask/curso_flask` | Aplicación web con Flask y templates |

### Otros
| Proyecto | Contenido |
|----------|-----------|
| `crud_python` | CRUD con Python y CSV (`platzi-ventas`) |
| `selenium` | Automatización web con Selenium |
| `nodejs` | Introducción a Node.js |

---

## 💻 01 — Lenguajes

> Bases sólidas en Python, Java y JavaScript.

### Python
| Curso | Contenido |
|-------|-----------|
| `python/curso_python` | POO, decoradores, concurrencia, manejo de archivos |
| `python/comprehension_funciones_errores` | List comprehensions, lambdas, manejo de errores |
| `python/comprension_manejo_errores` | Diccionarios, funciones avanzadas |
| `python/estructuras_datos` | Stacks, queues, listas enlazadas |
| `python/entornos_virtuales` | Gestión de entornos virtuales y dependencias |

### Java
| Curso | Contenido |
|-------|-----------|
| `java/introduccion_java` | Tipos de datos, estructuras de control, listas enlazadas, `MyMedicalAppointments` |
| `java/java_se` | Java SE: interfaces, herencia, colecciones |
| `java/functional_programming` | Programación funcional, árboles binarios |

### JavaScript
| Curso | Contenido |
|-------|-----------|
| `javascript/fundamentos` | Fundamentos JS, arrow functions |
| `javascript/ecmascript` | ES6+: destructuring, módulos, async/await |

---

## 🛠️ 05 — Buenas Prácticas

> Ingeniería de software aplicada — hace mejor todo lo anterior.

| Curso | Contenido |
|-------|-----------|
| `testing/testing_python` | Pytest, mocks, coverage (`htmlcov`), bank account, API client |
| `testing/testing_java` | Testing en Java con JUnit |
| `solid/principios_solid_python` | Los 5 principios SOLID en Python |
| `complejidad_algoritmica` | Big O, análisis de algoritmos, graficado de complejidad |

---

## 🧭 Cómo navegar este repositorio

```
¿Querés entrenar un modelo?     → 04_machine_learning/
¿Necesitás analizar datos?      → 03_data_science/
¿Construís una API para tu ML?  → 02_backend/fastapi/
¿Reforzás Python o Java?        → 01_languages/
¿Mejorás la calidad del código? → 05_best_practices/
```

---

## 🏗️ Stack cubierto

| Área | Tecnologías |
|------|-------------|
| **ML / IA** | Scikit-learn, TensorFlow, Keras, NumPy |
| **Data** | Pandas, Matplotlib, Seaborn, SQL, PostgreSQL |
| **Backend** | FastAPI, Django, Django REST, Flask |
| **Lenguajes** | Python, Java, JavaScript (ES6+) |
| **Prácticas** | Pytest, JUnit, SOLID, Big O |
