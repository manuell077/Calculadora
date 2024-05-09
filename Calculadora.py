from tkinter import *#libreria para la interfaz grafica



#funciones 

#funcion para validar que solo se puedan ingresar numeros
def validarNumero(entrada): 
    
    return entrada.isdigit() or entrada == "" #con el metodo isidigit devuelve un true si es un digito y un false si no 
 


'''la estructura de tkinter viene de la siguiente forma

-raiz
-frame
-wigets


''' 

#declaramos una variable con la clase tkinter

raiz = Tk() #en este caso como vamos a crear la raiz la llamamos asi 

raiz.title("Calculadora") #Para ponerle un titulo a nuestra venta utilizamos el metodo title 

raiz.resizable(False,False)#este metodo sirve para que podamos agrandar o no la ventana con un true o un false 


raiz.iconbitmap("imagenes/calculadora.ico")#ponerle un icono a la aplicacion



frame = Frame(raiz) #para crear un frame llamamos a su clase 
frame.config(width="400",height="600") #para ponerle un tamaño a la ventana hacemos lo siguiente , SOLO al frame
frame.pack() #tenemos que empaquetar el frame dentro de la raiz por lo cual utilizamos el siguiente metodo 
frame.config(bg="grey") #para cambiar el color de fondo en este caso del frame 




#input de nuestra calculadora 



vmcd = (raiz.register(validarNumero),"%P")#el register es para registrar una validacion en este caso lo vamos hacer con la funcion ya antes definida
#El %P es el texto que esta dentro del entry este se pasa como parametro a la funcion de validacion para que acceda al texto del entry
entrada = Entry(raiz,font=("Arial",40),validate="key",validatecommand=vmcd)#validate= "key" es para que se le diga que se tiene que realizar la validacion cada vez que se ingresa algo por teclado 
#el validatecommand es una funcion que se llamara cada vez que se tenga que realizar una validacion si devulve true deja realizar la accion si no  impide la accion 
entrada.place(x="0" , y =  "0")
entrada.config(bg="gray")








# si ponemos algo fuera de este metodo no va a funcionar
raiz.mainloop() #y ponemos este metodo para que se ejecute
#el metodo mainloop  nos sirve ya que para que se nos muestre la ventana tenemos que hacer como un bucle de manera infinita y para eso esta este metodo 





