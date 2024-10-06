print ("Olá! Bem-vindo(a) ao nosso sistema. ")
print ("\n1 - Adicione um novo cliente \n2 - Verifique todos os clientes cadastrados \n3 - Busque um cliente pelo nome \n4 - Atualize informações do cliente \n5 - Exclua um cliente do sistema")
(opcao)=int (input("\nPor favor, escolha uma opção: "))

match (opcao):
    case 1: print ("Vamos adicionar um novo cliente!")

    case 2: print("Aqui estão todos os clientes cadastrados ")

    case 3: print ("Informe o nome do cliente para buscá-lo")

    case 4: print ("Vamos atualizar informações do cliente!")

    case 5: print ("Informe o nome do cliente para deletá-lo do sistema")

    case __: print ("Opção inválida")



