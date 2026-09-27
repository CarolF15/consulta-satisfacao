# Projeto de Consulta de satifação

# Declaração de variáveis
nota_excelente = 0
nota_ruim = 0

# Estrutura de Repetição e coleta de dados
for x in range (50):
    print("\n-----------")
    print(f"Pesquisa {x + 1}")
    print("-----------")
    
    nome_cliente = input ("Seu nome: ")
    idade_cliente = int (input ("Sua idade: "))
    opiniao_cliente = input ("Seu grau de satisfação com o serviço (Excelente, Bom, Ruim): ")



    if opiniao_cliente == "Excelente" or opiniao_cliente == "excelente":
        nota_excelente += 1

    elif opiniao_cliente == "Ruim" or opiniao_cliente == "ruim":
        nota_ruim += 1

# Apresentação dos Resultados
print("\n----------------------")
print("\nResultado da pesquisa")
print("\nClassificaram como Excelente: ", nota_excelente)
print("Classificaram como Ruim: ", nota_ruim)