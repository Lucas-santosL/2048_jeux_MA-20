"""
name projet: 2048_jeux
autor: Lucas Santos
date: 20.01.25
"""
from tkinter import *


window = Tk()
window.title("2048")
window.geometry("400x400")

frame_fenetre = LabelFrame(window)
frame_fenetre.pack(fill=X)

frame_top = Frame(window)
frame_top.pack(fill=X)

score = Label(frame_top, text="Score:", font=("Arial, 20"))
score.pack(side=RIGHT, padx=60)

titre = Label(frame_top, text="2048", font=("Arial, 20"))
titre.pack(side=LEFT, padx=10)

nombres= [
    ["2", "4", "8", "16",]
    ["32", "64", "128", "256",]
    ["512", "1024", "2048", None,]
    [None, None, None, None]
]

cases=[
    [None, None, None, None,]
    [None, None, None, None,]
    [None, None, None, None,]
    [None, None, None, None,]
]




window.mainloop()