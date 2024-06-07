lista=[]
for n in range(1,6):
    numero=int(input(f"Ponga el numero {n} : "))
    lista.append(numero)
    suma=sum(lista)
    promedio=suma / len(lista)
    num_mayor=max(lista)
    num_menor=min(lista)
    
print(f"El numero mayor es: \n{num_mayor}\nEl numero menor es: \n {num_menor}\nLa suma de estos valores {len(lista)} es:{suma}\nEl promedio de esta suma {suma} es: {promedio} ")




