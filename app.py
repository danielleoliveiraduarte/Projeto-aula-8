# Pesquisa de satisfação - TudoWeb

quantidade_excelente = 0
quantidade_ruim = 0

# Repete a pesquisa para 50 entrevistados
for entrevistado in range(1, 51):
	print(f"\n--- Entrevistado {entrevistado} ---")

	nome = input("Nome: ")
	idade = int(input("Idade: "))

	print("\nAvaliação do atendimento")
	print("1 - EXCELENTE")
	print("2 - BOM")
	print("3 - RUIM")

	opiniao = int(input("Digite sua opção: "))

	# Estrutura de decisão
	if opiniao == 1:
		quantidade_excelente += 1
	elif opiniao == 3:
		quantidade_ruim += 1

# O resultado só será exibido após os 50 entrevistados
print("\n===================================")
print("RESULTADO FINAL DA PESQUISA")
print("===================================")
print(f"Quantidade de respostas EXCELENTE: {quantidade_excelente}")
print(f"Quantidade de respostas RUIM: {quantidade_ruim}")