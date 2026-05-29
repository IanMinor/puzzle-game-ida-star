# N-Puzzle Solver with IDA*

Este proyecto implementa un solucionador para el problema **N-Puzzle** utilizando el algoritmo **IDA\*** (*Iterative Deepening A\**), una técnica de búsqueda heurística que combina la eficiencia en memoria de la búsqueda en profundidad con el uso de heurísticas para encontrar soluciones óptimas.

El sistema permite generar tableros resolubles de distintos tamaños, desde **3x3 hasta 8x8**, y evalúa el desempeño del algoritmo bajo diferentes niveles de dificultad. Para guiar la búsqueda se utiliza principalmente la **distancia Manhattan**, una heurística común en problemas de rompecabezas deslizantes.

## Objetivo del proyecto

El objetivo principal de este proyecto fue implementar y analizar un algoritmo de búsqueda informada aplicado a un problema clásico de inteligencia artificial. Además de resolver instancias del N-Puzzle, el proyecto incluye un proceso de benchmarking para medir el comportamiento del algoritmo en términos de:

- Tasa de solución.
- Tiempo promedio de ejecución.
- Dificultad del tablero.
- Tamaño del tablero.
- Número de experimentos realizados.

## Características principales

- Implementación del algoritmo **IDA\*** desde cero en Python.
- Generación de tableros resolubles mediante movimientos aleatorios desde el estado objetivo.
- Uso de heurística de **distancia Manhattan** para estimar el costo restante hasta la solución.
- Evaluación experimental en tableros de **3x3 a 8x8**.
- Pruebas con distintos niveles de dificultad: `easy`, `medium` y `hard`.
- Benchmarking con múltiples ejecuciones por configuración.
- Visualización de resultados mediante gráficas de tiempo promedio y tasa de solución.

## Tecnologías utilizadas

- Python
- Matplotlib
- Algoritmos de búsqueda heurística
- Análisis experimental de rendimiento

## Resultados

Se realizaron experimentos sobre diferentes tamaños de tablero y niveles de dificultad. En los escenarios `easy` y `medium`, el algoritmo logró resolver el 100% de los casos evaluados. En escenarios `hard`, el desempeño dependió del tamaño y complejidad del tablero, manteniendo tiempos promedio razonables dentro del límite de ejecución definido.

Estos resultados permiten observar cómo el crecimiento del espacio de búsqueda afecta el rendimiento del algoritmo y cómo una heurística adecuada puede mejorar significativamente la eficiencia de la búsqueda.

## Aprendizajes

Este proyecto me permitió reforzar conceptos importantes de inteligencia artificial y desarrollo de software, incluyendo:

- Búsqueda informada.
- Diseño de heurísticas.
- Optimización de algoritmos.
- Análisis de complejidad práctica.
- Generación de pruebas experimentales.
- Visualización e interpretación de resultados.
