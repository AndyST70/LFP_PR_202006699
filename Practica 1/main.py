from tkinter import filedialog, Tk
import matplotlib.pyplot as plt

##########----------------------------------------------------------------
lst_aux_result = [] 
lst_aux_Pro = []
arre_produ_final  = []
#Reseteamos nuestras variables
mes_2 = ""
año_2 = ""
# reseteamos nuestras variables 
Grafica_Final = "",
Titulo_Final = "",
Titulo_Final = "",
TituloX_Final = "",
TituloY_Final = ""

#Abrimos el archivo y cargamos
def cargar():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Seleccionar un archivo",
        initialdir = "./",
        filetypes = [
            #Definimos los tipo de archivo
            ("archivos data", "*.data"),
            ("todos los archivos",  "*.*")
        ]
    )
    #si no se seleccióno ningun archivo
    if archivo is None:
        print('No se selecciono ningun archivo\n')
        return None
    else:
        #Leer el texto
        texto = archivo.read()
        archivo.close()
        return texto #retorna nuestro texto


def parse_Mes(chars: list):
    Anio_Mes = ""
    Anio_Mes_pase = Anio_Mes.join(chars).strip()
    list_Mes = Anio_Mes_pase = Anio_Mes_pase.split(" ")
    Lista_Meses=[]
    for Lista_Meses in list_Mes:
        Mes_propiedades = Lista_Meses.split(";")
def cargarlfp():

    Tk().withdraw()
    archivo_2 = filedialog.askopenfile(
        title = "Seleccionar un archivo",
        initialdir = "./",
        filetypes = [
            #Definimos los tipo de archivo
            ("archivos lfp", "*.lfp"),
            ("todos los archivos",  "*.*")
        ]
    )
    #si no se seleccióno ningun archivo
    if archivo_2 is None:
        print('No se selecciono ningun archivo\n')
        return None
    else:
        #Leer el texto
        texto_2 = archivo_2.read()
        archivo_2.close()
        return texto_2 #retorna nuestro texto

#def graficaXY():




def isLetra(char):
    if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
        return True
    return False

def isNumero(char):
    if ord(char) >= 48 and ord(char) <= 57:
        return True
    return False

def isSimbolos(char):
    if ord(char) == 32 or ord(char) == 10 or ord(char) == 9:
        return True
    return False

if __name__ == '__main__':
    

    while True:
        print("----------------Menu--------------",
               "\n 1. Cargar archivos",
               "\n 2. Cargar instrucciones",
               "\n 3. Analizar",
               "\n 4. Reportes",
               "\n 5. Salir",
               "\n 6. Probar función",
               "\n ------------------------------",
               
               )
        opc = input ("OPCIÓN: ")
        if opc == "1":
            
