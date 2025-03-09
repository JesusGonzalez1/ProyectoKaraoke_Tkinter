from config import canciones, lyrics, indice_lyrics, letras

def leer_letras(id):
    indice_lyrics = 0
    lyrics.clear()
    letras.set("")
    cancion = canciones[id]
    try:
        with open(cancion["lrc"], "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if "]" in linea:
                    tiempo = linea.split("]")[0].strip("[")
                    letra = linea.split("]")[1].strip()
                    minutos, segundos = tiempo.split(":")
                    segundos_total = float(minutos) * 60 + float(segundos) + cancion["desfase"]
                    lyrics.append([segundos_total, letra])
    except Exception as e:
        print(f"Error al leer el archivo LRC: {e}")
