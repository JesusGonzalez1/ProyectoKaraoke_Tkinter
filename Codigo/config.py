import os

# Carpeta donde se almacenarán las canciones y videos
SONGS_DIR = os.path.join(os.path.dirname(__file__), "songs")
VIDEOS_DIR = os.path.join(os.path.dirname(__file__), "videos")

# Cargar canciones automáticamente desde la carpeta `songs/`
SONGS = []

if os.path.exists(SONGS_DIR):
    for file in os.listdir(SONGS_DIR):
        if file.endswith(".mp3"):
            song_name = os.path.splitext(file)[0]  # Nombre sin extensión
            song_path = os.path.join(SONGS_DIR, file)

            # Buscar un video con el mismo nombre que la canción
            video_path = os.path.join(VIDEOS_DIR, f"{song_name}.mp4")

            SONGS.append({
                "artista": "Desconocido",
                "nombre": song_name,
                "archivo": song_path,
                "video": video_path if os.path.exists(video_path) else None,  
            })