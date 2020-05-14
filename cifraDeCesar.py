import requests

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
mensagem = str(input('Mensagem: ')).lower()
rot = int(input("Rotação Posiçao: "))

def criptografar(mensagem):
    m = ''

    for i in mensagem:
        if i in alfabeto:
            i_index = alfabeto.index(i)
            m += alfabeto[(i_index +  rot) % len(alfabeto)]
        else:
            m += i
    return m

def decriptografar(mensagem):
    m = ''

    for i in mensagem:
        if i in alfabeto:
            i_index = alfabeto.index(i)
            m += alfabeto[(i_index - rot) % len(alfabeto)]
        else:
            m += i
    return m

print(decriptografar(mensagem))

