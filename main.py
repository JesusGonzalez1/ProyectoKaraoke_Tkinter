import tkinter as tk
from config import ventana, obtener_lista_canciones, iniciar_mixer
from gui import crear_interfaz
from audio import actualizar_progreso

# Inicializar la aplicación
if __name__ == "__main__":
    iniciar_mixer()
    crear_interfaz()
    actualizar_progreso()
    obtener_lista_canciones   
    ventana.mainloop()
