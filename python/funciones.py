"""Claculadora"""

num1=int(input("Pon un numero: "))
num2=int(input("Pon otro numero: "))

operacion=input("Introduce la operacion ( + - * / ) : ")

match operacion:
    case "+":
        resultado= num1 + num2
    case "-":
        resultado= num1 - num2 
    case "*":
        resultado= num1 * num2 
    case "/":
        resultado= num1 / num2


print(f"El resultado de \n {num1} {operacion} {num2} = {resultado}")
