import time
import threading
from config import SONGS

class LyricsSync:
    def __init__(self, app):
        self.current_lyrics = []
        self.is_playing = False
        self.desfase = 0.0
        self.app = app

    def load_lyrics(self, song_title):
        song = next(song for song in SONGS if song["nombre"] == song_title)
        lyrics_path = song["lrc"]
        self.desfase = song["desfase"]
        with open(lyrics_path, "r") as f:
            self.current_lyrics = f.readlines()

    def start(self, song_title):
        self.load_lyrics(song_title)
        self.is_playing = True
        threading.Thread(target=self.sync_lyrics).start()

    def sync_lyrics(self):
        time.sleep(self.desfase)  # Ajustar el desfase inicial
    
        for line in self.current_lyrics:
            if not self.is_playing:
                break
        
            tiempo_espera = 4.5  # ⏳ Ajusta este valor (en segundos) para que la letra fluya mejor
            time.sleep(tiempo_espera)
        
            self.app.display_lyrics(line.strip())  # Actualizar la interfaz con la letra

    def stop(self):
        self.is_playing = False
