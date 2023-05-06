import csv
import random
from clase_registro import Registro 
from clase_menu import Menu

#Escribe en un archivo csv los datos: dia temperatura humedad y presión, 
#Generando valores random para todos los datos, menos el dato dia, que es secuencial
def escribir_archivo():
    with open('datos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['dia','hora','temperatura','humedad','presión'])
        for i in range(30):
            for j in range(24):
                random_temperature = random.randint(0, 30)
                random_pressure = random.uniform(0.8,1)
                random_humidity = random.randint(40, 60)
                writer.writerow([int(i+1), int(j), int(random_temperature), int(random_humidity), float(random_pressure)])

#crear matriz bidimensional 
def crear_Matriz():
    matriz = []
    for i in range(0,30):
        matriz.append([]) 
        for j in range(0,24):
            matriz[i].append([]) 
    return matriz

#carga Matriz Bidimensional
def carga_matriz_BD(matriz):
    archivo = open("datos.csv")
    reader = csv.reader(archivo, delimiter =",")
    bandera = True
    for fila in reader:
        if bandera:
            bandera = not bandera
        else:
            dato = Registro(int(fila[2]),int(fila [3]),float(fila [4]))
            matriz[int(fila[0])-1][int(fila [1])].append(dato)
    archivo.close()
    return matriz

#crear Menu   
def crear_menu():
    #cantidad de opciones
    cantidad = 3
    menu1 = Menu(cantidad)
    #Opciones del menú
    opciones = ["Mostrar para cada variable el día y hora de menor y mayor valor","Indicar la temperatura promedio mensual por cada hora."," Dado un número de día listar los valores de las tres variables para cada hora del día dado."]
    menu1.IngresaOpcion(opciones)
    return menu1

#opcion 1, mostrar para cada variable del día y hora de menor y mayor valor

#define los maximos por día y los muestra
def mostrar_var_max(matriz):
    print("Máximos \n")
    for i in range(len(matriz)):
        max_temperatura = -1
        max_presion = -1
        max_humedad = -1
        for j in range(len(matriz[i])):
            for obj in matriz[i][j]:
                
                
                if obj.get_temperatura() > max_temperatura:
                    max_temperatura = obj.get_temperatura()
                    j_temp_max = j
                
                if obj.get_presion() > max_presion:
                    max_presion = obj.get_presion()
                    j_pre_max = j
                    
                if obj.get_humedad() > max_humedad:
                    max_humedad = obj.get_humedad()
                    j_hum_max = j             
        print(f"Día {i+1} \nTemperatura: ", j_temp_max, " Humedad: ",j_hum_max, " Presion: ",j_pre_max)


#define los mínimos por día y los muestra
def mostrar_var_min(matriz):
    print("Mínimos \n")
    for i in range(len(matriz)):
        min_temperatura = 100
        min_presion = 100
        min_humedad = 100
        for j in range(len(matriz[i])):
            for obj in matriz[i][j]:
                
                
                if obj.get_temperatura() < min_temperatura:
                    min_temperatura = obj.get_temperatura()
                    j_temp_min = j
                
                if obj.get_presion() < min_presion:
                    min_presion = obj.get_presion()
                    j_pre_min = j
                    
                if obj.get_humedad() < min_humedad:
                    min_humedad = obj.get_humedad()
                    j_hum_min = j 
        print(f"Día {i+1} \nTemperatura:", j_temp_min, " Humedad: ",j_hum_min, "Presion: ",j_pre_min)





#opción 2 Indicar la temperatura promedio mensual por cada hora.
#lee por hora de cada mes, los suma y los divide en el total, generando un promedio          
def temp_prom_men(matriz):
    for j in range(0,24):
        sum_temp = 0
        contador = 0
        for i in range(0,30):
            for obj in matriz [i][j]:
                contador += 1
                sum_temp += obj.get_temperatura()
        print(f"Temperatura promedio mensual de hora: {j}", sum_temp/(i + 1))
        
        
        
#opción 3 Dado un número de día listar los valores de las tres variables para cada hora del día dado.        
#Dado un número de día listar los valores de las tres variables para cada hora del día dado.            
def listar_valores_xDia(matriz):
    dia = int(input("ingrese día a listar"))
    print("Hora     Temperatura     Humedad     Presion \n")
    for j in range(len(matriz[dia-1])):
        for obj in matriz[dia-1][j]:
            print(f"{j}        ",obj.get_temperatura(), "            ", obj.get_humedad(), "          ", obj.get_presion())