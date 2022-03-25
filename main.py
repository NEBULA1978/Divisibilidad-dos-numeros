"""
cree un programa que pieda por teclado dos numeros
de tres cifras y que muestre por pantalla true si el
primer numero y el segundo numero es divisible por el primer
digito del segundo numero,y el segundo numero es divisible para el primer digito del primer numero

"""

num1 =input("Ingrese numero1 de tres digitos: ")#"450"
num2 =input("Ingrese numero2 de tres digitos: ")#"312"
primerDig=num2[0]#3
residuo1 = int(num1) % int(primerDig)

primerDig2=num1[0] # "4"
residuo2= int(num2) % int(primerDig2) #1

cond= (residuo1 == 0) and (residuo2 == 0)
print("El resultado es: ", cond)
