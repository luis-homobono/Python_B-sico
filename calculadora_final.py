try:
    digito1 = float(input('Inserta un digito: '))
    digito2 = float(input('Inserta otro digito: '))
except ValueError:
    print("Debes ingresar un numero entero o decimal.")
else:
    print('¿Qué operacion quieres hacer?')
    print('1 -> Suma')
    print('2 -> Resta')
    print('3 -> Multiplicación')
    print('4 -> División')
    print('5 -> Salir')
    try:
        operacion = int(input('Ingresa tu operacion: '))
    except ValueError:
        print('Debes ingresar una operación valida')
    else:
        if operacion == 1:
            print(digito1 + digito2)
        elif operacion == 2:
            print(digito1 - digito2)
        elif operacion == 3:
            print(digito1 * digito2)
        elif operacion == 4:
            try:
                print(digito1 / digito2)
            except ZeroDivisionError:
                print("La división sobre 0 es indeterminada")
        elif operacion == 5:
            print("Hasta luego")
            exit()
        else:
            print('No existe esa operación')
        print("Gracias, Vuelve pronto")
