from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import csv

Lista_Estudiantes = []
Lista_Estudiantes_aprobados = []
Lista_Estudiantes_reprobados = []

def verificar_rut(rut):
    rut = rut.replace('.', '').replace('-', '')
    numero = rut[:-1]
    digito_verificador = rut[-1].upper()

    if len(numero) < 7 or len(numero) > 8:
        return False

    reverso = numero[::-1]
    total = 0
    factor = 2

    for char in reverso:
        total += int(char) * factor
        factor += 1
        if factor > 7:
            factor = 2

    digito_calculado = 11 - (total % 11)
    if digito_calculado == 11:
        digito_calculado = '0'
    elif digito_calculado == 10:
        digito_calculado = 'K'
    else:
        digito_calculado = str(digito_calculado)

    return digito_calculado == digito_verificador

def Registro_Estudiantes(nombre, rut, n1, n2, n3, n4, promedio, estado):
    estudiante = [nombre, rut, n1, n2, n3, n4, promedio, estado]
    Lista_Estudiantes.append(estudiante)

    if promedio >= 4:
        Lista_Estudiantes_aprobados.append(estudiante)
    else:
        Lista_Estudiantes_reprobados.append(estudiante)

def Ver_estudiantes():
    entry_7.delete("1.0", "end")
    for estudiante in Lista_Estudiantes:
        entry_7.insert("end", f"{estudiante}")

def Exportar_estudiantes():
    nombre_archivo = entry_1.get()

    with open(f"{nombre_archivo}_registrados.csv", mode="w", newline="") as archivo_csv:
        agregar_csv = csv.writer(archivo_csv)
        agregar_csv.writerow(["Nombre", "Rut", "Nota 1", "Nota 2", "Nota 3", "Nota 4", "Promedio", "Estado"])
        agregar_csv.writerows(Lista_Estudiantes)

    with open(f"{nombre_archivo}_pasaron.csv", mode="w", newline="") as archivo_csv:
        agregar_csv = csv.writer(archivo_csv)
        agregar_csv.writerow(["Nombre", "Rut", "Nota 1", "Nota 2", "Nota 3", "Nota 4", "Promedio", "Estado"])
        agregar_csv.writerows(Lista_Estudiantes_aprobados)

    with open(f"{nombre_archivo}_no_pasaron.csv", mode="w", newline="") as archivo_csv:
        agregar_csv = csv.writer(archivo_csv)
        agregar_csv.writerow(["Nombre", "Rut", "Nota 1", "Nota 2", "Nota 3", "Nota 4", "Promedio", "Estado"])
        agregar_csv.writerows(Lista_Estudiantes_reprobados)

    entry_7.insert("end", f"Datos exportados a {nombre_archivo}_registrados.csv, {nombre_archivo}_pasaron.csv, y {nombre_archivo}_no_pasaron.csv")

def Buscar_estudiantes():
    buscar_rut = entry_2.get()
    for estudiante in Lista_Estudiantes:
        if estudiante[1] == buscar_rut:
            entry_7.insert("end", f"{estudiante}")
            break
    else:
        entry_7.insert("end", "Estudiante no encontrado.")

def registrar_estudiante():
    nombre = entry_1.get()
    rut = entry_2.get()

    if not verificar_rut(rut):
        entry_7.insert("end", f"El rut {rut} es inválido. Intente nuevamente.")
        return

    try:
        n1 = float(entry_3.get())
        n2 = float(entry_4.get())
        n3 = float(entry_5.get())
        n4 = float(entry_6.get())

        promedio_presentacion =  n1 + n2 + n3 + n4
        promedio_final = promedio_presentacion / 4

        if promedio_final > 7:
            promedio_final = 7
        elif promedio_final < 1:
            promedio_final = 1

        estado = "Aprobado" if promedio_final >= 4 else "Reprobado"

        Registro_Estudiantes(nombre, rut, n1, n2, n3, n4, promedio_final, estado)
        entry_7.insert("end", f"Estudiante {nombre} registrado con promedio {promedio_final} ({estado}).\n")
    except ValueError:
        entry_7.insert("end", "Favor de colocar datos correctos.")
    except:
        entry_7.insert("end", "Lo sentimos, hubo una falla inesperada.")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pussyhunter\Desktop\pruebainterfaz\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1920x1080")
window.configure(bg = "#9F4D4D")

canvas = Canvas(
    window,
    bg = "#9F4D4D",
    height = 900,
    width = 1800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=registrar_estudiante,
    relief="flat"
)
button_1.place(
    x=128.0,
    y=879.0,
    width=354.0,
    height=126.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=Ver_estudiantes,
    relief="flat"
)
button_2.place(
    x=560.0,
    y=879.0,
    width=354.0,
    height=126.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Exportar_estudiantes,
    relief="flat"
)
button_3.place(
    x=972.0,
    y=879.0,
    width=354.0,
    height=126.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=window.quit,
    relief="flat"
)
button_4.place(
    x=1404.0,
    y=879.0,
    width=393.0,
    height=126.0
)

canvas.create_text(
    900.0,
    900.0,
    anchor="nw",
    text="pongame el 6 profe me esforme muxo :0",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    305.0,
    150.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=168.0,
    y=87.0,
    width=274.0,
    height=124.0
)

canvas.create_text(
    236.0,
    48.0,
    anchor="nw",
    text="Nombre:",
    fill="#FFFFFF",
    font=("Inter", 35 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    305.0,
    330.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=168.0,
    y=267.0,
    width=274.0,
    height=124.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    399.5,
    510.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=353.0,
    y=447.0,
    width=93.0,
    height=124.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    210.5,
    510.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=164.0,
    y=447.0,
    width=93.0,
    height=124.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    399.5,
    690.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=353.0,
    y=627.0,
    width=93.0,
    height=124.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    210.5,
    690.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=164.0,
    y=627.0,
    width=93.0,
    height=124.0
)

canvas.create_text(
    272.0,
    228.0,
    anchor="nw",
    text="Rut:",
    fill="#FFFFFF",
    font=("Inter", 35 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    990.0,
    347.5,
    image=entry_image_7
)
entry_7 = Text(
    bd=0,
    bg="#9F4E4E",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=560.0,
    y=87.0,
    width=860.0,
    height=519.0
)

canvas.create_rectangle(
    1758.0,
    21.0,
    1891.0,
    154.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    149.0,
    400.0,
    anchor="nw",
    text="Nota 1:",
    fill="#FFFFFF",
    font=("Inter", 35 * -1)
)

canvas.create_text(
    338.0,
    400.0,
    anchor="nw",
    text="Nota 2:",
    fill="#FFFFFF",
    font=("Inter", 35 * -1)
)

canvas.create_text(
    149.0,
    586.0,
    anchor="nw",
    text="Nota 3:",
    fill="#FFFFFF",
    font=("Inter", 35 * -1)
)

canvas.create_text(
    338.0,
    586.0,
    anchor="nw",
    text="Nota 4:",
    fill="#FFFFFF",
    font=("Inter", 35 * -1)
)

window.resizable(False, False)
window.mainloop()
