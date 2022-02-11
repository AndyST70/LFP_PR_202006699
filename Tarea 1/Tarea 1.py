from tkinter import filedialog, Tk
    
def abrir(): #definimos la función del
    Tk().withdraw() #evita que quede anclada
    archivo = filedialog.askopenfile(
        title = "ingresa tu archivo",
        initialdir = "./",
        filetypes= [
            ("archivo txt", "*.txt"),
            ("todos los archivos", "*.*")

            # * significa 0 o más caracteres
            #*.* cualquieer cosa
            #lee data.txt    
        ]
    )
    if archivo is None:
        print("No se selecciono un archivo \n'")
        return None
    else: 
        text = archivo.read()    
        archivo.close()
        return text


if __name__ == '__main__':
    #variables gloables
    txt = abrir()
    contadorcaracteres=0
    contadornum=0
    contadorsimbolos = 0
    lista = []
    if txt is not None:   #si es nulo"
       # print(txt)
       
        if (len(txt)>0):
            for c in txt: #esto recorre el archivo
                if c=="\n":
                    pass
                elif c == " ": 
                    pass
                else: 
                    listaAux = [ord(c), c]
                    lista.append(listaAux)

                """
                if c.isdigit():
                    contadornum +=1
                
                else: 
                    if c.isalpha(): 
                     contadorcaracteres +=1
                    else : 
                         lista_numeros = [c]
                """   
            for datos in lista:
                #contador de letras
                if ((datos[0]>= 65) and (datos[0]<=90)) or ((datos[0]>= 97)and (datos[0]<=116)) or ((datos[0]>=164)and(datos[0]<=165)): 
                      contadorcaracteres +=  1
                else: 
                    #contador de numeros
                    if ((datos[0]>=48) and (datos[0]<= 57)):                         
                        contadornum +=1
                        #contador de simbolos
                    else: 
                        if ((datos[0]>=33) and (datos[0]<= 46))or ((datos[0]>= 58)and(datos[0]<=64)):                         
                            contadorsimbolos +=1        
            print("\n el número de digitos es: "+ str(contadornum))
            print("\n el numero de letras es: " + str(contadorcaracteres))
            print("\n el numero de simbolo es: " + str(contadorsimbolos))
        else: print("No hay texto, no seas troll jsjsjs")

    else:
        print( "no te topo. \n")
