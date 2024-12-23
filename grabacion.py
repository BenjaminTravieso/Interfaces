import customtkinter as ctk

# Configuración de la ventana principal
root = ctk.CTk()
root.title("Audio Scribe")
root.geometry("1000x700")

# Configuración de los grid
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

# Panel de Navegación
nav_frame = ctk.CTkFrame(root, width=200, height=700)
nav_frame.grid(row=0, column=0, rowspan=4, sticky="nsw")

nav_label = ctk.CTkLabel(nav_frame, text="Navegación", font=("Arial", 16, "bold"))
nav_label.pack(pady=10)

# Botones del Panel de Navegación
boton_grabar_formato = ctk.CTkButton(nav_frame, text="Grabar Formato")
boton_grabar_formato.pack(pady=5)

boton_historial_formatos = ctk.CTkButton(nav_frame, text="Historial Formatos")
boton_historial_formatos.pack(pady=5)

boton_cerrar = ctk.CTkButton(nav_frame, text="Cerrar Audio Scribe", fg_color="red")
boton_cerrar.pack(pady=5)

# Sección de Autor
autor_frame = ctk.CTkFrame(root)
autor_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

autor_label = ctk.CTkLabel(autor_frame, text="Autor", font=("Arial", 16, "bold"))
autor_label.grid(row=0, column=0, columnspan=2, pady=10)

nombre_entry = ctk.CTkEntry(autor_frame, width=200, placeholder_text="Nombre")
nombre_entry.grid(row=1, column=0, pady=5, padx=10)

apellido_entry = ctk.CTkEntry(autor_frame, width=200, placeholder_text="Apellido")
apellido_entry.grid(row=1, column=1, pady=5, padx=10)

# Sección de Datos de Archivo
datos_frame = ctk.CTkFrame(root)
datos_frame.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

datos_label = ctk.CTkLabel(datos_frame, text="Datos del archivo", font=("Arial", 16, "bold"))
datos_label.grid(row=0, column=0, columnspan=2, pady=10)

tema_entry = ctk.CTkEntry(datos_frame, width=200, placeholder_text="Tema")
tema_entry.grid(row=1, column=0, pady=5, padx=10)

titulo_entry = ctk.CTkEntry(datos_frame, width=200, placeholder_text="Título")
titulo_entry.grid(row=1, column=1, pady=5, padx=10)

descripcion_entry = ctk.CTkEntry(datos_frame, width=400, height=100, placeholder_text="Descripción")
descripcion_entry.grid(row=2, column=0, columnspan=2, pady=5, padx=10)

# Botón de Grabación
boton_grabacion = ctk.CTkButton(root, text="Empezar Grabación", fg_color="green")
boton_grabacion.grid(row=2, column=1, pady=10, sticky="ew")

# Sección de Archivo Generado
archivo_generado_frame = ctk.CTkFrame(root, width=250, height=200)
archivo_generado_frame.grid(row=0, column=2, rowspan=2, padx=10, pady=10, sticky="nsew")

archivo_generado_label = ctk.CTkLabel(archivo_generado_frame, text="Archivo Generado", font=("Arial", 16, "bold"))
archivo_generado_label.pack(pady=10)

icono_archivo = ctk.CTkLabel(archivo_generado_frame, text="📄", font=("Arial", 24))
icono_archivo.pack()

ver_archivo_button = ctk.CTkButton(archivo_generado_frame, text="Ver Archivo")
ver_archivo_button.pack(pady=5)

guardar_archivo_button = ctk.CTkButton(archivo_generado_frame, text="Guardar en historial", fg_color="green")
guardar_archivo_button.pack(pady=5)

borrar_archivo_button = ctk.CTkButton(archivo_generado_frame, text="Borrar archivo", fg_color="red")
borrar_archivo_button.pack(pady=5)

# Sección de Audio Capturado
audio_capturado_frame = ctk.CTkFrame(root)
audio_capturado_frame.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

audio_capturado_label = ctk.CTkLabel(audio_capturado_frame, text="Audio Capturado", font=("Arial", 16, "bold"))
audio_capturado_label.pack(pady=10)

barra_reproduccion = ctk.CTkProgressBar(audio_capturado_frame, width=400)
barra_reproduccion.pack(pady=5)

procesar_audio_button = ctk.CTkButton(audio_capturado_frame, text="Procesar audio", fg_color="green")
procesar_audio_button.pack(pady=5)

borrar_audio_button = ctk.CTkButton(audio_capturado_frame, text="Borrar archivo", fg_color="red")
borrar_audio_button.pack(pady=5)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
