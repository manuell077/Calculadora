from tkinter import *



#funcion para mandar numeros a la pantalla 


def CaracteresPantalla(seleccion):
    
    if resultado.get() == "0":#si el label resultado es igual a 0 entonces que borre ese 0 y quede en blanco y escriba el valor que ingreso 
        
        resultado.set("")
        resultado.set(seleccion)
          

    else:#si ya no es cero que se siga concatenando
        
        resultado.set(resultado.get()+seleccion)
    

#funcion para sumar numeros
def Suma():
    
    global operador
    global valor1
    valor1 = int(resultado.get())#obtenemos el valor 1 
    operacion.set(resultado.get() + "+")#el valor obtenido de resultado cuando le dio al boton "+" se guarde y se mand a operacion
    resultado.set("")
    operador = "suma"#si es una suma decimos que operador  es una suma
    
def igual():
    
    global suma
     
    
    if operador == "suma":#le decimos que si operador es de tipo suma entonces que realice las operaciones
        
       valor2 = int(resultado.get())
       operacion.set(operacion.get()+ resultado.get())#que el valor de resultado se concatene en operacion
       resultado.set("")
       suma = valor1 + valor2#operacion de para sumar los dos valores obtenidos
       resultado.set(suma)#enviar  el resultado de la operacion al label resultado 
       
       
         
       
        
        


raiz = Tk()#raiz del proyecto
raiz.title("Calculadora")


raiz.iconbitmap("imagenes/calculadora.ico")

frame = Frame(raiz,width=40)#frame del proyecto
frame.pack()#empaquetamos la calculadora





#StringVars que van a ser modificables
operacion = StringVar()
resultado = StringVar()
operacion.set("0")
resultado.set("0")



#labels de operacion y el resultado

Labeloperacion = Label(frame,textvariable=operacion)
Labeloperacion.config(font=("ARIAL", 15))
Labeloperacion.grid(row=0,column=0,columnspan=4,sticky="e")
LabelResultaod = Label(frame,textvariable=resultado)
LabelResultaod.config(font=("ARIAL", 15))
LabelResultaod.grid(row=1,column=0,columnspan=4,sticky="e")

#Buttons de numeros y operaciones

Boton_7 = Button(frame,text="7",width=10,height=3,command=lambda:CaracteresPantalla("7"))
Boton_7.grid(row=2,column=0,sticky="NSEW")
Boton_8 = Button(frame,text="8",width=10,height=3,command=lambda:CaracteresPantalla("8"))
Boton_8.grid(row=2,column=1,sticky="NSEW")
Boton_9 = Button(frame,text="9",width=10,height=3,command=lambda:CaracteresPantalla("9"))
Boton_9.grid(row=2,column=2,sticky="NSEW")
Boton_10 = Button(frame,text="+",width=10,height=3,command=lambda:Suma())
Boton_10.grid(row=2,column=3,sticky="NSEW")
Boton_4 = Button(frame,text="4",width=10,height=3,command=lambda:CaracteresPantalla("4"))
Boton_4.grid(row=3,column=0,sticky="NSEW")
Boton_5 = Button(frame,text="5",width=10,height=3,command=lambda:CaracteresPantalla("5"))
Boton_5.grid(row=3,column=1,sticky="NSEW")
Boton_6 = Button(frame,text="6",width=10,height=3,command=lambda:CaracteresPantalla("6"))
Boton_6.grid(row=3,column=2,sticky="NSEW")
Boton_11 = Button(frame,text="-",width=10,height=3,command=lambda:CaracteresPantalla("-"))
Boton_11.grid(row=3,column=3,sticky="NSEW")
Boton_1 = Button(frame,text="1",width=10,height=3,command=lambda:CaracteresPantalla("1"))
Boton_1.grid(row=4,column=0,sticky="NSEW")
Boton_2 = Button(frame,text="2",width=10,height=3,command=lambda:CaracteresPantalla("2"))
Boton_2.grid(row=4,column=1,sticky="NSEW")
Boton_3 = Button(frame,text="3",width=10,height=3,command=lambda:CaracteresPantalla("3"))
Boton_3.grid(row=4,column=2,sticky="NSEW")
Boton_12 = Button(frame,text="x",width=10,height=3,command=lambda:CaracteresPantalla("x"))
Boton_12.grid(row=4,column=3,sticky="NSEW")
Boton_Porcentaje = Button(frame,text="%",width=10,height=3,command=lambda:CaracteresPantalla("%"))
Boton_Porcentaje.grid(row=5,column=0,sticky="NSEW")
Boton_0 = Button(frame,text="0",width=10,height=3,command=lambda:CaracteresPantalla("0"))
Boton_0.grid(row=5,column=1,sticky="NSEW")
Boton_Diviendo = Button(frame,text="/",width=10,height=3,command=lambda:CaracteresPantalla("/"))
Boton_Diviendo.grid(row=5,column=2,sticky="NSEW")
Boton_Resultado = Button(frame,text="=",width=10,height=3,command=lambda:igual())
Boton_Resultado.grid(row=5 ,column=3,sticky="NSEW")




raiz.mainloop()#un ciclo para que se repita la ventana





