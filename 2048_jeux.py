"""
name projet: 2048_jeux
autor: Lucas Santos
date: 10.02.25
"""

from tkinter import *
import random

def pack_4(a, b, c, d):
    moves = 0

    if c == 0 and d != 0:
        c = d
        d = 0
        moves = moves + 1


    if b==0 and c != 0:
        b=c
        c=d
        d=0
        moves = moves + 1

    if a == 0 and b != 0:
        a = b
        b = c
        c = d
        d = 0
        moves = moves + 1

    if a == b and a != 0:
        a = 2 * a
        b = c
        c = d
        d = 0
        moves = moves + 1

    if b == c and b != 0:
        b = 2 * b
        c = d
        d = 0
        moves = moves + 1

    if c==d and c != 0:
        c=2*c
        d=0
        moves = moves + 1

    return a, b, c, d, moves

#avec l'aide de chat gpt
def bouger(direction):
    if direction == "left":
        for i in range(4):
            nombres[i][0], nombres[i][1], nombres[i][2], nombres[i][3], moves = pack_4(nombres[i][0], nombres[i][1], nombres[i][2], nombres[i][3])
    elif direction == "right":
        for i in range(4):
            nombres[i][3], nombres[i][2], nombres[i][1], nombres[i][0], moves = pack_4(nombres[i][3], nombres[i][2], nombres[i][1], nombres[i][0])
    elif direction == "up":
        for j in range(4):
            colonne = pack_4(nombres[0][j], nombres[1][j], nombres[2][j], nombres[3][j])
            for i in range(4):
                nombres[i][j] = colonne[i]
    elif direction == "down":
        for j in range(4):
            colonne = pack_4(nombres[3][j], nombres[2][j], nombres[1][j], nombres[0][j])
            for i in range(4):
                nombres[3 - i][j] = colonne[i]


# Fonction pour mettre à jour l'affichage du jeu
def display_game():
    for row in range(4):
        for col in range(4):
            cases[row][col].config(text=nombres[row][col] if nombres[row][col] != 0 else "", bg=couleurs[nombres[row][col]])

def key_press(event):
    global nombres
    if event.keysym == "Left":
        bouger("left")
    elif event.keysym == "Right":
        bouger("right")
    elif event.keysym == "Up":
        bouger("up")
    elif event.keysym == "Down":
        bouger("down")

    display_game()

# Initialisation de la fenêtre
window = Tk()
window.title("2048")
window.geometry("600x800")

frame_top = Frame(window)
frame_top.pack(fill=X)

score = Label(frame_top, text="Score:" , font=("Arial", 20, "italic"))
score.pack(side=RIGHT, padx=60, pady=15)

titre = Label(frame_top, text="2048", font=("Arial", 20, "italic"))
titre.pack(side=LEFT, padx=15)

# Frames
frame_tableau = LabelFrame(window, width=430, height=420, bg="#848484")
frame_tableau.pack()

frame_bottom = Frame(window)
frame_bottom.pack(fill=X)

# Bouton reset
bt_reset = Button(frame_bottom, text="RESET", bg="#7F7F7F", font=("Arial", 20, "italic"))
bt_reset.pack(side=LEFT, padx=15, pady=20)

# Initialisation de la grille avec des valeurs
nombres = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

positions = random.sample([(x, y) for x in range(len(nombres)) for y in range(len(nombres))], 2) # Affichage aléatoire sur la grille (avec ChatGPT)for x, y in positions:
for x, y in positions:
    nombres[x][y] = 2 # Placer un "2" sur la grille

#nombres= [
    #[2, 4, 8, 16,],
    #[32, 64, 128, 256,],
    #[512, 1024, 2048, 4096,],
    #[0, 0, 0, 0 ],
#]



cases = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
]

couleurs = {
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
    4096: "#25FDE9"
}

# Création des labels pour afficher la grille
for row in range(4):
    for col in range(4):
        cases[row][col] = Label(frame_tableau, text="", bg=couleurs[nombres[row][col]], width=7, height=3, relief="solid", fg="#000000", font=("Arial", 15))
        cases[row][col].place(x=10 + 105 * col, y=10 + 100 * row)


# Fonction pour gérer les déplacements via les flèches
window.bind("<Left>", key_press)
window.bind("<Right>", key_press)
window.bind("<Up>", key_press)
window.bind("<Down>", key_press)

# Affichage initial
display_game()

# Lancer la boucle principale Tkinter
window.mainloop()
