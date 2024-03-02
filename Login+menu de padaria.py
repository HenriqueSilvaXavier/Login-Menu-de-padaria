from time import sleep
listaN=[]
listaS=[]
produtos=[]
R=False
lixeira=[]
while True:
	print("1-Cadastrar")
	print("2-Entrar")
	r=int(input(""))
	if r==1:
		if R==False:
			nome=""
		while nome in listaN or len(listaN)==0:
			nome=input("Digite seu nome: ")
			if nome in listaN:
				print("\033[31mO nome já está em uso.\033[m")
			elif nome not in listaN:
				listaN.append(nome)
				R=True
				break
		senha=input("Digite sua senha: ")
		listaS.append(senha)
	try:
		if r==2:
			nome2=input("Digite seu nome: ")
			senha2=input("Digite sua senha: ")
			i=listaN.index(nome2)
			while nome2==listaN[i] and senha2==listaS[i]:
				numeros=[1,2,3,4,5,6,7]
				print("Bem vindo à padaria Boa Massa!")
				sleep(1)
				print("1- Cadastrar produto")
				print("2- Alterar produto")
				print("3- Excluir produto")
				print("4- Total de itens cadastrados")
				print("5- Itens excluídos")
				print("6- Total de funcionários")
				print("7- Sair")
				r=int(input(""))
				informacoes=["ID", "nome", "lote", "quantidade", "preço", "validade"]
				if r==1:
					id=input("Digite o id do produto: ")
					nome=input("Digite o nome do produto: ")
					lote=input("Digite o lote do produto: ")
					qtd=int(input("Digite a quantidade do produto: "))
					preco=input("Digite o preço do produto: ")
					validade=input("Digite a data de validade do produto:")
					produtos.append([id, nome, lote, qtd, preco, validade])
				if r==2:
					c=1
					for n in produtos:
						print("{}- {}".format(c, n[1]))
						c=c+1
					r2=int(input(""))
					if r2>0 and r2<=len(produtos):
						c=1
						for n in produtos[r2-1]:
							print("{}- {}".format(c, n))
							c=c+1
						r3=int(input(""))
						if r3==1:
							produtos[r2-1][0]=input("Digite o id do produto: ")
						if r3==2:
							produtos[r2-1][1]=input("Digite o nome do produto: ")
						if r3==3:
							produtos[r2-1][2]=input("Digite o lote do produto: ")
						if r3==4:
							produtos[r2-1][3]=int(input("Digite a quantidade do produto: "))
						if r3==5:
							produtos[r2-1][4]=input("Digite o preço do produto: ")
						if r3==6:
							produtos[r2-1][5]=input("Digite a data de validade do produto:")
				if r==3:
				   c=1
				   for n in produtos:
					   print("{}- {}".format(c, n[1]))
					   c=c+1
				   r4=int(input(""))
				   if r4>0 and r4<=len(produtos):
				   		lixeira.append(produtos[r4-1])
				   		del produtos[r4-1]
				while r==4:
					c=1
					for n in produtos:
						print("{}- {}".format(c, n[1]))
						c = c + 1
					r2 = int(input(""))
					if r2 > 0 and r2 <= len(produtos):
						print("Digite 0 para sair.")
						c = 0
						for n in produtos[r2 - 1]:
							print("{}- {}".format(informacoes[c], n))
							c = c + 1
						r5 = int(input(""))
						if r5 == 0:
							break
				while r==5:
					c=1
					print("Digite 0 para sair.")
					for n in lixeira:
						print("{}- {}".format(c, n[1]))
						c=c+1
					r5=int(input(""))
					if r5==0:
						break
				while r==6:
					print("Digite 0 para sair.")
					for n in listaN:
						print(n)
					r5 = int(input(""))
					if r5 == 0:
						break
				if r==7:
					break
			else:
				print("\033[91mA senha está incorreta.\033[0m")
	except:
		print("\033[91mO usuário nao foi cadastrado.\033[0m")