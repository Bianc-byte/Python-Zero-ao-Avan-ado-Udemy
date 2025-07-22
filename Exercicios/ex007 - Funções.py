"""
crie uma função que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
"""
number = 1

def funcao_duplica(number):
    print(number * 2)

#posso usar return no lugar de print tbm

def funcao_triplica(number):
    print(number * 3)

def funcao_quadriplica(number):
    print(number * 4)

"""
ou posso também criar uma função dentro de outra funçao
exemplo:
def criar_multiplicar(numero):
    def multiplocar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadripliucar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))

"""
funcao_duplica(number)
funcao_triplica(number)
funcao_quadriplica(number)