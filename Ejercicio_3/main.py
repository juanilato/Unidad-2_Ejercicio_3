import funciones



if __name__ =="__main__":
    
    #escribir archivos con datos
    funciones.escribir_archivo()
    
    
    #crear matriz bidimensional    
    matriz = funciones.crear_Matriz()
    
    
    #leer archivo y colocar datos en matriz bidimensional
    matriz = funciones.carga_matriz_BD(matriz)
    
    #crea Menu
    menu1 = funciones.crear_menu()

    
    #muestra del Menú
    menu1.muestra()
    opcion = int(input("Ingrese opcion: "))
    cantidad = menu1.getCantidad() + 1
    while opcion != cantidad:
        if opcion == 1:
            funciones.mostrar_var_max(matriz)
            funciones.mostrar_var_min(matriz)
        elif opcion == 2:
            funciones.temp_prom_men(matriz)
        elif opcion == 3:
            funciones.listar_valores_xDia(matriz)
        else: 
            print("Ingreso opción incorrecta ")
            input(("Ingrese enter para para continuar"))
            
        menu1.muestra()
        opcion = int(input("Ingrese opcion: "))
