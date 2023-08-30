num1= int(input("Ingresa un numero:"))
num2= int(input("Ingresa otro numero"))

eleccion = 0

while eleccion != 6:
    print("""
        Indique la operacion a realizar)
    1)Suma
    2)Resta
    3)Multiplicacion
    4)Division
    5)Cambio de valores
    6)Salir  
    """)

    eleccion = int(input())

    if eleccion == 1:
        print(" ")
        print("Resultado: ", num1, "+", num2,"=", num1 + num2)  

    if eleccion == 2:
        print(" ")
        print("Resultado: ", num1, "-", num2,"=", num1 - num2 )

    if eleccion == 3:
        print(" ")
        print("Resultado: ", num1 , "*", num2, "=", num1 * num2)

    if eleccion == 4:
        print(" ")
        print("Resultado: ", num1 , "/", num2, "/", num1 / num2)

    if eleccion == 5 :
        num1= int(input("Ingresa un numero:"))
        num2= int(input("Ingresa otro numero"))

    if eleccion == 6:
        print("Gracias por usar la calculadora. Creada por: Miguel Nieto")
        
