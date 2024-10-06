salario_fixo=float(input("Informe o seu salário fixo: "))
total_vendas=float(input("Informe o valor total das vendas: "))
comissao=int(input("Informe o percentual da sua comissão: "))

comissao=(comissao/100)*(total_vendas)


print ("O seu salário total é: ", float(salario_fixo+comissao))
