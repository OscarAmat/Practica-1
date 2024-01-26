number1 = int(input("Ingresar primer numero "))
number2 = int(input("Ingresar segundo numero "))
print("elegir una opcion \n1) Mostrar una suma de los dos números\n2) Mostrar una resta de los dos números\n3) Mostrar una multiplicación de los dos números")

opcion = int(input("Ingrese la opcion "))

if opcion==1:
    print(number1+number2)
elif opcion==2:
    print(number1-number2)
elif opcion==3:
    print(number1*number2)
else:
    print("No es correcto")