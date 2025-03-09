import pygame
import os
from config import SONGS

import pygame
import os

class AudioPlayer:
    def __init__(self):
        pygame.mixer.init()  # Inicializa el reproductor de audio

    def play(self, song_title):
        """Reproduce el audio de la canción."""
        song = next((song for song in SONGS if song["nombre"] == song_title), None)

        if song and "archivo" in song:
            audio_path = song["archivo"]

            if os.path.exists(audio_path):  # ✅ Verifica que el archivo existe
                print(f"🎵 Reproduciendo: {audio_path}")

                try:
                    pygame.mixer.music.load(audio_path)  # Cargar el audio
                    pygame.mixer.music.play()  # Reproducir el audio
                    pygame.mixer.music.set_volume(1.0)  # ✅ Asegurar volumen máximo

                except Exception as e:
                    print(f"❌ Error al reproducir audio: {e}")
            else:
                print(f"⚠️ El archivo de audio no existe: {audio_path}")
        else:
            print(f"⚠️ No se encontró la canción '{song_title}' en SONGS")



    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    @staticmethod
    def scan_music_folder(folder_path):
        music_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".mp3"):
                    music_files.append(os.path.join(root, file))
        return music_files

