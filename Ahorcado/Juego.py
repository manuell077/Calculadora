from random import * 

global i
i = True
linea = []
palabras= ["juego","python","ruby"]
equivocaciones = 3
guardarLetra = ""
cont = 0
while(i == True):
    
    print("Bienvenido al juego del ahorcado")
    print("Selecciona un numero")
    print("1.Agregar palabra 2.Configurar 3.Jugar 4.Salir")
    
    valor = int(input("Selecciona un numero"))
    
    
    if valor == 1:
        
        letra = input("Dame una palabra")
        palabras.append(letra)
        
    elif valor == 2:
        
        eq = int(input("Equivocaciones permitidas"))
        equivocaciones = eq 
        
    elif valor ==3: 
        
        cantidadDeplabras = len(palabras)
        palabraAleatroia = randint(0,cantidadDeplabras)
        longitudReal = palabraAleatroia - 1
        
        palabraSeleccionada = palabras[longitudReal]
        letrasPalabraSeleccionada = len(palabraSeleccionada)
        
        print(palabraSeleccionada)
        for x in range(letrasPalabraSeleccionada):
            
            linea.append("_")
            espacios = "".join(linea)
            
        print(espacios)

        LetraIng = input("Dame una letra")
         
        for c in palabraSeleccionada:
             
             
            cont += 1
             
            if LetraIng == c:
                posicionLetra = cont
                guardarLetra += LetraIng
                   
        
            
           
              
        
            
    elif valor == 4:        
      
        i = False   
        
     
        
         
                    
                