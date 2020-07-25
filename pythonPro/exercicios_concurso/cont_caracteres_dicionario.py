def contador_caracteres(s):
    """ FUNÇÃO QUE CONTA OS CARACTERES
    Ex:
    >>> contador_caracteres('renzo')
    {'e':1, 'n':1, 'o':1, 'r':1, 'z':1}
    >>> contador_caracteres('banana')
    {'a':3, 'b':1, 'n':2}

    :param s:
    :return:
    """

    resultado = {}
    for caracter in s:
        contagem = resultado.get(caracter, 0)
        contagem+=1
        resultado[caracter] = contagem
    return resultado


if __name__ == "__main__":
    print(contador_caracteres("renzo"))
    print()
    print(contador_caracteres("banana"))
