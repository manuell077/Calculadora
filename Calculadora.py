from tkinter import *  #libreria para la interfaz grafica

resultado = 0
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



frame = Frame() #para crear un frame llamamos a su clase 
frame.config(width="400",height="600") #para ponerle un tamaño a la ventana hacemos lo siguiente , SOLO al frame

frame.pack() #tenemos que empaquetar el frame dentro de la raiz por lo cual utilizamos el siguiente metodo 
frame.config(bg="grey") #para cambiar el color de fondo en este caso del frame 


resultadoLabel = Label(frame,text=resultado,font=("Arial",60))#Aqui es un label de tipo texto que va a mostrar el resultado que tenemos almacenado en una variable llamada "resultado" ademas le decimos el tipo de fuente y el tamaño con el parametro font("nombreFuente",tamaño)
#la estructura de un label es label(contenedorPadre,opcion) hay diferentes opciones
resultadoLabel.config(bg="grey")#cambiamos el color de fondo del label 
resultadoLabel.place(x=330 , y= 50)#aqui mediante el metodo place podemos ubicar el texto dentro del contenedor padre con unas cordenadas "x" "y" 


# si ponemos algo fuera de este metodo no va a funcionar
raiz.mainloop() #y ponemos este metodo para que se ejecute
#el metodo mainloop  nos sirve ya que para que se nos muestre la ventana tenemos que hacer como un bucle de manera infinita y para eso esta este metodo 





