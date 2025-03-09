import pygame
from config import canciones, cancion_actual, reproduciendo, duracion_cancion, portada

def iniciar_mixer():
    pygame.mixer.init()

def reproducir_cancion(id):
    global cancion_actual, reproduciendo, duracion_cancion
    cancion_actual = id
    reproduciendo = True
    cancion = canciones[id]
    pygame.mixer.music.stop()
    pygame.mixer.music.load(cancion["archivo"])
    pygame.mixer.music.play()
    duracion_cancion = pygame.mixer.Sound(cancion["archivo"]).get_length()
    portada.set(cancion["nombre"])

def detener_cancion():
    global reproduciendo
    reproduciendo = False
    pygame.mixer.music.pause()

def reanudar_cancion():
    global reproduciendo
    reproduciendo = True
    pygame.mixer.music.unpause()

def actualizar_progreso():
    from config import progreso_porcentaje, lyrics, letras, indice_lyrics, ventana
    if reproduciendo:
        progreso_segundos = pygame.mixer.music.get_pos() / 1000
        progreso_porcentaje.set((progreso_segundos / duracion_cancion) * 100)

        while indice_lyrics < len(lyrics) and progreso_segundos >= lyrics[indice_lyrics][0]:
            letras.set(lyrics[indice_lyrics][1])
            indice_lyrics += 1

    ventana.after(100, actualizar_progreso)
    ventana.update_idletasks()
