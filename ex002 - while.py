"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""


##exercicio


name = 'Luiz Otávio'
indice = 0
new_name = ""

while indice < len(name):
    letra = name[indice]
    if indice == len(name) - 1:
        new_name += letra 
    else:
        new_name += letra + "*"
    indice += 1
print(new_name)