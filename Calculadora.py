from tkinter import *  #libreria para la interfaz grafica

'''la estructura de tkinter viene de la siguiente forma

-raiz
-frame
-wigets


''' 

#declaramos una variable con la clase tkinter

raiz = Tk() #en este caso como vamos a crear la raiz la llamamos asi 

raiz.title("Calculadora") #Para ponerle un titulo a nuestra venta utilizamos el metodo title 

raiz.resizable(False,False)#este metodo sirve para que podamos agrandar o no la ventana con un true o un false 


raiz.iconbitmap("imagenes/calculadora.ico")

raiz.geometry("300x500")
# si ponemos algo fuera de este metodo no va a funcionar
raiz.mainloop() #y ponemos este metodo para que se ejecute
#el metodo mainloop  nos sirve ya que para que se nos muestre la ventana tenemos que hacer como un bucle de manera infinita y para eso esta este metodo 





