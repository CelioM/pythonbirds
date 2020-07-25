def contador_caracteres(s):
    """ FUNÇÃO QUE CONTA OS CARACTERES
    Ex:
    >>> contador_caracteres('renzo')
    e:1
    n:1
    o:1
    r:1
    z:1
    >>> contador_caracteres('banana')
    a:3
    b:1
    n:2

    :param s:
    :return:
    """
    caracteres_ordenados = sorted(s)
    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}:{contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior}:{contagem}')


if __name__ == "__main__":
    contador_caracteres("renzo")
    print()
    contador_caracteres("banana")   
