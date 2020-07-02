# aqui se pondran las funciones del teclado y se enviaran
# a la pantalla que tenemos en el disenyo
from tkinter import *
import operaciones_calc

class PresionarCalculadora():

    def __init__(self, num):
        # Numeros
        self.__botonN   = num
        # Operaciones
        self.resultado  = 0.0
        self.contador   = 0
        # propiedades
        self.valorsuma  = False
        self.valorresta = False
        self.valorprod  = False
        self.valordivi  = False


    # ----------------------------- numeros -------------------------------------

    def pushbuttonN(self, presionarboton):
        if presionarboton.get() == "0.":
            presionarboton.set(self.__botonN)
        elif presionarboton.get() != "0." and self.contador == 0:
            presionarboton.set(presionarboton.get() + str(self.__botonN))
        elif presionarboton.get() != "0." and self.contador == 1:
            presionarboton.set(self.__botonN)
            self.contador = 0
    
    # ------------------------------ suma -------------------------------------
    def funcion_suma(self, pantalla):
        if pantalla.get() == "0.":
            pass
        elif len(pantalla.get()) == 0:
            pass
        else:
            self.resultado += float(pantalla.get())
            pantalla.set(self.resultado)
            self.contador   = 1
            self.valorsuma  = True
            self.valorresta = False
            self.valorprod  = False
            self.valordivi  = False
    
    # ------------------------------ igual ------------------------------------
    def igual(self, pantalla):
        
        __variableDiv = 0.0
        __VariableTemp = 0.0

        if len(pantalla.get()) == 0:
            pass
        
        if self.valorsuma == True:
            self.resultado += float(pantalla.get())
            pantalla.set(str(self.resultado))
            self.contador = 0
            self.resultado = 0.0
            self.valorsuma = False
        elif self.valorresta:
            self.resultado -= float(pantalla.get())
            pantalla.set(str(self.resultado))
            self.contador = True
            self.resultado = 0.0
            self.valorsuma = False
        elif self.valorprod:
            self.resultado *= float(pantalla.get())
            pantalla.set(str(self.resultado))
            self.contador = True
            self.resultado = 0.0
            self.valorprod = False
    
    '''
    # ------------------------- numeros 0 y Punto --------------------------------
    def pushbutton0(self, presionarboton):
        ObjOp = operaciones_calc.OperacionesNumericas()
        # Primero comprueba si esta vacio el campo
        if len(presionarboton.get()) == 2 and presionarboton.get() == "0.":
            pass
        else:
            if presionarboton.get() != "0." and ObjOp.funcion_devolver():
                presionarboton.set(presionarboton.get() + self.__boton9)
            elif ObjOp.funcion_devolver() == True:
                presionarboton.set(self.__boton9) 
    
    def pushbuttonP(self, presionarboton):
        ObjOp = operaciones_calc.OperacionesNumericas()
        # Primero comprueba si esta vacio el campo
        if len(presionarboton.get()) == 2 and presionarboton.get() == "0." and ObjOp.contador == 0:
            presionarboton.set("0" + self.__botonP)
        elif len(presionarboton.get()) == 2 and presionarboton.get() == "0." and ObjOp.contador == 1:
            presionarboton.set("0" + self.__botonP)
        else:
            contador = 0
            texto = str()
            texto = presionarboton.get()
            for i in texto:
                if texto[i] == "." and contador == 1:
                    pass
                else:
                    presionarboton.set(presionarboton.get() + self.__botonP)
                    contador = 1
    '''
    #------------------------------ botones borrar -----------------------------
    # Borrar memoria
    def pushbuttonB(self, presionarboton):
        objOp = operaciones_calc.OperacionesNumericas()
        valor = True
        operaciones_calc.OperacionesNumericas.funcion_limpiar(objOp,valor,presionarboton)
        presionarboton.set("0.")
    
    # borrar entry
    def pushbuttonL(self, presionarboton):
        presionarboton.set("0.")
    
    # borrar caracter por caracter
    def pushbuttonR(self, presionarboton):
        if len(presionarboton.get()) == 0:
            pass
        else:
            texto1 = str()
            texto1 = presionarboton.get()
            
            texto2 = []
            texto2 = list(texto1)
            texto2.pop()

            textoS = "".join(texto2)
            
            presionarboton.set(textoS)
    

