temperatura = int(input("Informe a temperatura: "))

if (temperatura>=25 and temperatura<=30):
    print("O clima está agradável!")

elif (temperatura>=31 and temperatura<=35):
    print ("O clima está quente! Beba água!")

elif (temperatura>=36):
    print ("Calor intenso! Busque ambientes refrigerados e evite atividades ao ar livre!")

else:
    print ("O clima está frio!")

