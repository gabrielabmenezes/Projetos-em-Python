acumulador=0
while True: 
    num = int (input("Informe um número positivo (0 - Sair)"))

    if num < 0:
       print ("Não é permitido números negativos!")
       continue 
    elif num == 0:
        break

    acumulador=acumulador + num
print ("A soma total: ", acumulador)
       
