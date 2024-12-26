import customtkinter as ctk
from tkinter import font
from config import *
from util.util_ventana import centrar_ventana

class Grabar_Audio(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.config_window()
        self.paneles()
        self.controles_de_navegacion_menu_lateral()
        self.formulario_para_grabar_audio()
        self.opciones_archivos()
        self.opciones_capturar_audio()
        
    def config_window(self):
        self.title("Audio Scribe")
        w, h = 1280, 720
        centrar_ventana(self, w, h)
        self.resizable(False, False)

    def paneles(self):
       #Esta seccion es de los Frame lo cual se agregaran para ir estructurando los elementos de pendiendo de la necesidad
       
       self.menu_lateral = ctk.CTkFrame(self, fg_color=color_secundario, width=170)
       self.menu_lateral.pack(side="left", fill="y") 
       self.menu_lateral.grid_propagate(False)  # Evita que el tamaño del frame cambie según su contenido

      
       self.cuerpo_principal = ctk.CTkFrame(self, fg_color=color_primario) #este es el cuerpo principal donde esta ligado el formulario y el menu derecho
       self.cuerpo_principal.pack(side="right", fill="both", expand=True)  

       
       self.contenedor_menu_derecho_archivo = ctk.CTkFrame(self.cuerpo_principal, fg_color=color_primario, width=320, height=380)
       self.contenedor_menu_derecho_archivo.pack(side="right", fill="y")
       self.contenedor_menu_derecho_archivo.grid_propagate(False)  # Evita que el tamaño del frame cambie según su contenido

       self.menu_derecho_archivo = ctk.CTkFrame(self.contenedor_menu_derecho_archivo, fg_color=color_secundario, width=370, height=380)
       self.menu_derecho_archivo.pack(side="right", fill="x", pady=(0, 140), padx=(0, 60))
       self.menu_derecho_archivo.grid_propagate(False)  # Evita que el tamaño del frame cambie según su contenido
       

       self.vista_formulario_cuerpo_principal = ctk.CTkFrame(self.cuerpo_principal, fg_color=color_primario, width=450, height=480)
       self.vista_formulario_cuerpo_principal.pack(side="left", fill="y", padx=30)

    def controles_de_navegacion_menu_lateral(self):
        #Este es el menu lateral donde se tienen las opciones de navegacion
      
        # Título del menú lateral
        titulo_menu_lateral = ctk.CTkLabel(self.menu_lateral, text="Audio Scribe", font=("Arial", 17, "normal"), fg_color=color_secundario, text_color=color_primario)
        titulo_menu_lateral.grid(row=0, column=0, pady=(17, 32))
        
        # Opciones del menú lateral
        opciones_menu = [
            ("Grabar Formato", self.funcion_grabar_formato),        
            ("Historial Formatos", self.funcion_historial_formatos),
            ("Cerrar Audio Scribe", self.funcion_cerrar_audio_scribe)
        ]
        
        # Texto del menú lateral
        for index, (textoMenu, funcion) in enumerate(opciones_menu, start=1):
            label = ctk.CTkLabel(self.menu_lateral, text=textoMenu, font=("Arial", 14, "bold"), text_color=color_primario, cursor="hand2", fg_color=color_secundario)
            label.grid(row=index, column=0, pady=3, padx=15)
            label.bind("<Button-1>", lambda e, cmd=funcion: cmd())
            self.efecto_hover_menu_texto(label)

    def efecto_hover_menu_texto(self, label):
        # Efecto cuando el mouse está arriba del texto del menú 
        label.bind("<Enter>", lambda e: label.configure(font=("Arial", 14, "bold", "underline")))  # Subrayar al pasar el ratón
        label.bind("<Leave>", lambda e: label.configure(font=("Arial", 14, "bold")))  # Restaurar al salir el ratón

   
   
    def funcion_grabar_formato(self):
        #ESTO MOSTRARA LA VISTA DE GRABAR CUANDO SE LE DE CLICK AL MENU
        Grabar_Audio()
 

    def funcion_historial_formatos(self):
        #ACA SE DEBE AGREGAR EL OBJECTO DE LA VISTA HISTORIAL CUANDO SE LE DE CLICK LO MUESTREE
        print("Historial Formatos seleccionado")
        self.procesar_datos("Historial de formatos")

    def funcion_cerrar_audio_scribe(self):
        self.quit()

    def procesar_datos(self, datos):
        # Función para procesar datos
        print(f"Procesando: {datos}")
        
      
    def formulario_para_grabar_audio(self):
      # Aca solo contiene el formulario y el boton donde se va a interacturar el envios de datos a la base de datos seguramente tengamos que crear un metodo  para el manejo de los datos
        h = 45  
        w = 200
        
        autor_label = ctk.CTkLabel(self.vista_formulario_cuerpo_principal, text="Autor", font=("Arial", 20, "bold"), text_color=color_secundario)
        autor_label.grid(row=0, column=0, columnspan=2, pady=(60, 5))

        nombre_entry = ctk.CTkEntry(self.vista_formulario_cuerpo_principal, width=w, height=h, placeholder_text="Nombre", border_width=1, border_color="black", placeholder_text_color=color_secundario, fg_color=color_primario, text_color=color_secundario)
        nombre_entry.grid(row=1, column=0, pady=5, padx=10)

        apellido_entry = ctk.CTkEntry(self.vista_formulario_cuerpo_principal, width=w, height=h, placeholder_text="Apellido", border_width=1, border_color="black", placeholder_text_color=color_secundario, fg_color=color_primario, text_color=color_secundario)
        apellido_entry.grid(row=1, column=1, pady=5, padx=10)
        
        datos_label = ctk.CTkLabel(self.vista_formulario_cuerpo_principal, text="Datos del archivo", font=("Arial", 20, "bold"), text_color=color_secundario)
        datos_label.grid(row=2, column=0, columnspan=2, pady=10)

        tema_entry = ctk.CTkEntry(self.vista_formulario_cuerpo_principal, width=w, height=h, placeholder_text="Tema", border_width=1, border_color="black", placeholder_text_color=color_secundario, fg_color=color_primario, text_color=color_secundario)
        tema_entry.grid(row=3, column=0, pady=5, padx=10)

        titulo_entry = ctk.CTkEntry(self.vista_formulario_cuerpo_principal, width=w, height=h, placeholder_text="Título", border_width=1, border_color="black", placeholder_text_color=color_secundario, fg_color=color_primario, text_color=color_secundario)
        titulo_entry.grid(row=3, column=1, pady=5, padx=10)

        descripcion_entry = ctk.CTkEntry(self.vista_formulario_cuerpo_principal, width=400, height=100, placeholder_text="Descripción", border_width=1, border_color="black", placeholder_text_color=color_secundario, fg_color=color_primario, text_color=color_secundario)
        descripcion_entry.grid(row=4, column=0, columnspan=2, pady=5)
        
        boton_grabacion = ctk.CTkButton(self.vista_formulario_cuerpo_principal, width=200, height=40, text="Empezar Grabación", fg_color=color_terciario_verde_claro, text_color=color_secundario, font=("Arial", 14, "bold"), corner_radius=0, hover_color=color_terciario_verde_claro, cursor="hand2" )
        boton_grabacion.grid(row=5, column=0, pady=20, columnspan=2)
        self.efecto_hover_boton(boton_grabacion)
        
    def efecto_hover_boton(self, boton):
        #Efecto para cambiar el color de texto del boton
        boton.bind("<Enter>", lambda e: boton.configure(text_color=color_primario))  
        boton.bind("<Leave>", lambda e: boton.configure(text_color=color_secundario))   

    def opciones_archivos(self):
       # Aca se manejara los datos que recibamos de la base de datos para mostrar las opciones que se hara con el archivo

       autor_label = ctk.CTkLabel(self.contenedor_menu_derecho_archivo, text="Archivo Generado", font=("Arial", 20, "bold"), text_color=color_secundario)
       autor_label.place(relx=0.25, rely=0.080)

       self.menu_derecho_archivo.grid_columnconfigure(0, weight=1)
    
       icono_archivo = ctk.CTkLabel(self.menu_derecho_archivo, text="📄", font=("Arial", 24))
       icono_archivo.grid(row=1, column=0, pady=60, sticky="n" )  # Centrado verticalmente

       ver_archivo_button = ctk.CTkButton(self.menu_derecho_archivo, text="Ver Archivo", cursor="hand2")
       ver_archivo_button.grid(row=2, column=0, pady=5, sticky="n")  # Centrado verticalmente

       guardar_archivo_button = ctk.CTkButton(self.menu_derecho_archivo, text="Guardar en historial", fg_color="green", cursor="hand2")
       guardar_archivo_button.grid(row=3, column=0, pady=5, sticky="n")  # Centrado verticalmente

       borrar_archivo_button = ctk.CTkButton(self.menu_derecho_archivo, text="Borrar archivo", fg_color="red", cursor="hand2")
       borrar_archivo_button.grid(row=4, column=0, pady=5, sticky="n")  # Centrado verticalmente

  
    def opciones_capturar_audio(self):
        # Aca se manejara los datos que recibamos de la base de datos para mostrar las opciones, del archivo generado
        h = 40
        audio_capturado_label = ctk.CTkLabel(self.vista_formulario_cuerpo_principal, text="Audio Capturado", font=("Arial", 16, "bold"), text_color=color_secundario)
        audio_capturado_label.grid(row=6, column=0, columnspan=2, pady=(60, 5))
    
        barra_reproduccion = ctk.CTkProgressBar(self.vista_formulario_cuerpo_principal, width=400)
        barra_reproduccion.grid(row=7, column=0, columnspan=2, pady=(60, 5))

        procesar_audio_button = ctk.CTkButton(self.vista_formulario_cuerpo_principal, text="Procesar audio", fg_color="green", height=h, cursor="hand2")
        procesar_audio_button.grid(row=7, column=2, columnspan=2, pady=(7, 5))

        borrar_audio_button = ctk.CTkButton(self.vista_formulario_cuerpo_principal, text="Borrar archivo", fg_color=color_terciario_rojo_claro, height=h, cursor="hand2")
        borrar_audio_button.grid(row=9, column=2, columnspan=2, pady=(7, 5))
        
