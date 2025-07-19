#Lista
pedido = ["hambúrguer", "refrigerante", "batata", "molho", "sorvete"]
#Troca de item
pedido[2] = "suco"
#Adciona dois items 
pedido.append("brownie")
pedido.append("milkshake")
#Inserindo um item na posição 1
pedido.insert(1, "Água")
#Mostrando a quantidade de items
print(len(pedido))
#Removendo item pelo nome
pedido.remove("milkshake")
#Removendo pela posição
pedido.pop(3)

print(pedido)