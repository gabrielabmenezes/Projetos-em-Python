banho = tosa = banhotosa = outro = 0


def menu ():
    print ("1 - banho")
    print ("2 - tosa")
    print ("3 - banho e tosa")
    print ("4 - outros")
global op
op = int (input("Informe o serviço desejado: "))


for x in range (5):
    menu ()
    match (op):
     
        case 1: 
            banho+=1
    
        case 2: 
            tosa+=1

        case 3:
            banhotosa+=1
        
        case 4:
            outro+=1

print ("Quantidades: ")
print ("Banho: ", banho)
print ("Tosa: ", tosa)
print ("Banho e tosa: ", banhotosa)
print ("Outros: ", outro)


