#Trabalhando com multiplas listas
from itertools import zip_longest

a_lista = ['A','B','C','D','E']
b_lista = [1,2,3,4,6]

for a,b in zip(a_lista, b_lista):
    print(a)
    print(b)


#cenários perfeitos
produtos = ['produto 1','produto 2','produto 3','produto 4','produto 5',]
precos = [250,150,220,550,50]
for a,b in zip(produtos, precos):
    print(f'salvando produto {a} valor R$ {b}')

titulos = ['Titulo 1','Titulo 2','Titulo 3','Titulo 4']
descricoes = ['Descrição 1', 'Descrição 2','Descrição 3']
for titulo, descricao in zip_longest(titulos, descricoes):
    print(f'Encontramos p {titulo} descrição: {descricao}')

#Desafio 1
##Estamos extraindo preços de um site de produtos e queremos armazenar as informações encontradas, porem a pesquisa foi
##encontrada em momentos diferentes, assim acabamos com duas listas diferentes, favor criar uma mensagem que diz o nome e valor do
##produto, como as mensagens abaixo:

produtos = ['produto 1','produto 2','produto 3','produto 4','produto 5',]
precos = ['R$500,00','R$1500,00','R$2700,00','R$5000,00']
for produto,preco in zip_longest(produtos, precos):
    print(f'Produto: {produto} encontrado no valor R$ {preco}')