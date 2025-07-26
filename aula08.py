#Listas são elemntis que podem guardar mais de um valor ao mesmo tempo, elas podem ser do mesmo tipo ou com tipos diferentes

#Lista de Strings
itemMochila = ["caneta","carregador","garrafa","caderno"] 
#Lista de int's
quantidade = [3,5,6,7,8,9] 
#Lista mista
pessoa = ["Ingrid", 25, 1.51]

#Exibindo todos items das listas
print(itemMochila)
print(quantidade)
print(pessoa)

#Imprimindo apenas um item da lista, o itam esta na posição 2
print(itemMochila[2])

#alterando um valor da lista
itemMochila[2] = "copo"
print(itemMochila)

#Inserindo um novo valor na lista
itemMochila.append("lapis") #vai iniserir a string lápis ao final da lista
itemMochila.append(10) #ele vai inserir o número 10 ao final da lista
print(itemMochila)

#inserindo um novo item na lista com index
itemMochila.insert(1, "guarda-chuva") #vai inserir a string na posição 1
print(itemMochila)

#utilizanod valores da lista para uma soma
print(itemMochila[6]+8)

#remove um elemento da lista buscando diretamente o valor
itemMochila.remove("lapis")
print(itemMochila)

#remove por posição
itemMochila.pop(5)
print(itemMochila)

#saber o tamanho da minha lista uso o len()
#obs: ele retorna o TAMANHO/QAUNTIDADE e não as posições
print(len(itemMochila))