# convertir datos e imprimir        
            txt = cargar()
            lista = [] 
            lista_letters =[] # guardamos contenido
            ls_Mes = [] # guardamos
            ls_Año=[]# guardamos
            ls_productos=[]#guardamos
            if txt is not None:
                if(len(txt)>0):# verificamos el ingreso
                    for c in txt: #recorremos nuestro texto 
                        if c == "\n": 
                            pass
                        elif c == " ": 
                            pass
                        else: 
                            listaAux = [ord(c), c]
                            lista.append(listaAux)
                            lista_letters.append(c)

                    contadorauxiliaranio_1 = 0 # contador del año: guarda registros
                    contadorauxiliarmes_2 =0 # contador de mes: guarda datos del mes
                    for a in lista:
                        # Se obtiene el año, al igual que sus caracteres
                        if ((a[0]>= 48) and ( a[0] <= 57) and (contadorauxiliaranio_1 < 4)):
                            contadorauxiliaranio_1 +=1
                            ls_Año.append(a[1])
                            año = "".join(ls_Año)
                            año_2 = año
                        else: 
                            contadorauxiliaranio_1 == 4

                        # Se obtiene el mes, al igual que sus caracteres
                        if((a [0] != 58) and (contadorauxiliarmes_2<1)):
                            ls_Mes.append(a[1])
                            mes= "".join(ls_Mes)
                            mes = mes_2 

                        else: 
                            contadorauxiliarmes_2 =1

                        # Obtenemos el producto y sus caracteristicas
                        if(a[0] == 40):
                            agrega =lista_letters.index("(")
                            pro = lista_letters[agrega+1: len(lista_letters)-1]
                            produc = "".join(pro) # imprime juntos los datos
                            txtaux = produc.split(";") #split separa por , y comas
                            auxipro = txtaux
                    print("Mes: "+ mes)
                    print("El año es "+ año)
                    #print(auxipro)
                    a1 =  "\""
                    for pro in range (len(auxipro)):
                        pi_pro = auxipro[pro].split(",")
                        if auxipro[pro] != "":
                        #  print ("Productos ", pro+1, ";",auxipro[pro])
        
                            Nombre_producto = pi_pro[0].replace("[", "")

                            Nombre_Producto = Nombre_producto.replace(a1,"") 
                            lst_aux_Pro.append(Nombre_Producto)
                            p1 = pi_pro[1]#p1 = precio
                            p2 = pi_pro[2].replace("]", "")#p2 = cantidad de producto
                            base = float(p1) *float(p2)
                          #  lst_aux_result.append = list(map (lambda x, y: x*y, p1, p2))
                            lst_aux_result.append(base) 
                            print ("Producto : "+Nombre_Producto + " Precio : Q. "+ p1 + " Cantidad : " + p2)
                            #print ("resultados: "+lst_aux_result) #prueba de impresión
                        else: break 
                    print("....")    

        elif opc =="2":          
            txt_list_2 = []
            lists_2 = []
            txt_2 = cargarlfp()
            listinfo = [] # guarda nuestras instrucciones
            intro = [] #separar las instrucciones 

            
            if txt_2 is not None: # si no tenemos texto de la list
                if (len(txt_2) > 0):# recorremos
                    for s in txt_2: # recorremos nuestra info

                        if s == "\n": # quitamos saltos
                            pass
                        elif s == " ": # recorremos y quitamos espaciados
                            pass
                        else: # recorremos
                            listaux_2 = [ord(s), s]
                            txt_list_2.append(listaux_2)
                            lists_2.append(s)
                    for m in lists_2:
                        extra_2 = lists_2.index("¿")
                        if (m == "¿"): # a partir del signo ¿ cuenta
                            extralist= lists_2[extra_2+1: len(lists_2)-2]# agregamos menos 2 resta posición 0,1 
                            srt = "".join(extralist)
                            aux_2 = srt.split(",") #separamos nuestro arreglo, pos1, :, pos2
                            a = aux_2 # instruccinoes sin todo lo anterior, y para visualización

                   # print(a) #visualizamos

                    for e in a:
                        separar = "".join(e)
                        auxi_22 = separar.split(":") # identificamos el número de elementos en una linea
                        intro.append(auxi_22) 

                   # print("Separación de arreglo: ", intro )

                    for n in intro: # recorremos todo el texto
                        if ( (n[0] == "Nombre")and (len(n[1])>0)):
                            rep_2 = n[1] 
                            
                            print ("Nombre : ", rep_2)
                        elif ((n[0] == "Nombre") and (len(n[1])< 1)):
                            print( "he te saltaste el nombre, por favor vuelve a ingresarlo")
                            break
                        else:    
                            if ((n[0] == "Grafica") and (len(n[1])>0)):
                                V_grafica = n[1] # verificamos el dato seleccionado
                                print("Grafica: ", V_grafica) 
                                Grafica_Final= V_grafica.replace("\"", "")

                            elif ((n[0] == "Grafica")and (len(n[1]) <1 )):
                                print(" he te saltaste el tipo de Gráfica, por favor vuelve a intentarlo")
                                break
                            else:    
                                if ((n[0] == "Titulo") and (len(n[1])>0)):
                                    V_Titu = n[1] # verificamos el dato seleccionado
                                    Titulo_Final = V_Titu
                                    print("Titulo: ", V_Titu) 

                                elif ((n[0] == "Titulo")and (len(n[1]) <1 )):
                                    V_Titu = "Reporte de ventas"
                                    print(" he te saltaste el Titulo, tranqui eso si lo cubrimos :3")
                                
                                else:    
                                    if ((n[0] == "TituloX") and (len(n[1])>0)):
                                        V_TituX = n[1] # verificamos el dato seleccionado
                                        TituloX_Final =V_TituX
                                        print("TituloX: ", V_TituX) 

                                    elif ((n[0] == "TituloX")and (len(n[1]) <1 )):
                                        print(" he te saltaste el TituloX, tranqui eso si lo cubrimos :3")
                                        
                                    else:    
                                        if ((n[0] == "TituloY") and (len(n[1])>0)):
                                            V_TituY = n[1] # verificamos el dato seleccionado
                                            TituloY_Final = V_TituY
                                            print("TituloY: ", V_TituY) 

                                        elif ((n[0] == "TituloY")and (len(n[1]) <1 )):
                                            print(" he te saltaste el TituloY, tranqui eso si lo cubrimos :3")
                                                
                    print("listo..... ")
                else:
                    print("Vuelve a ingresar el texto, por favor") 

        elif opc =="3":
           

            plt.rcdefaults()
            figB, axB = plt.subplots() # barras
            figL, axL = plt.subplots() #Lineas
            figP, axP = plt.subplots() # pie
            

            #Grafica de Barras
            axB.bar(lst_aux_Pro, lst_aux_result)
            axB.set_xlabel(TituloX_Final) #Titulo de los ejes
            axB.set_ylabel(TituloY_Final)

            axB.grid(axis = "y", color="red")
            axL.set_title("Productos")

            #Grafica de Lineas
            #Titulos
            axL.plot(lst_aux_Pro, lst_aux_result)
            axL.set_xlabel(TituloX_Final, fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'blue'})
            axL.set_ylabel(TituloY_Final, fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'red'})
            #
            axL.grid(axis='y', color='darkgray', linestyle='dashed')
            axL.set_title(Titulo_Final)
            #Grafica de PIE
            axP.pie(lst_aux_result, labels=lst_aux_Pro )
            axP.set_xlabel(TituloX_Final, fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'blue'})
            axP.set_ylabel(TituloY_Final, fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'red'})
            #
            axP.grid(axis='y', color='darkgray', linestyle='dashed')
            axP.set_title(Titulo_Final)

            if Grafica_Final == "Barras":
                figB.savefig("./graficaBarras.png")
            elif Grafica_Final == "barras":
                figB.savefig("./graficaBarras.png")

            elif Grafica_Final == "Lineas":
                figL.savefig("./graficaLineas.png")
            elif Grafica_Final == "lineas":
                figL.savefig("./graficaLineas.png")

                
            elif Grafica_Final == "Pie":
                figP.savefig("./graficaPie.png")
            elif Grafica_Final == "pie":
                figP.savefig("./graficaPie.png")
                    
        elif opc =="5":
            cargar()
        elif opc =="4:":
            print("gracias por preferirnos")
            break          
        else:
            print(" no es una opción")