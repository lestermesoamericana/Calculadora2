# Creacion de una calculadora en Python
from tkinter import *

# creacion de raiz para el frame principal
raiz = Tk()
raiz.title("Calculadora")

miFrame = Frame(raiz, width = 220, height = 220)
miFrame.pack()

# ----------------------- PANTALLA-------------------------------------------
# Variable para aceptar numero en pantalla
numeros_pantalla = StringVar()

pantalla = Entry(miFrame)
pantalla.grid(row = 1, columnspan = 6, sticky = W + E)

# Creacion de un indice que nos permitira ir mostrando
# y acumulando los resultados
i = 0

# -------------------------- funcion poner numeros --------------------------
def getnumber(num):
    global i

    pantalla.insert(i, num)
    i+=1

#------------------------ Fila1 ---------------------------------------------
# borrar memoria
Button(miFrame, text = "C").grid(row = 2, column = 0, sticky = W+E)

# borrar dato ingresado
Button(miFrame, text = "CE").grid(row = 2, column = 1, sticky = W+E)

# borrar caracter
Button(miFrame, text = "←").grid(row = 2, column = 2, sticky = W+E)

# division
Button(miFrame, text = "➗").grid(row = 2, column = 3, sticky = W+E, columnspan = 3)

#------------------------ Fila2 ---------------------------------------------
# numero 7
Button(miFrame, text = "7", command = lambda :getnumber(7)).grid(row = 3, 
    column = 0, sticky = W+E) 

# numero 8
Button(miFrame, text = "8", command = lambda :getnumber(8)).grid(row = 3, 
    column = 1, sticky = W+E)

# Numero 9
Button(miFrame, text = "9", command = lambda :getnumber(9)).grid(row = 3,
    column = 2, sticky = W+E)

# Multiplicacion
Button(miFrame, text = "*").grid(row = 3, column = 3, sticky = W+E, columnspan = 3)

#------------------------ Fila3 ---------------------------------------------
# Numero 4
Button(miFrame, text = "4", command = lambda :getnumber(4)).grid(row = 4, 
    column = 0, sticky = W+E)

# Numero 5
Button(miFrame, text = "5", command = lambda :getnumber(5)).grid(row = 4, 
    column = 1, sticky = W+E)

# Numero 6
Button(miFrame, text = "6", command = lambda :getnumber(6)).grid(row = 4, 
    column = 2, sticky = W+E)

# Resta
Button(miFrame, text = "-").grid(row = 4, column = 3, sticky = W+E, columnspan = 3)

#------------------------ Fila4 ---------------------------------------------
# numero 1
Button(miFrame, text = "1", command = lambda :getnumber(1)).grid(row = 5, 
    column = 0, sticky = W+E)

# numero 2
Button(miFrame, text = "2", command = lambda :getnumber(2)).grid(row = 5, 
    column = 1, sticky = W+E)

# numero 3
Button(miFrame, text = "3", command = lambda :getnumber(3)).grid(row = 5, 
    column = 2, sticky = W+E)

# suma
Button(miFrame, text = "+").grid(row = 5, column = 3, sticky = W+E, columnspan = 3)

#------------------------ Fila5 ---------------------------------------------
# boton 0
Button(miFrame, text = "0", command = lambda :getnumber(0)).grid(row = 6, 
    column = 0, sticky = W+E)

# boton Punto (.)
Button(miFrame, text = ".").grid(row = 6, column = 1, sticky = W+E)

# boton %
Button(miFrame, text = "%").grid(row = 6, column = 2, sticky = W+E)

# boton igual
Button(miFrame, text = "=").grid(row = 6, column = 3, sticky = W+E, columnspan = 3)

# Final del codigo
raiz.mainloop()