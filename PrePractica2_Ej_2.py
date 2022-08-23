#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO
lista = []
listaImpar = []
for i in range(3) :
    valor=int(input("Ingrese un numero: "))
    lista.append(valor)
    if valor%2 != 0:
     listaImpar.append(valor)  

print("La lista entera tiene los siguientes valores :",lista)
print("Los valores impares son :",listaImpar)   
#FIN