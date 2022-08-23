#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
lista=[]
a= int(input("Ingrese el valor de a "))
lista.append(a)
b= int(input("Ingrese el valor de b "))
lista.append(b)
max_value = max(lista)
print("El maximo valor es :" ,max_value)

if lista[0]> lista[1] :
    max_value =lista[0]
else:
    max_value= lista[1]

print("El maximo valor es :" ,max_value)
#FIN