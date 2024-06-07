
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
while True:
    numero_mes = int(input("Ingrese el numero del mes que desea saber: "))
    if numero_mes <= 0:
        print("Programa finalizado.")
        break
    if 1 <= numero_mes <= 12:
        print(f"El mes es: \n", meses[numero_mes - 1])
    else:
        print("Este numero no esta admitido por favor ingrese del 1 al 12.")
