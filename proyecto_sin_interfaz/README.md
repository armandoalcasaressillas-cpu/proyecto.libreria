# Sistema de Gestión de Bibliotecas (SGB)

Sistema completo de gestión de bibliotecas desarrollado en Python con interfaz gráfica Tkinter.

## Características Implementadas

### Estructuras de Datos
- **Pila (LIFO)**: Historial de préstamos por usuario con persistencia en JSON
- **Cola (FIFO)**: Lista de espera para reservas de libros agotados con persistencia en JSON
- **Listas**: Inventario General (desordenado) e Inventario Ordenado (por ISBN)

### Algoritmos de Ordenamiento
- **Ordenamiento por Inserción**: Mantiene el inventario ordenado por ISBN cada vez que se agrega un libro
- **Merge Sort**: Genera reportes globales ordenados por valor

### Algoritmos de Búsqueda
- **Búsqueda Lineal**: Búsqueda por título o autor en el inventario general
- **Búsqueda Binaria**: Búsqueda por ISBN en el inventario ordenado (crítica para verificar reservas)

### Módulo de Estantería
- **Fuerza Bruta**: Encuentra todas las combinaciones de 4 libros que superan 8 Kg
- **Backtracking**: Encuentra la combinación óptima que maximiza el valor sin exceder 8 Kg

### Recursión
- **Recursión de Pila**: Calcula el valor total de libros de un autor
- **Recursión de Cola**: Calcula el peso promedio de libros de un autor

### Programación Orientada a Objetos
- Clase `Libro`: Representa un libro con todos sus atributos
- Clase `Usuario`: Representa un usuario del sistema
- Clase `GestorLibros`: Gestiona el inventario de libros
- Clase `GestorPrestamos`: Gestiona préstamos y devoluciones
- Clase `GestorUsuario`: Gestiona usuarios
- Clase `Estanteria`: Gestiona algoritmos de estantería
- Clase `FuncionesRecursivas`: Contiene funciones recursivas
- Clase `Ordenamiento`: Contiene algoritmos de ordenamiento
- Clase `Busqueda`: Contiene algoritmos de búsqueda
- Clase `Pila`: Implementación de estructura de datos Pila
- Clase `Cola`: Implementación de estructura de datos Cola

## Estructura del Proyecto

```
proyecto_sin_interfaz/
├── inicial.py                      # Archivo principal
├── interfaz_grafica.py             # Interfaz gráfica con Tkinter
├── libros.json                     # Archivo de datos de libros
├── historial_prestamos.json        # Historial de préstamos (generado automáticamente)
├── reservas.json                   # Reservas pendientes (generado automáticamente)
├── estructuras_datos/
│   ├── __init__.py
│   ├── pila.py                     # Implementación de Pila
│   └── cola.py                     # Implementación de Cola
├── funciones_libros/
│   ├── __init__.py
│   ├── libro.py                    # Clase Libro
│   └── gestor_libros.py            # Gestor de libros
├── funciones_prestamo/
│   ├── __init__.py
│   ├── gestor_prestamos.py         # Gestor de préstamos
│   └── funciones_usuario/
│       ├── __init__.py
│       └── gestor_usuario.py       # Gestor de usuarios
├── algoritmos_ordenamiento/
│   ├── __init__.py
│   └── ordenamiento.py             # Algoritmos de ordenamiento
├── algoritmos_busqueda/
│   ├── __init__.py
│   └── busqueda.py                 # Algoritmos de búsqueda
├── problemas_resueltos/
│   ├── __init__.py
│   └── estanteria.py               # Algoritmos de estantería
└── recursion/
    ├── __init__.py
    └── funciones_recursivas.py     # Funciones recursivas
```

## Requisitos

- Python 3.6 o superior
- Tkinter (incluido en la mayoría de instalaciones de Python)

## Instalación

1. Asegúrate de tener Python instalado
2. Clona o descarga este proyecto
3. No se requieren dependencias adicionales (Tkinter viene con Python)

## Uso

Para ejecutar el sistema:

```bash
python inicial.py
```

O directamente:

```bash
python interfaz_grafica.py
```

## Funcionalidades de la Interfaz

### 1. Gestión de Libros
- Agregar nuevos libros al inventario
- Ver inventario general y ordenado
- Los libros se ordenan automáticamente por ISBN usando ordenamiento por inserción

### 2. Gestión de Préstamos
- Prestar libros a usuarios
- Devolver libros
- Ver historial de préstamos por usuario (Pila LIFO)
- Ver reservas pendientes (Cola FIFO)
- Asignación automática de reservas cuando se devuelve un libro

### 3. Búsqueda de Libros
- Búsqueda binaria por ISBN (en inventario ordenado)
- Búsqueda lineal por título o autor (en inventario general)

### 4. Reportes
- Generar reporte global ordenado por valor usando Merge Sort
- El reporte se guarda en `reporte_por_valor.json`

### 5. Módulo de Estantería
- **Fuerza Bruta**: Encuentra todas las combinaciones de 4 libros que superan 8 Kg
- **Backtracking**: Encuentra la combinación óptima que maximiza el valor sin exceder 8 Kg

### 6. Funciones Recursivas
- **Recursión de Pila**: Calcula el valor total de libros de un autor
- **Recursión de Cola**: Calcula el peso promedio de libros de un autor

### 7. Ver Inventario
- Visualizar inventario general (desordenado)
- Visualizar inventario ordenado (por ISBN)

## Persistencia de Datos

El sistema guarda automáticamente:
- `libros.json`: Inventario de libros
- `historial_prestamos.json`: Historial de préstamos (Pila)
- `reservas.json`: Reservas pendientes (Cola)
- `reporte_por_valor.json`: Reporte generado por Merge Sort

## Documentación

Todo el código está completamente documentado con docstrings siguiendo estándares de Python. Cada clase, método y algoritmo tiene una explicación clara de su propósito, parámetros y retorno.

## Notas Técnicas

- El sistema mantiene dos listas: Inventario General (desordenado) e Inventario Ordenado (por ISBN)
- El ordenamiento por inserción se ejecuta automáticamente al agregar un libro
- La búsqueda binaria es crítica para verificar reservas pendientes
- Las estructuras de datos (Pila y Cola) se persisten en archivos JSON
- La interfaz gráfica está desarrollada completamente con Tkinter

## Autor

Sistema desarrollado como proyecto académico para demostrar comprensión de:
- Estructuras de datos (Listas, Pilas, Colas)
- Algoritmos de ordenamiento (Inserción, Merge Sort)
- Algoritmos de búsqueda (Lineal, Binaria)
- Algoritmos de resolución de problemas (Fuerza Bruta, Backtracking)
- Recursión (Pila y Cola)
- Programación Orientada a Objetos
- Modularidad y organización de código

