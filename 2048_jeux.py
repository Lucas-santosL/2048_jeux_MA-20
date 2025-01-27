"""
name projet: 2048_jeux
autor: Lucas Santos
date: 20.01.25
"""
from tkinter.ttk import Label

from tkinter import *

#initiation de la fenêtre
window = Tk()
window.title("2048")
window.geometry("600x800")

frame_top = Frame(window)
frame_top.pack(fill=X)

score = Label(frame_top, text="Score:" , font=("Arial", 20, "italic", ))
score.pack(side=RIGHT, padx=60, pady=15)

titre = Label(frame_top, text="2048", font=("Arial", 20, "italic"))
titre.pack(side=LEFT, padx=15)

#frames
frame_tableau = LabelFrame(window, width=430, height=420, bg="#848484")
frame_tableau.pack()

frame_bottom = Frame(window)
frame_bottom.pack(fill=X)

#bouton reset
bt_reset = Button(frame_bottom, text="RESET",bg="#7F7F7F", font=("Arial", 20, "italic",))
bt_reset.pack(side=LEFT, padx= 15, pady=20)

nombres= [
    [2, 4, 8, 16,],
    [32, 64, 128, 256,],
    [512, 1024, 2048, 4096,],
    [0, 0, 0, 0 ],
]

#nombres= [
    #[0, 0, 2, 0,],
    #[0, 0, 0, 0,],
    #[0, 0, 0, 0,],
    #[0, 2, 0, 0 ],
#]


cases=[
    [None, None, None, None,],
    [None, None, None, None,],
    [None, None, None, None,],
    [None, None, None, None,],
]

#dictionnaire
couleurs={
    0: "#FFFFFF",
    2: "#DFF2FF",
    4: "#A9EAFE",
    8: "#0F9DE8",
    16: "#CCCCFF",
    32: "#9683EC",
    64: "#1034A6",
    128: "#003399",
    256: "#21177D",
    512: "#6600CC",
    1024: "#7F7F7F",
    2048: "#CECECE",
    4096: "#25FDE9",
    +4096: "#25FDE9"
}

couleurs.get(8192, "#25FDE9")

for line in range(len(nombres)):
    for col in range(len(nombres[line])):
        cases[line][col] = Label(frame_tableau, text=1*nombres[line][col], bg=couleurs[nombres[line][col]], width=7,height=3,relief="solid", fg="#000000",
                                 font=("Arial",15),)
        cases[line][col].place(x=10 + 105 * col, y=10  + 100 * line)

def display_game():
    for line in range(len(nombres)):
        for col in range(len(nombres[line])):
            valeur = nombres[line][col]
            cases[line][col].config(frame_tableau, text=1*nombres[line][col], bg=couleurs[nombres[line][col]])
    return

window.mainloop()