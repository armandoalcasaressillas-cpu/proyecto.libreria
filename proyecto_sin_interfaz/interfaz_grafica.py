"""
Sistema de Gestión de Bibliotecas (SGB) - Interfaz Gráfica
Interfaz gráfica desarrollada con Tkinter que implementa todas las funcionalidades del sistema.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from typing import List
import os

from funciones_libros.gestor_libros import GestorLibros
from funciones_prestamo.gestor_prestamos import GestorPrestamos
from funciones_prestamo.funciones_usuario.gestor_usuario import GestorUsuario
from problemas_resueltos.estanteria import Estanteria
from recursion.funciones_recursivas import FuncionesRecursivas
from algoritmos_ordenamiento.ordenamiento import Ordenamiento
from funciones_libros.libro import Libro

class InterfazGestionBibliotecas:
    """
    Clase principal que gestiona la interfaz gráfica del sistema.
    """
    
    def __init__(self, root):
        """
        Inicializa la interfaz gráfica.
        
        Args:
            root: Ventana principal de Tkinter
        """
        self.root = root
        self.root.title("Sistema de Gestión de Bibliotecas (SGB)")
        self.root.geometry("1200x700")
        self.root.configure(bg='#f0f0f0')
        
        # Inicializar componentes del sistema
        self.gestor_libros = GestorLibros()
        self.gestor_prestamos = GestorPrestamos(self.gestor_libros)
        self.gestor_usuario = GestorUsuario()
        self.estanteria = Estanteria()
        self.recursion = FuncionesRecursivas()
        self.ordenamiento = Ordenamiento()
        
        # Crear interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea todos los componentes de la interfaz gráfica."""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
        # Panel izquierdo - Menú
        menu_frame = ttk.LabelFrame(main_frame, text="Menú Principal", padding="10")
        menu_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        
        # Botones del menú
        ttk.Button(menu_frame, text="1. Gestión de Libros", 
                  command=self.mostrar_gestion_libros, width=25).pack(pady=5, fill=tk.X)
        ttk.Button(menu_frame, text="2. Gestión de Préstamos", 
                  command=self.mostrar_gestion_prestamos, width=25).pack(pady=5, fill=tk.X)
        ttk.Button(menu_frame, text="3. Búsqueda de Libros", 
                  command=self.mostrar_busqueda, width=25).pack(pady=5, fill=tk.X)
        ttk.Button(menu_frame, text="4. Reportes", 
                  command=self.mostrar_reportes, width=25).pack(pady=5, fill=tk.X)
        ttk.Button(menu_frame, text="5. Módulo de Estantería", 
                  command=self.mostrar_estanteria, width=25).pack(pady=5, fill=tk.X)
        ttk.Button(menu_frame, text="6. Funciones Recursivas", 
                  command=self.mostrar_recursion, width=25).pack(pady=5, fill=tk.X)
        ttk.Button(menu_frame, text="7. Ver Inventario", 
                  command=self.mostrar_inventario, width=25).pack(pady=5, fill=tk.X)
        
        # Panel derecho - Área de contenido
        self.content_frame = ttk.Frame(main_frame)
        self.content_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.content_frame.columnconfigure(0, weight=1)
        self.content_frame.rowconfigure(0, weight=1)
        
        # Mostrar pantalla de bienvenida
        self.mostrar_bienvenida()
    
    def limpiar_contenido(self):
        """Limpia el área de contenido."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def mostrar_bienvenida(self):
        """Muestra la pantalla de bienvenida."""
        self.limpiar_contenido()
        
        welcome_frame = ttk.Frame(self.content_frame, padding="20")
        welcome_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(welcome_frame, text="Sistema de Gestión de Bibliotecas (SGB)", 
                 font=("Arial", 20, "bold")).pack(pady=20)
        ttk.Label(welcome_frame, text="Bienvenido al sistema", 
                 font=("Arial", 12)).pack(pady=10)
        ttk.Label(welcome_frame, 
                 text="Seleccione una opción del menú para comenzar", 
                 font=("Arial", 10)).pack(pady=10)
    
    def mostrar_gestion_libros(self):
        """Muestra la interfaz de gestión de libros."""
        self.limpiar_contenido()
        
        frame = ttk.LabelFrame(self.content_frame, text="Gestión de Libros", padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
        frame.columnconfigure(0, weight=1)
        
        # Formulario para agregar libro
        form_frame = ttk.LabelFrame(frame, text="Agregar Nuevo Libro", padding="10")
        form_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        form_frame.columnconfigure(1, weight=1)
        
        ttk.Label(form_frame, text="ISBN:").grid(row=0, column=0, sticky=tk.W, pady=5)
        entry_isbn = ttk.Entry(form_frame, width=30)
        entry_isbn.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        ttk.Label(form_frame, text="Título:").grid(row=1, column=0, sticky=tk.W, pady=5)
        entry_titulo = ttk.Entry(form_frame, width=30)
        entry_titulo.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        ttk.Label(form_frame, text="Autor:").grid(row=2, column=0, sticky=tk.W, pady=5)
        entry_autor = ttk.Entry(form_frame, width=30)
        entry_autor.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        ttk.Label(form_frame, text="Peso (Kg):").grid(row=3, column=0, sticky=tk.W, pady=5)
        entry_peso = ttk.Entry(form_frame, width=30)
        entry_peso.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        ttk.Label(form_frame, text="Valor ($ COP):").grid(row=4, column=0, sticky=tk.W, pady=5)
        entry_valor = ttk.Entry(form_frame, width=30)
        entry_valor.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        ttk.Label(form_frame, text="Cantidad:").grid(row=5, column=0, sticky=tk.W, pady=5)
        entry_cantidad = ttk.Entry(form_frame, width=30)
        entry_cantidad.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        def agregar_libro():
            try:
                isbn = entry_isbn.get().strip()
                titulo = entry_titulo.get().strip()
                autor = entry_autor.get().strip()
                peso = float(entry_peso.get())
                valor = int(entry_valor.get())
                cantidad = int(entry_cantidad.get())
                
                if not all([isbn, titulo, autor]):
                    messagebox.showerror("Error", "Todos los campos son obligatorios")
                    return
                
                libro = self.gestor_libros.cargar_libro_manual(isbn, titulo, autor, peso, valor, cantidad)
                
                if self.gestor_libros.agregar_libro(libro):
                    messagebox.showinfo("Éxito", "Libro agregado exitosamente")
                    # Limpiar campos
                    entry_isbn.delete(0, tk.END)
                    entry_titulo.delete(0, tk.END)
                    entry_autor.delete(0, tk.END)
                    entry_peso.delete(0, tk.END)
                    entry_valor.delete(0, tk.END)
                    entry_cantidad.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "El ISBN ya existe en el inventario")
            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")
            except Exception as e:
                messagebox.showerror("Error", f"Error al agregar libro: {str(e)}")
        
        ttk.Button(form_frame, text="Agregar Libro", command=agregar_libro).grid(
            row=6, column=0, columnspan=2, pady=10)
        
        # Lista de libros
        list_frame = ttk.LabelFrame(frame, text="Inventario", padding="10")
        list_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        
        # Treeview para mostrar libros
        columns = ("ISBN", "Título", "Autor", "Peso", "Valor", "Disponibles", "Total")
        tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=15)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120)
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        def actualizar_lista():
            for item in tree.get_children():
                tree.delete(item)
            inventario = self.gestor_libros.obtener_inventario_general()
            for libro in inventario:
                tree.insert("", tk.END, values=(
                    libro.isbn, libro.titulo, libro.autor, 
                    f"{libro.peso} Kg", f"${libro.valor:,}", 
                    libro.cantidad_presente, libro.cantidad
                ))
        
        actualizar_lista()
        ttk.Button(list_frame, text="Actualizar Lista", command=actualizar_lista).grid(
            row=1, column=0, pady=5)
    
    def mostrar_gestion_prestamos(self):
        """Muestra la interfaz de gestión de préstamos."""
        self.limpiar_contenido()
        
        notebook = ttk.Notebook(self.content_frame)
        notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
        self.content_frame.columnconfigure(0, weight=1)
        self.content_frame.rowconfigure(0, weight=1)
        
        # Pestaña de préstamos
        prestamo_frame = ttk.Frame(notebook, padding="10")
        notebook.add(prestamo_frame, text="Prestar/Devolver")
        
        # Prestar
        prestar_frame = ttk.LabelFrame(prestamo_frame, text="Prestar Libro", padding="10")
        prestar_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        prestar_frame.columnconfigure(1, weight=1)
        
        ttk.Label(prestar_frame, text="ISBN:").grid(row=0, column=0, sticky=tk.W, pady=5)
        entry_isbn_prestar = ttk.Entry(prestar_frame, width=30)
        entry_isbn_prestar.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        ttk.Label(prestar_frame, text="Usuario:").grid(row=1, column=0, sticky=tk.W, pady=5)
        entry_usuario_prestar = ttk.Entry(prestar_frame, width=30)
        entry_usuario_prestar.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        def prestar():
            isbn = entry_isbn_prestar.get().strip()
            usuario = entry_usuario_prestar.get().strip()
            if not isbn or not usuario:
                messagebox.showerror("Error", "Por favor complete todos los campos")
                return
            exito, mensaje = self.gestor_prestamos.prestar_libro(isbn, usuario)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
            else:
                messagebox.showwarning("Advertencia", mensaje)
            entry_isbn_prestar.delete(0, tk.END)
            entry_usuario_prestar.delete(0, tk.END)
        
        ttk.Button(prestar_frame, text="Prestar", command=prestar).grid(
            row=2, column=0, columnspan=2, pady=10)
        
        # Devolver
        devolver_frame = ttk.LabelFrame(prestamo_frame, text="Devolver Libro", padding="10")
        devolver_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        devolver_frame.columnconfigure(1, weight=1)
        
        ttk.Label(devolver_frame, text="ISBN:").grid(row=0, column=0, sticky=tk.W, pady=5)
        entry_isbn_devolver = ttk.Entry(devolver_frame, width=30)
        entry_isbn_devolver.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        ttk.Label(devolver_frame, text="Usuario:").grid(row=1, column=0, sticky=tk.W, pady=5)
        entry_usuario_devolver = ttk.Entry(devolver_frame, width=30)
        entry_usuario_devolver.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        def devolver():
            isbn = entry_isbn_devolver.get().strip()
            usuario = entry_usuario_devolver.get().strip()
            if not isbn or not usuario:
                messagebox.showerror("Error", "Por favor complete todos los campos")
                return
            exito, mensaje = self.gestor_prestamos.devolver_libro(isbn, usuario)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
            else:
                messagebox.showerror("Error", mensaje)
            entry_isbn_devolver.delete(0, tk.END)
            entry_usuario_devolver.delete(0, tk.END)
        
        ttk.Button(devolver_frame, text="Devolver", command=devolver).grid(
            row=2, column=0, columnspan=2, pady=10)
        
        # Pestaña de historial
        historial_frame = ttk.Frame(notebook, padding="10")
        notebook.add(historial_frame, text="Historial")
        
        ttk.Label(historial_frame, text="Usuario:").grid(row=0, column=0, sticky=tk.W, pady=5)
        entry_usuario_hist = ttk.Entry(historial_frame, width=30)
        entry_usuario_hist.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        historial_frame.columnconfigure(1, weight=1)
        
        text_historial = scrolledtext.ScrolledText(historial_frame, height=20, width=60)
        text_historial.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        historial_frame.rowconfigure(1, weight=1)
        
        def mostrar_historial():
            usuario = entry_usuario_hist.get().strip()
            if not usuario:
                messagebox.showerror("Error", "Por favor ingrese un usuario")
                return
            historial = self.gestor_prestamos.obtener_historial_usuario(usuario)
            text_historial.delete(1.0, tk.END)
            if historial:
                text_historial.insert(tk.END, f"Historial de préstamos de {usuario}:\n\n")
                for i, prestamo in enumerate(reversed(historial), 1):
                    text_historial.insert(tk.END, 
                        f"{i}. ISBN: {prestamo['ISBN']}\n   Fecha: {prestamo['Fecha']}\n\n")
            else:
                text_historial.insert(tk.END, f"No hay historial de préstamos para {usuario}")
        
        ttk.Button(historial_frame, text="Buscar Historial", command=mostrar_historial).grid(
            row=0, column=2, padx=5)
        
        # Pestaña de reservas
        reservas_frame = ttk.Frame(notebook, padding="10")
        notebook.add(reservas_frame, text="Reservas")
        
        text_reservas = scrolledtext.ScrolledText(reservas_frame, height=20, width=60)
        text_reservas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        reservas_frame.columnconfigure(0, weight=1)
        reservas_frame.rowconfigure(0, weight=1)
        
        def actualizar_reservas():
            reservas = self.gestor_prestamos.obtener_reservas_pendientes()
            text_reservas.delete(1.0, tk.END)
            if reservas:
                text_reservas.insert(tk.END, "Reservas pendientes:\n\n")
                for i, reserva in enumerate(reservas, 1):
                    text_reservas.insert(tk.END, 
                        f"{i}. ISBN: {reserva['ISBN']} - Usuario: {reserva['Usuario']}\n")
            else:
                text_reservas.insert(tk.END, "No hay reservas pendientes")
        
        ttk.Button(reservas_frame, text="Actualizar Reservas", command=actualizar_reservas).grid(
            row=1, column=0, pady=5)
        actualizar_reservas()
    
    def mostrar_busqueda(self):
        """Muestra la interfaz de búsqueda."""
        self.limpiar_contenido()
        
        frame = ttk.LabelFrame(self.content_frame, text="Búsqueda de Libros", padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(2, weight=1)
        
        # Búsqueda por ISBN
        isbn_frame = ttk.LabelFrame(frame, text="Búsqueda Binaria por ISBN", padding="10")
        isbn_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        isbn_frame.columnconfigure(1, weight=1)
        
        ttk.Label(isbn_frame, text="ISBN:").grid(row=0, column=0, sticky=tk.W, pady=5)
        entry_isbn = ttk.Entry(isbn_frame, width=30)
        entry_isbn.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        def buscar_isbn():
            isbn = entry_isbn.get().strip()
            if not isbn:
                messagebox.showerror("Error", "Por favor ingrese un ISBN")
                return
            libro = self.gestor_libros.buscar_por_isbn_binaria(isbn)
            if libro:
                resultado_text.delete(1.0, tk.END)
                resultado_text.insert(tk.END, f"Libro encontrado:\n\n")
                resultado_text.insert(tk.END, f"ISBN: {libro.isbn}\n")
                resultado_text.insert(tk.END, f"Título: {libro.titulo}\n")
                resultado_text.insert(tk.END, f"Autor: {libro.autor}\n")
                resultado_text.insert(tk.END, f"Peso: {libro.peso} Kg\n")
                resultado_text.insert(tk.END, f"Valor: ${libro.valor:,} COP\n")
                resultado_text.insert(tk.END, f"Disponibles: {libro.cantidad_presente}/{libro.cantidad}\n")
            else:
                messagebox.showinfo("No encontrado", f"Libro con ISBN {isbn} no encontrado")
        
        ttk.Button(isbn_frame, text="Buscar", command=buscar_isbn).grid(
            row=0, column=2, padx=5)
        
        # Búsqueda por título/autor
        lineal_frame = ttk.LabelFrame(frame, text="Búsqueda Lineal por Título/Autor", padding="10")
        lineal_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        lineal_frame.columnconfigure(1, weight=1)
        
        ttk.Label(lineal_frame, text="Término:").grid(row=0, column=0, sticky=tk.W, pady=5)
        entry_termino = ttk.Entry(lineal_frame, width=30)
        entry_termino.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        def buscar_lineal():
            termino = entry_termino.get().strip()
            if not termino:
                messagebox.showerror("Error", "Por favor ingrese un término de búsqueda")
                return
            resultados = self.gestor_libros.buscar_por_titulo_autor(termino)
            resultado_text.delete(1.0, tk.END)
            if resultados:
                resultado_text.insert(tk.END, f"Se encontraron {len(resultados)} resultado(s):\n\n")
                for i, libro in enumerate(resultados, 1):
                    resultado_text.insert(tk.END, f"{i}. {libro.titulo}\n")
                    resultado_text.insert(tk.END, f"   ISBN: {libro.isbn} | Autor: {libro.autor}\n")
                    resultado_text.insert(tk.END, f"   Peso: {libro.peso} Kg | Valor: ${libro.valor:,} COP\n")
                    resultado_text.insert(tk.END, f"   Disponibles: {libro.cantidad_presente}/{libro.cantidad}\n\n")
            else:
                resultado_text.insert(tk.END, f"No se encontraron libros con el término '{termino}'")
        
        ttk.Button(lineal_frame, text="Buscar", command=buscar_lineal).grid(
            row=0, column=2, padx=5)
        
        # Área de resultados
        resultado_frame = ttk.LabelFrame(frame, text="Resultados", padding="10")
        resultado_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        resultado_frame.columnconfigure(0, weight=1)
        resultado_frame.rowconfigure(0, weight=1)
        
        resultado_text = scrolledtext.ScrolledText(resultado_frame, height=15, width=60)
        resultado_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    def mostrar_reportes(self):
        """Muestra la interfaz de reportes."""
        self.limpiar_contenido()
        
        frame = ttk.LabelFrame(self.content_frame, text="Reportes", padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        
        def generar_reporte():
            inventario = self.gestor_libros.obtener_inventario_general()
            if not inventario:
                messagebox.showwarning("Advertencia", "No hay libros en el inventario")
                return
            
            self.ordenamiento.generar_reporte_por_valor(inventario)
            messagebox.showinfo("Éxito", "Reporte generado exitosamente en 'reporte_por_valor.json'")
            
            # Mostrar el reporte
            inventario_ordenado = self.ordenamiento.merge_sort_por_valor(inventario)
            texto_reporte.delete(1.0, tk.END)
            texto_reporte.insert(tk.END, "Reporte de Inventario Ordenado por Valor (Merge Sort):\n\n")
            for i, libro in enumerate(inventario_ordenado, 1):
                texto_reporte.insert(tk.END, f"{i}. {libro.titulo}\n")
                texto_reporte.insert(tk.END, f"   Valor: ${libro.valor:,} COP | Peso: {libro.peso} Kg\n")
                texto_reporte.insert(tk.END, f"   ISBN: {libro.isbn} | Autor: {libro.autor}\n\n")
        
        ttk.Button(frame, text="Generar Reporte por Valor (Merge Sort)", 
                  command=generar_reporte).grid(row=0, column=0, pady=10)
        
        texto_reporte = scrolledtext.ScrolledText(frame, height=20, width=60)
        texto_reporte.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    def mostrar_estanteria(self):
        """Muestra la interfaz del módulo de estantería."""
        self.limpiar_contenido()
        
        notebook = ttk.Notebook(self.content_frame)
        notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
        self.content_frame.columnconfigure(0, weight=1)
        self.content_frame.rowconfigure(0, weight=1)
        
        # Fuerza Bruta
        fuerza_frame = ttk.Frame(notebook, padding="10")
        notebook.add(fuerza_frame, text="Fuerza Bruta - Combinaciones de Riesgo")
        fuerza_frame.columnconfigure(0, weight=1)
        fuerza_frame.rowconfigure(1, weight=1)
        
        def mostrar_fuerza_bruta():
            inventario = self.gestor_libros.obtener_inventario_general()
            if len(inventario) < 4:
                messagebox.showwarning("Advertencia", "Se necesitan al menos 4 libros")
                return
            
            combinaciones = self.estanteria.fuerza_bruta_estanteria_deficiente(inventario)
            texto_fuerza.delete(1.0, tk.END)
            
            if combinaciones:
                texto_fuerza.insert(tk.END, 
                    f"Combinaciones de riesgo (peso > {self.estanteria.capacidad_maxima} Kg):\n\n")
                for i, combinacion in enumerate(combinaciones, 1):
                    peso_total = sum(libro.peso for libro in combinacion)
                    texto_fuerza.insert(tk.END, f"Combinación {i} (Peso total: {peso_total:.2f} Kg):\n")
                    for libro in combinacion:
                        texto_fuerza.insert(tk.END, 
                            f"  - {libro.titulo}: {libro.peso} Kg\n")
                    texto_fuerza.insert(tk.END, "\n")
            else:
                texto_fuerza.insert(tk.END, 
                    f"No se encontraron combinaciones de 4 libros que superen {self.estanteria.capacidad_maxima} Kg")
        
        ttk.Button(fuerza_frame, text="Calcular Combinaciones de Riesgo", 
                  command=mostrar_fuerza_bruta).grid(row=0, column=0, pady=10)
        
        texto_fuerza = scrolledtext.ScrolledText(fuerza_frame, height=20, width=60)
        texto_fuerza.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Backtracking
        backtrack_frame = ttk.Frame(notebook, padding="10")
        notebook.add(backtrack_frame, text="Backtracking - Estantería Óptima")
        backtrack_frame.columnconfigure(0, weight=1)
        backtrack_frame.rowconfigure(1, weight=1)
        
        def mostrar_backtracking():
            inventario = self.gestor_libros.obtener_inventario_general()
            if not inventario:
                messagebox.showwarning("Advertencia", "No hay libros en el inventario")
                return
            
            mejor_combinacion, mejor_valor, mejor_peso = self.estanteria.backtracking_estanteria_optima(inventario)
            texto_backtrack.delete(1.0, tk.END)
            
            if mejor_combinacion:
                texto_backtrack.insert(tk.END, "Estantería Óptima:\n\n")
                texto_backtrack.insert(tk.END, f"Valor total: ${mejor_valor:,} COP\n")
                texto_backtrack.insert(tk.END, f"Peso total: {mejor_peso:.2f} Kg\n")
                texto_backtrack.insert(tk.END, f"Capacidad máxima: {self.estanteria.capacidad_maxima} Kg\n\n")
                texto_backtrack.insert(tk.END, f"Libros seleccionados ({len(mejor_combinacion)}):\n\n")
                for libro in mejor_combinacion:
                    texto_backtrack.insert(tk.END, 
                        f"- {libro.titulo}\n")
                    texto_backtrack.insert(tk.END, 
                        f"  Peso: {libro.peso} Kg | Valor: ${libro.valor:,} COP\n\n")
            else:
                texto_backtrack.insert(tk.END, "No se encontró una combinación válida")
        
        ttk.Button(backtrack_frame, text="Calcular Estantería Óptima", 
                  command=mostrar_backtracking).grid(row=0, column=0, pady=10)
        
        texto_backtrack = scrolledtext.ScrolledText(backtrack_frame, height=20, width=60)
        texto_backtrack.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    def mostrar_recursion(self):
        """Muestra la interfaz de funciones recursivas."""
        self.limpiar_contenido()
        
        notebook = ttk.Notebook(self.content_frame)
        notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
        self.content_frame.columnconfigure(0, weight=1)
        self.content_frame.rowconfigure(0, weight=1)
        
        # Recursión de Pila
        pila_frame = ttk.Frame(notebook, padding="10")
        notebook.add(pila_frame, text="Recursión de Pila - Valor Total")
        pila_frame.columnconfigure(0, weight=1)
        pila_frame.rowconfigure(2, weight=1)
        
        ttk.Label(pila_frame, text="Autor:").grid(row=0, column=0, sticky=tk.W, pady=5)
        entry_autor_pila = ttk.Entry(pila_frame, width=30)
        entry_autor_pila.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        pila_frame.columnconfigure(1, weight=1)
        
        def calcular_valor_pila():
            autor = entry_autor_pila.get().strip()
            if not autor:
                messagebox.showerror("Error", "Por favor ingrese un autor")
                return
            inventario = self.gestor_libros.obtener_inventario_general()
            valor_total = self.recursion.valor_total_autor_recursivo_pila(inventario, autor)
            texto_pila.delete(1.0, tk.END)
            texto_pila.insert(tk.END, f"Valor total de libros del autor '{autor}':\n\n")
            texto_pila.insert(tk.END, f"${valor_total:,} COP\n\n")
            texto_pila.insert(tk.END, "Este resultado se calculó usando recursión de pila,\n")
            texto_pila.insert(tk.END, "donde el resultado se acumula en el retorno de las llamadas recursivas.")
        
        ttk.Button(pila_frame, text="Calcular Valor Total", 
                  command=calcular_valor_pila).grid(row=0, column=2, padx=5)
        
        texto_pila = scrolledtext.ScrolledText(pila_frame, height=15, width=60)
        texto_pila.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Recursión de Cola
        cola_frame = ttk.Frame(notebook, padding="10")
        notebook.add(cola_frame, text="Recursión de Cola - Peso Promedio")
        cola_frame.columnconfigure(0, weight=1)
        cola_frame.rowconfigure(2, weight=1)
        
        ttk.Label(cola_frame, text="Autor:").grid(row=0, column=0, sticky=tk.W, pady=5)
        entry_autor_cola = ttk.Entry(cola_frame, width=30)
        entry_autor_cola.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        cola_frame.columnconfigure(1, weight=1)
        
        def calcular_peso_cola():
            autor = entry_autor_cola.get().strip()
            if not autor:
                messagebox.showerror("Error", "Por favor ingrese un autor")
                return
            inventario = self.gestor_libros.obtener_inventario_general()
            peso_promedio = self.recursion.peso_promedio_autor_recursivo_cola(inventario, autor)
            texto_cola.delete(1.0, tk.END)
            texto_cola.insert(tk.END, f"Peso promedio de libros del autor '{autor}':\n\n")
            texto_cola.insert(tk.END, f"{peso_promedio:.2f} Kg\n\n")
            texto_cola.insert(tk.END, "Este resultado se calculó usando recursión de cola,\n")
            texto_cola.insert(tk.END, "donde los resultados se acumulan como parámetros en cada llamada recursiva.")
        
        ttk.Button(cola_frame, text="Calcular Peso Promedio", 
                  command=calcular_peso_cola).grid(row=0, column=2, padx=5)
        
        texto_cola = scrolledtext.ScrolledText(cola_frame, height=15, width=60)
        texto_cola.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
    
    def mostrar_inventario(self):
        """Muestra el inventario completo."""
        self.limpiar_contenido()
        
        notebook = ttk.Notebook(self.content_frame)
        notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
        self.content_frame.columnconfigure(0, weight=1)
        self.content_frame.rowconfigure(0, weight=1)
        
        # Inventario General
        general_frame = ttk.Frame(notebook, padding="10")
        notebook.add(general_frame, text="Inventario General (Desordenado)")
        general_frame.columnconfigure(0, weight=1)
        general_frame.rowconfigure(0, weight=1)
        
        columns = ("ISBN", "Título", "Autor", "Peso", "Valor", "Disponibles", "Total")
        tree_general = ttk.Treeview(general_frame, columns=columns, show="headings", height=20)
        
        for col in columns:
            tree_general.heading(col, text=col)
            tree_general.column(col, width=120)
        
        scrollbar_general = ttk.Scrollbar(general_frame, orient=tk.VERTICAL, command=tree_general.yview)
        tree_general.configure(yscrollcommand=scrollbar_general.set)
        
        tree_general.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar_general.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        inventario_general = self.gestor_libros.obtener_inventario_general()
        for libro in inventario_general:
            tree_general.insert("", tk.END, values=(
                libro.isbn, libro.titulo, libro.autor, 
                f"{libro.peso} Kg", f"${libro.valor:,}", 
                libro.cantidad_presente, libro.cantidad
            ))
        
        # Inventario Ordenado
        ordenado_frame = ttk.Frame(notebook, padding="10")
        notebook.add(ordenado_frame, text="Inventario Ordenado (Por ISBN)")
        ordenado_frame.columnconfigure(0, weight=1)
        ordenado_frame.rowconfigure(0, weight=1)
        
        tree_ordenado = ttk.Treeview(ordenado_frame, columns=columns, show="headings", height=20)
        
        for col in columns:
            tree_ordenado.heading(col, text=col)
            tree_ordenado.column(col, width=120)
        
        scrollbar_ordenado = ttk.Scrollbar(ordenado_frame, orient=tk.VERTICAL, command=tree_ordenado.yview)
        tree_ordenado.configure(yscrollcommand=scrollbar_ordenado.set)
        
        tree_ordenado.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar_ordenado.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        inventario_ordenado = self.gestor_libros.obtener_inventario_ordenado()
        for libro in inventario_ordenado:
            tree_ordenado.insert("", tk.END, values=(
                libro.isbn, libro.titulo, libro.autor, 
                f"{libro.peso} Kg", f"${libro.valor:,}", 
                libro.cantidad_presente, libro.cantidad
            ))

def main():
    """Función principal que inicia la aplicación."""
    root = tk.Tk()
    app = InterfazGestionBibliotecas(root)
    root.mainloop()

if __name__ == "__main__":
    main()

