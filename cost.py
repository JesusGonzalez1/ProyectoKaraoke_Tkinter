from tkinter import messagebox
from config import COSTO_POR_MEDIA_HORA

def calcular_costo():
    try:
        tiempo = float(tiempo.get())
        personas = int(personas.get())
        costo_total = int(tiempo * 2 * COSTO_POR_MEDIA_HORA)
        messagebox.showinfo("Costo Total", f"Tiempo: {tiempo} horas\nPersonas: {personas}\nCosto Total: {costo_total} pesos")
    except ValueError:
        messagebox.showerror("Error", "Entrada inválida.")

