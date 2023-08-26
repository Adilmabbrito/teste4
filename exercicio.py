import os

carros =[]

class Carro:
    nome = ''
    pot = 0
    velMax=0
    ligado=False


    def __init__(self, nome, pot):
        self.nome=nome
        self.pot=pot
        self.velMax = int(pot)*2
        self.ligado=False

    def ligar(self):
        self.ligado= True

    def desligar(self):
        self.desligar = False

    def info(self):
        print('**********************************')
        print('Nome ....:' + self.nome)
        print('Potência....:' + str(self.pot))
        print('Velocidade máxima....: ' + str(self.velMax))
        print('Ligado ....: ' + ('sim' if self.ligado == True else 'Não'))


def Menu():
    os.system('cls') or None
    print('1 - Novo carro')
    print('2- Informações do carro' )
    print('3 - Excluir carro')
    print('4- Ligar carro')
    print('5- Desligar carro')
    print('6 - Listar carro')
    print('7- Sair')
    print('Quantidade de carros' + str(len(carros)))
    opc=input('Digite uma opção: ')
    return opc
def NovoCarro():
    os.system('cls') or None
    n = input('Nome do carro: ')
    p= input('Potência do carro: ')
    car= Carro(n,p)

    carros.append(car)
    print('Novo carro criado')
    os.system('pause')

def informacoes():
    os.system('cls') or None
    n = input('Informe o número do carro que deseja informações: ')

    try: 
        carros[int(n)].info()
    
    except:
        print('Carro não existe na lista!')
    os.system('pause')

def excluiCarro():
   

    def informacoes():
        os.system('cls') or None
        n = input('Informe o número do carro que deseja excluir: ')

    try: 
        carros[int(n)].info()
    
    except:
        print('Carro não existe na lista')
              
    os.system('pause')

def ligarCarro():
    os.system('cls') or None
    n= input('Informe o carro que deseja ligar')
    try:
       carros[int(n)].ligar
       print('carro ligado')
    except:
        print('carro não existe na lista')
    os.system('pause')

def DesligarCarro():
    os.system('cls') or None
    n= input('Informe o carro que deseja desligar')
    try:
       carros[int(n)].desligar
       print('carro desligado')
    except:
        print('carro não existe na lista')
    os.system('pause')

    def listarCarro():
        os.system('cls') or None
        p=0
        for c in carros:
            print(str(p) + '-' + c.nome)
            p=p+1
    
    os.system('pause')

