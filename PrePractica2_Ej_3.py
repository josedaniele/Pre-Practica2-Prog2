#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
try:  
    division = a/b
except ZeroDivisionError as exception:
    print(f"Ha ocurrido un error {exception}")
else:
    print("El resultado es ", division)
finally:
    print("Proceso finalizado")
#FIN