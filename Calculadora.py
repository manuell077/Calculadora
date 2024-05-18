from tkinter import *


#funciones para poner atributos por defecto
def ButtonAtributos(contenedor,texto,x,y):#atributos de button 
    
    nombre = Button(contenedor,text=texto,height=8,width=10)
    nombre.grid(row=x,column=y , sticky="nsew")

    return nombre

def LabelAtributos(contenedor,texto,x,y):
    
    label = Label(contenedor,textvariable=texto,justify="right",height=3)
    label.config(font=("ARIAL",15))#tamaño de fuente recibe como parametros el nombre de la fuente y el tamaño 
    label.grid(row=x,column=y)
    

    
    return label


raiz = Tk()#raiz del proyecto
raiz.title("Calculadora")
raiz.resizable(False,False)

raiz.iconbitmap("imagenes/calculadora.ico")

frame = Frame(raiz,width=40)#frame del proyecto
frame.pack()#empaquetamos la calculadora


#variables que van a  enviar una notificacion cuando sean modificadas
resultado = StringVar()
resultado.set("0") #Que el texto por defecto sea 0 por eso mandamos 0 con set
operacion = StringVar()
operacion.set("0")

#label que van a tener nuestra aplicacion 

LabelOperacion = LabelAtributos(frame,operacion,0,3)
LabelResultado = LabelAtributos(frame,resultado,1,3)



#los buttons que van a tener nuestra aplicacion
button_1 = ButtonAtributos(frame,"1",2,0)
button_2 = ButtonAtributos(frame,"2",2,1)
button_3 = ButtonAtributos(frame,"3",2,2)
button_4 = ButtonAtributos(frame,"4",3,0)
button_5 = ButtonAtributos(frame,"5",3,1)
button_6 = ButtonAtributos(frame,"6",3,2)
button_7 = ButtonAtributos(frame,"7",4,0)
button_8 = ButtonAtributos(frame,"8",4,1)
button_9 = ButtonAtributos(frame,"9",4,2)
button_0 = ButtonAtributos(frame,"0",5,0)
button_multiplicar = ButtonAtributos(frame,"X",2,3)
button_Sumar = ButtonAtributos(frame,"+",5,1)
button_Restar = ButtonAtributos(frame,"-",5,2)
button_Dividir = ButtonAtributos(frame,"/",3,3)
button_Porcentaje = ButtonAtributos(frame,"%",4,3)
button_Resultado = ButtonAtributos(frame,"=",5,3)




raiz.mainloop()#un ciclo para que se repita la ventana





