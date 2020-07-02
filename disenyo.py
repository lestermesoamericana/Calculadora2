# Creacion de una calculadora en Python
from tkinter import *
# este modulo me permite tomar una expreison y empezar a evaluarla
import parser

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
def get_number(num):
    global i

    pantalla.insert(i, num)
    i+=1

# ---------------------------- funcion operador ----------------------------
def get_operador(operator):
    global i

    operator_lenght = len(operator)
    pantalla.insert(i, operator)
    i+= operator_lenght

# ------------------------- funcion LimpiarPantalla -------------------------
# para toda la pantalla
def limpiar_pantalla():
    pantalla.delete(0, END)

# para un solo caracter
def undo_character():
    estado_pantalla = pantalla.get()
    # si la pantalla tiene datos
    if len(estado_pantalla):
        # quitar un elemento de la pantalla
        nueva_pantalla = estado_pantalla[:-1]
        # limpiamos la pantalla
        limpiar_pantalla()
        # y lo ingresa a la pantalla
        pantalla.insert(0,nueva_pantalla)
    else:
        limpiar_pantalla()
        pantalla.insert(0, "ERROR")

# ---------------------------- funcion Calcular ----------------------------
def calcular():
    estado_pantalla = pantalla.get()
    try:
        expresion_matematica = parser.expr(estado_pantalla).compile()
        result = eval(expresion_matematica)
        limpiar_pantalla()
        pantalla.insert(0,result)
    except:
        limpiar_pantalla()
        pantalla.insert(0,"ERROR")

#------------------------ Fila1 ---------------------------------------------
# borrar memoria
Button(miFrame, text = "^2", command = lambda: get_operador("**2")).grid(row = 2, 
    column = 0, sticky = W+E)

# borrar dato ingresado
Button(miFrame, text = "CE", command = lambda: limpiar_pantalla()).grid(row = 2, column = 1, sticky = W+E)

# borrar caracter
Button(miFrame, text = "←", command = lambda : undo_character()).grid(row = 2, column = 2, sticky = W+E)

# division
Button(miFrame, text = "➗", command = lambda : get_operador("/")).grid(row = 2, 
    column = 3, sticky = W+E, columnspan = 3)

#------------------------ Fila2 ---------------------------------------------
# numero 7
Button(miFrame, text = "7", command = lambda :get_number(7)).grid(row = 3, 
    column = 0, sticky = W+E) 

# numero 8
Button(miFrame, text = "8", command = lambda :get_number(8)).grid(row = 3, 
    column = 1, sticky = W+E)

# Numero 9
Button(miFrame, text = "9", command = lambda :get_number(9)).grid(row = 3,
    column = 2, sticky = W+E)

# Multiplicacion
Button(miFrame, text = "*", command = lambda : get_operador("*")).grid(row = 3, 
    column = 3, sticky = W+E, columnspan = 3)

#------------------------ Fila3 ---------------------------------------------
# Numero 4
Button(miFrame, text = "4", command = lambda :get_number(4)).grid(row = 4, 
    column = 0, sticky = W+E)

# Numero 5
Button(miFrame, text = "5", command = lambda :get_number(5)).grid(row = 4, 
    column = 1, sticky = W+E)

# Numero 6
Button(miFrame, text = "6", command = lambda :get_number(6)).grid(row = 4, 
    column = 2, sticky = W+E)

# Resta
Button(miFrame, text = "-", command = lambda : get_operador("-")).grid(row = 4, 
    column = 3, sticky = W+E, columnspan = 3)

#------------------------ Fila4 ---------------------------------------------
# numero 1
Button(miFrame, text = "1", command = lambda :get_number(1)).grid(row = 5, 
    column = 0, sticky = W+E)

# numero 2
Button(miFrame, text = "2", command = lambda :get_number(2)).grid(row = 5, 
    column = 1, sticky = W+E)

# numero 3
Button(miFrame, text = "3", command = lambda :get_number(3)).grid(row = 5, 
    column = 2, sticky = W+E)

# suma
Button(miFrame, text = "+", command = lambda : get_operador("+")).grid(row = 5, 
    column = 3, sticky = W+E, columnspan = 3)

#------------------------ Fila5 ---------------------------------------------
# boton 0
Button(miFrame, text = "0", command = lambda :get_number(0)).grid(row = 6, 
    column = 0, sticky = W+E)

# boton Punto (.)
Button(miFrame, text = ".").grid(row = 6, column = 1, sticky = W+E)

# boton %
Button(miFrame, text = "%", command = lambda : get_operador("+")).grid(row = 6, 
    column = 2, sticky = W+E)

# boton igual
Button(miFrame, text = "=", command = lambda : calcular()).grid(row = 6, 
    column = 3, sticky = W+E, columnspan = 3)

# Final del codigo
raiz.mainloop()