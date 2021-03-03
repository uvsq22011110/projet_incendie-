#########################################
# groupe MPCI 6
# OUCHERIF Lounis
# ZAGBAHI Godi
# LIGER Arthur
# MORCOS DOUEIHY Jean-Paul
# ROBINSON Andry
#
# https://github.com/uvsq22011110/projet_incendie-
###################################


import tkinter as tk
import random

root = tk.Tk()
root.title("Propagation d'incendie ")
#les constantes
L = 500
WIDTH, HEIGHT = L, L
couleurs=["blue","yellow","green"]
n = 4
p = 4
# les variables
coul=random.choice(couleurs)

# les fonctions 
#def feu(event):
    ###########
    # x = event.x
    # y = event.y
    # coul= red
    # la case (x,y) devien reouge

#debut du code

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, borderwidth=5)
canvas.grid()
rectangle = []
for i in range(10):
    for j in range(10):
        rectangle_ = canvas.create_rectangle(i * L // 10, j * L // 10, (i + 1) * L // 10, (j + 1) * L // 10,fill="black")
        rectangle.append(rectangle_)

for i in range(1,11): 
    canvas.create_line(0,i * L // 10,L,i * L // 10,fill = "white")
    canvas.create_line(i * L // 10,0,i * L // 10,L,fill = "white")

        

root.mainloop()