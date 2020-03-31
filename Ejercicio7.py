import time
import os
try:
    opcion=0
    provincias=[]
    confirmados=[]
    nuevos=[]
    while True:
        os.system ("cls")  
        print("Situación epidemiológica del coronavirus (COVID-19) en Castilla y León ")
        print ("Actualización diaria. Datos a ",time.strftime("%d/%m/%y"))
        print("\t1.- Dar de alta  Provincia y datos (confirmados y nuevos)")
        print("\t2.- Introduce una provincia para modificar sus datos(confirmados y nuevos) " )
        print("\t3.- Numero Total de casos Confirmados y Nuevos en la Comunidad ")
        print("\t4.- Listado de la situacion  general por provincias(confirmados y nuevos)")
        print("\t5.-Salir")
        opcion=int(input())

        def altas():
            print("Introduzca provincia a dar de alta:")
            provincias.append(input())
            print("Introduzca numero de nuevos casos positivos:")
            nuevos.append(input())
            print("Introduzca numero de casos confirmados:")
            confirmados.append(input())
        
        def modificar():
            print("Introduce nombre de la provincia a modificar:")
            nomprov=input()
            coinprov=provincias.index(nomprov)
            print(provincias[coinprov],",",confirmados[coinprov],",",nuevos[coinprov])
            print("¿Que desea modificar?")
            print("\t1.- Confirmados")
            print("\t2.- Nuevos")
            opcion=int(input())

            if opcion==1:
                print("Introduzca nuevos confirmados:")
                num=int(input())
                confirmados.remove(coinprov)
                confirmados.append(num)
            elif opcion==2:
                print("Introduzca nuevos casos:")
                num=int(input())
                nuevos.remove(coinprov)
                nuevos.append(num)
            else:
                print("Error...")

        def listadogeneral():
            print("Datos a ", time.strftime("%d/%m/%y"))
            print("Provincia | confirmados | nuevos ")
            for x in range(10):
                print(provincias[x],"|",confirmados[x],"|",nuevos[x])
        
    
        if opcion == 1:
            altas()
        elif opcion == 2:
            modificar()
        elif opcion == 3:
            print("Total de casos...")
            input("Pulse para continuar...")
        elif opcion == 4:
            listadogeneral()
        elif opcion == 5:
            exit
        else: 
            input("Error, vuelve a introducir opcion")

except ValueError:
    print("No pude convertir el dato a un entero.")
except Exception as e: # OJO SIEMPRE LA ULTIMA
    print("Ha ocurrido un error no previsto del tipo ", type(e).__name__ )



