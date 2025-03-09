import tkinter as tk
import pygame.mixer


# Configuración de la ventana principal
ventana = tk.Tk()

# Variables globales
reproduciendo = False
cancion_actual = 0
duracion_cancion = 0
progreso_porcentaje = tk.IntVar()
portada = tk.StringVar()
letras = tk.StringVar()
lyrics = []
indice_lyrics = 0

# Base de datos de canciones
canciones = {
    1: {"artista": "Adele", "nombre": "Someone Like You", "archivo": r"C:\Users\jesus\Musica\Adele.mp3", "lrc": r"C:\Users\jesus\Musica\adele.lrc", "desfase": 2.0},
    2: {"artista": "Carlos Vives y Shakira", "nombre": "La Bicicleta", "archivo": r"C:\Users\jesus\Musica\LaBicicleta.mp3", "lrc": r"C:\Users\jesus\Musica\la_kabraa.lrc", "desfase": 2.5},
}

# Constante para el costo por media hora
COSTO_POR_MEDIA_HORA = 8000

def obtener_lista_canciones():
    return [f"{id}: {cancion['artista']} - {cancion['nombre']}" for id, cancion in canciones.items()]

def iniciar_mixer():
    pygame.mixer.init()
    print("Mixer inicializado")