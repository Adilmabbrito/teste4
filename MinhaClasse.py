class MinhaClasse:
    def __init__(self, velMax, ligado, cor):
        self.velMax = velMax
        self.ligado = ligado
        self.cor = cor



    def mostrar(self):
        print('Velocidade máxima: '+ str(self.velMax))  
        print('Cor .......................' + self.cor )
        estado = 'sim' if self.ligado else 'N' 
        print('Ligado .......................' + estado)   
        print('--------------------------------------')

        c1 = MinhaClasse (200, False, 'Preto')
        c2 = MinhaClasse(120, False, 'branco')

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado= False
    
    def andar(self):
        if (self.ligado):
            print('andando')
        else:
            print('carro desligado')



c1= MinhaClasse(200, False, 'preto')
c2= MinhaClasse(120, False, 'vermelho')
c3= MinhaClasse(350, False, 'branco')
c1.ligar()
c1.mostrar()
c2.mostrar()
c3.mostrar()

c1.andar()
c2.andar()

c2.ligar()
c2.andar()


        