class Pessoa:
    olhos = 2 #atributo de classe, para economizar memória (podem ser dos tipo:lista, dict, string,etc)
    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Ola{id( self)}'
    @staticmethod
    def metodo_estatico(): #o metodo de classe não precisa de parametro como a função da classe
        return 42
    @classmethod #está ligado à classe, logo pode se acessar esta e as atribuições usando o 'cls'
    def nome_e_atribuição(cls):
        return f'{cls} - {cls.olhos}'
if __name__ == '__main__':
    renzo = Pessoa(nome="renzo")
    luciano = Pessoa(renzo, nome = "Luciano")
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = "Ramalho"
    del luciano.filhos
    luciano.olhos = 1 #o atributo dinamico vai inserir um novo valor para o de classe no objeto 'luciano',
    #- porém vai fazer esse atributo ocupar um novo espaço na memória

    del luciano.olhos # apaga o atributo do objeto 'luciano', não da classe 'Pessoa', logo ele não tem-
    #-atributo de instancia(criado como dinamico) no dunder dict de 'luciano'

    Pessoa.olhos = 3 # muda o valor do atributo para objetos da classe
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos) #é possivel acessar atributos de classe através dos objetos
    print(renzo.olhos)
    print(id(Pessoa.olhos),id(renzo.olhos),id(luciano.olhos))
    #o endereço é o mesmo para o atributo da classe
    #o dunder dict não mostra os atributos de classe, apenas os de instância
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico()) # tanto acessando pelo objeto quanto pela classe
    #retorna o mesmo valor pelo @staticmethod
    print(Pessoa.nome_e_atribuição(),luciano.nome_e_atribuição()) # pode ser acessado pela classe quanto
    # pelo objeto da classe e acessar suas atribuições
    # os metodos e atributos de classe devem ser separados dos de instância