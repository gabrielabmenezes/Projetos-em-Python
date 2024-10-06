salario_fixo=float(input("Informe o seu salário fixo: "))
quant_carros=int(input("Informe a quantidade de carros que você vendeu: "))
total_vendas=float(input("Informe o valor total das vendas: "))
comissao_carro=int(input("Informe o percentual da sua comissão: "))

comissao=(comissao_carro/100)*(total_vendas/quant_carros)
totalvendas=total_vendas*0.05

print ("O seu salário total é: ", float(salario_fixo+comissao+totalvendas))
