from tkVideoPlayer import TkinterVideo  
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from config import SONGS
from audio import AudioPlayer
from cost import calculate_cost
import os
import pygame

class KaraokeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración básica de la ventana
        self.title("Karaoke")
        self.geometry("750x600")
        self.style = tb.Style(theme="darkly")
        self.configure(bg="#2E2E2E")

        # Variables
        self.song_index = 0
        self.audio_player = AudioPlayer()

        # Crear frames antes de cargar las canciones
        self.create_frames()
        self.create_song_list()
 
        # Imagen
        self.create_image()

        # Cargar canciones
        self.load_songs()

        # Botones
        self.create_buttons()

        # Sección de costo
        self.create_cost_section()

        # Botón de salir
        self.create_exit_button()

        # Crear el reproductor de video 
        self.create_video_player()

    def load_songs(self):
        """Carga todas las canciones detectadas en la carpeta 'songs/'."""
        if not hasattr(self, "song_listbox"):
            print("Error: self.song_listbox no está definido todavía.")
            return

        self.song_listbox.delete(0, tk.END)  

        for song in SONGS:
            self.song_listbox.insert("end", song["nombre"])

    def create_frames(self):
        """Crea los contenedores principales de la interfaz."""
        self.left_frame = ttk.Frame(self, width=200, style="TFrame")
        self.left_frame.pack(side="left", fill="y")

        self.right_frame = ttk.Frame(self, style="TFrame")
        self.right_frame.pack(side="right", expand=True, fill="both") 



    def create_buttons(self):
        """Crea los botones de control en una columna a la izquierda."""
        self.button_frame = ttk.Frame(self.right_frame, style="TFrame")  
        self.button_frame.pack(side="left", padx=20, pady=10, fill="both", expand=True)  

        self.play_button = tb.Button(self.button_frame, text="Play", command=self.play_song, bootstyle="success")
        self.play_button.pack(pady=5, fill="x")

        self.pause_button = tb.Button(self.button_frame, text="Pause", command=self.pause_song, bootstyle="info")
        self.pause_button.pack(pady=5, fill="x")

        self.next_button = tb.Button(self.button_frame, text="Next", command=self.next_song, bootstyle="warning")
        self.next_button.pack(pady=5, fill="x")


    def create_song_list(self):
        """Crea la lista de canciones disponibles."""
        self.song_listbox = tk.Listbox(self.left_frame, selectmode="single", bg="#1C1C1C", fg="#F2F2F2")
        self.song_listbox.pack(fill="y", expand=True)

    def create_cost_section(self):
        """Crea la sección de costo en la segunda columna."""
        self.cost_frame = ttk.Frame(self.right_frame, style="TFrame")
        self.cost_frame.pack(side="right", padx=20, pady=10, fill="both", expand=True)  # Posiciona en la segunda columna

        self.people_label = ttk.Label(self.cost_frame, text="Número de personas:", style="TLabel")
        self.people_label.pack(pady=5)
        self.people_entry = ttk.Entry(self.cost_frame)
        self.people_entry.pack(pady=5)

        self.hours_label = ttk.Label(self.cost_frame, text="Tiempo en horas:", style="TLabel")
        self.hours_label.pack(pady=5)
        self.hours_entry = ttk.Entry(self.cost_frame)
        self.hours_entry.pack(pady=5)

        self.calculate_button = tb.Button(self.cost_frame, text="Calcular Costo", command=self.calculate_cost, bootstyle="primary")
        self.calculate_button.pack(pady=10)

        self.result_label = ttk.Label(self.cost_frame, text="", style="TLabel")
        self.result_label.pack(pady=10)


    def create_video_player(self):
        """Crea el reproductor de video en la interfaz."""
        self.video_container = ttk.Frame(self, style="TFrame")
        self.video_container.pack(side="bottom", fill="x", pady=10)

        self.video_inner_frame = ttk.Frame(self.video_container)
        self.video_inner_frame.pack(side="top", anchor="center")

        self.video_player = TkinterVideo(master=self.video_container, scaled=True)
        self.video_player.config(width=1080, height=720)
        self.video_player.pack()


    def play_video(self, video_path):
        """Carga el video correctamente antes de reproducirlo."""
        if hasattr(self, "video_player"):
            self.video_player.stop()

            try:
                self.video_player.load(video_path)
                self.video_player.seek(0)

                #rapidez del video
                #self.video_player.set_speed(0.90)  
                self.after(500, self.video_player.play)  
            except Exception as e:
                print(f"❌ Error al cargar el video: {e}")



    def create_exit_button(self):
        """Crea el botón de salida."""
        self.exit_button = tb.Button(self.left_frame, text="Salir", command=self.quit, bootstyle="danger")
        self.exit_button.pack(pady=10)

    def create_image(self):
        """Crea la imagen de fondo del karaoke."""
        self.image_frame = ttk.Frame(self.right_frame, style="TFrame")
        self.image_frame.pack(side="top", fill="x", pady=10)

        # Ruta de la imagen dentro del proyecto
        image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "images", "musica.png"))

        if not os.path.exists(image_path):
            print(f"Error: La imagen {image_path} no existe.")
            return

        try:
            self.image = Image.open(image_path)
            self.image = self.image.resize((400, 200), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(self.image)

            self.image_label = ttk.Label(self.image_frame, image=self.photo, style="TLabel")
            self.image_label.image = self.photo
            self.image_label.pack(expand=True, fill="both", padx=20, pady=20)

            self.image_frame.update_idletasks()

            print("✅ Imagen visible en la interfaz.")

        except Exception as e:
            print(f"❌ Error al cargar la imagen: {e}")

    def calculate_cost(self):
        """Calcula el costo según la cantidad de personas y el tiempo de uso."""
        try:
            people = int(self.people_entry.get())
            hours = float(self.hours_entry.get())
            total_cost = calculate_cost(people, hours)
            self.result_label.config(text=f"Costo total: ${total_cost}")
        except ValueError:
            self.result_label.config(text="Por favor, ingresa valores válidos.")

    def play_song(self):
        """Reproduce la canción seleccionada y su video asociado al mismo tiempo."""
        selected_song = self.song_listbox.get(tk.ACTIVE)

    # Buscar la canción seleccionada en SONGS
        song_data = next((song for song in SONGS if song["nombre"] == selected_song), None)
    
        if song_data:
        # ✅ Verifica que la clave 'archivo' exista en el diccionario
            if "archivo" in song_data and song_data["archivo"]:
                print(f"🎶 Reproduciendo audio: {song_data['archivo']}")
                self.audio_player.play(song_data["nombre"])

        # ✅ Verifica que la clave 'video' exista y tenga un valor
            if "video" in song_data and song_data["video"]:
                print(f"🎥 Reproduciendo video: {song_data['video']}")
                self.play_video(song_data["video"])  # ✅ Ahora pasamos la ruta del video correctamente

    # Iniciar el video en lugar de las letras
        self.play_video()


    def pause_song(self):
        """Alterna entre pausar y reanudar el audio y el video."""
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            if hasattr(self, "video_player"):
                self.video_player.pause()
        else:
            pygame.mixer.music.unpause()
            if hasattr(self, "video_player"):
                self.video_player.play()

    def next_song(self):
        """Pasa a la siguiente canción en la lista y sincroniza el video."""
        self.video_player.stop()  
        self.song_index = (self.song_index + 1) % len(SONGS)
        self.song_listbox.select_set(self.song_index)
        
        selected_song = self.song_listbox.get(self.song_index)
        song_data = next((song for song in SONGS if song["nombre"] == selected_song), None)

        if song_data:
            self.audio_player.play(song_data["nombre"])

            if song_data["video"]:
                self.play_video(song_data["video"])
                print(f"🎵 Siguiente canción: {selected_song}")


if __name__ == "__main__":
    app = KaraokeApp()
    app.mainloop()

def next_song(self):
    """Reproduce la siguiente canción en la lista."""
    self.song_index = (self.song_index + 1) % len(SONGS)  
    self.song_listbox.select_clear(0, tk.END)  
    self.song_listbox.select_set(self.song_index)  

    selected_song = self.song_listbox.get(self.song_index)  
    song_data = next((song for song in SONGS if song["nombre"] == selected_song), None)

    if song_data:
        self.audio_player.play(song_data["nombre"])  
        
        if song_data["video"]:  
            self.play_video(song_data["video"])


def play_video(self, video_path):
    """Carga y reproduce el video correctamente."""
    if hasattr(self, "video_player"):
        self.video_player.stop()

        try:
            self.video_player.load(video_path)
            self.video_player.seek(0)  
            self.video_player.play()  

        except Exception as e:
            print(f"❌ Error al cargar el video: {e}")


