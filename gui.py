import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb
from config import ventana, progreso_porcentaje, portada, letras
from audio import reproducir_cancion, detener_cancion, reanudar_cancion
from cost import calcular_costo

# Cambiar el tema dinámicamente
def cambiar_tema():
    global tema_actual
    nuevo_tema = "cyborg" if tema_actual == "solar" else "solar"
    estilo.theme_use(nuevo_tema)
    tema_actual = nuevo_tema

# Efecto de brillo en botones
def on_enter(e):
    e.widget.config(bg="#00ffff", fg="black")

def on_leave(e):
    e.widget.config(bg="#222", fg="white")

# Configuración de la ventana principal
ventana.title("Karaoke Futurista")
ventana.geometry("1080x700")
ventana.resizable(False, False)

# Aplicar un estilo moderno
estilo = tb.Style()
tema_actual = "solar"
estilo.theme_use(tema_actual)

# Imagen de fondo
bg_image = tk.PhotoImage(file="musica.png")  # Asegúrate de tener esta imagen
bg_label = tk.Label(ventana, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

frame_izquierda = tk.Frame(ventana, bg="#222", bd=10, relief="flat")
frame_izquierda.pack(side="left", padx=20, pady=20, fill="both", expand=True)

label_titulo = tk.Label(frame_izquierda, text="BIENVENIDO AL KARAOKE", font=("Orbitron", 20, "bold"), bg="#222", fg="#00ffff")
label_titulo.pack(pady=20)

# Campo de entrada para cálculo de costo
tk.Label(frame_izquierda, text="Número de personas:", font=("Arial", 12), bg="#222", fg="white").pack(pady=5)
entry_personas = tk.Entry(frame_izquierda, font=("Arial", 12), bg="#333", fg="white", relief="flat")
entry_personas.pack(pady=5)

# Tiempo en horas
tk.Label(frame_izquierda, text="Tiempo en horas:", font=("Arial", 12), bg="#222", fg="white").pack(pady=5)
entry_tiempo = tk.Entry(frame_izquierda, font=("Arial", 12), bg="#333", fg="white", relief="flat")
entry_tiempo.pack(pady=5)

# Botón de calcular costo
btn_calcular = tk.Button(frame_izquierda, text="Calcular Costo", font=("Arial", 14), bg="#222", fg="white", relief="flat", command=lambda: calcular_costo(entry_tiempo, entry_personas))
btn_calcular.pack(pady=10)
btn_calcular.bind("<Enter>", on_enter)
btn_calcular.bind("<Leave>", on_leave)

# Botón para cambiar el tema
tk.Button(frame_izquierda, text="Cambiar Tema", font=("Arial", 14), bg="#222", fg="white", relief="flat", command=cambiar_tema).pack(pady=10)

# Marco para la interfaz de la canción
frame_cancion = tk.Frame(frame_izquierda, bg="#111", bd=10, relief="flat")
frame_cancion.pack(padx=20, pady=20, fill="both", expand=True)

# Texto de la canción
tk.Label(frame_cancion, textvariable=portada, font=("Orbitron", 18), bg="#111", fg="#00ffff").pack(pady=10)
tk.Label(frame_cancion, textvariable=letras, font=("Arial", 16), bg="#111", fg="white", wraplength=600).pack(pady=10)

# Botones de control
btn_play = tk.Button(frame_cancion, text="⏯", font=("Arial", 18), bg="#222", fg="white", relief="flat", command=lambda: detener_cancion() if reanudar_cancion else reproducir_cancion())
btn_play.pack(side="left", padx=10, pady=10)
btn_play.bind("<Enter>", on_enter)
btn_play.bind("<Leave>", on_leave)

btn_skip = tk.Button(frame_cancion, text="⏩", font=("Arial", 18), bg="#222", fg="white", relief="flat")
btn_skip.pack(side="left", padx=10, pady=10)
btn_skip.bind("<Enter>", on_enter)
btn_skip.bind("<Leave>", on_leave)

# Barra de progreso
ttbar = ttk.Progressbar(frame_cancion, orient="horizontal", length=600, mode="determinate", variable=progreso_porcentaje)
ttbar.pack(side="bottom", padx=40, pady=20)

ventana.mainloop()