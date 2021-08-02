# Grupo dos Dino - Controle de acesso em Grandes Obras

# Para executar a simulação lógica basta rodar o código diretamente
# Para ativar os recursos de conexão da rede CAN basta remover os comentarios das seções indicadas

# Bibiliotecas da rede CAN 
#import can
#import canopen

import random
import time

# Definção do controlador CAN a ser usado
#bus = can.interface.Bus(channel='can1', bustype='socketcan_native')
#id = 0x123

class Sensor:
  
  # parâmetros para o sensor da porta

    def __init__(self):
        #Sem presença = False / Presença = True
        self.__estado = False


    def setEstado(self, estado):
        self.__estado = estado


    def getEstado(self):
        return self.__estado
        
class Motor:
   
   # parâmetros para os motores que abrem e fecham a porta

    def __init__(self):
        #Parado = False / Em funcionamento = True
        self.__estado = False
        
        #Fechado = False / Aberto = True
        self.__posicao = False


    def setEstado(self, estado):
        self.__estado = estado


    def getEstado(self):
        return self.__estado


    def setPosicao(self, posicao):
        self.__posicao = posicao


    def getPosicao(self):
        return self.__posicao

        
class Calendario:
    
    # definição do objeto calendario para referenciar os intervalos de tempo utilizados

    def __init__(self):
        self.__tempo_real = 0

    def getTempoReal(self):
        return self.__tempo_real

    def setTempoReal(self, tempoReal):
        self.__tempo_real = tempoReal

    def geraPessoa(self):
        return random.randint(1,5)



class Porta:
   
   # Parâmetros de operação da porta

    def __init__(self, calendario, motorEsquerdo, motorDireito, sensorEntrada, sensorSaida):
        self.calendario = calendario
        self.sensorPortaEntrada = sensorSaida
        self.sensorPortaSaida = sensorEntrada
        self.motorPortaEsquerda = motorEsquerdo
        self.motorPortaDireita = motorDireito
        
        #Fechada = False / Aberta = True
        self.__estadoPorta = False
        
        #segundos para cada etapa
        self.__tempoEsperaPorta = 5
        self.__tempoAberturaPorta = 3
        self.__tempoFechamentoPorta = 3
        

    def detectaPessoa(self):

        if self.sensorPortaEntrada.getEstado() == True or self.sensorPortaSaida.getEstado() == True:

            #Verificação porta esta fechada
            if self.__estadoPorta == False:
                self.abrePorta()

            #Verifica se chega outra pessoa  
            self.aguardaPorta()

            #setando os sensores
            if self.sensorPortaEntrada.getEstado() == True:
                self.sensorPortaEntrada.setEstado(False)

            if self.sensorPortaSaida.getEstado() == True:
                self.sensorPortaSaida.setEstado(False)
                
    def aguardaPorta(self):

        tempo = 0
        tempoExtra = 0
        
        #Avança o tempo com a porta aberta    
        print("%d segundos decorridos => VERIFICANDO PRESENÇA DE MAIS PESSOAS" % calendario.getTempoReal(), end = '')

#Definindo o conteudo das mensagens para a rede CAN

				#cont = ["%d segundos decorridos => VERIFICANDO PRESENÇA DE MAIS PESSOAS" % calendario.getTempoReal(), end = '']
				#msg = can.Message(arbitration_id = id,data=cont)  #Criando a mensagem que será enviada na rede
    		#bus.send(msg) #Enviando para a rede
    		#print("Mensagem enviada para a rede")

        time.sleep(1)
        print(".", end = '')        
        time.sleep(0.5)
        print(".", end = '')        
        time.sleep(0.5)
        print(".\n\n")
        time.sleep(1)

        #Gera a chegada de uma pessoa
        while tempo < self.__tempoEsperaPorta + tempoExtra:
            #Probabilidade de outra pessoa passar na porta no próximo segundo
            if random.randint(1,5) == 1:
                tempoExtra = tempo
                self.calendario.setTempoReal(calendario.getTempoReal() + tempo)
                
                print("%d segundos decorridos => ACESSO AUTORIZADO, PRATIQUE O DISTANCIAMENTO SOCIAL, OBRIGADO" % calendario.getTempoReal())
                print("%d segundos decorridos => VERIFICANDO PRESENÇA DE MAIS PESSOAS" % calendario.getTempoReal(), end = '')

#Definindo o conteudo das mensagens para a rede CAN

                #cont = ["%d segundos decorridos => ACESSO AUTORIZADO, PRATIQUE O DISTANCIAMENTO SOCIAL, OBRIGADO" % calendario.getTempoReal() "\n" "%d segundos decorridos => VERIFICANDO PRESENÇA DE MAIS PESSOAS" % calendario.getTempoReal(), end = '' ]
								#msg = can.Message(arbitration_id = id,data=cont)  #Criando a mensagem que será enviada na rede
    						#bus.send(msg) #Enviando para a rede
    						#print("Mensagem enviada para a rede")

                time.sleep(1)
                print(".", end = '')        
                time.sleep(0.5)
                print(".", end = '')        
                time.sleep(0.5)
                print(".\n\n")
                time.sleep(1)


            tempo += 1

        #Atualiza o tempo total decorrido
        self.calendario.setTempoReal(calendario.getTempoReal() + self.__tempoEsperaPorta)


    def verificaPessoa(self):
        
        #Verifica se ainda há pessoas na porta
        if self.sensorPortaEntrada.getEstado() == False and self.sensorPortaSaida.getEstado()  == False:

        #Verificação de portas fechadas
            if self.__estadoPorta == True:
                self.fechaPorta()
	
    def abrePorta(self):	
        
        #Verificação de portas fechadas

        if self.motorPortaEsquerda.getPosicao == False and self.motorPortaDireita.getPosicao == False:
            #motores da porta
            self.motorPortaEsquerda.setEstado(True)
            self.motorPortaDireita.setEstado(True)

        #Passar o tempo de abertura da porta
        print("%d segundos decorridos => ABRINDO PORTAS " % calendario.getTempoReal(), end = '')

#Definindo o conteudo das mensagens para a rede CAN

				#cont = ["%d segundos decorridos => ABRINDO PORTAS " % calendario.getTempoReal(), end = '']
				#msg = can.Message(arbitration_id = id,data=cont)  #Criando a mensagem que será enviada na rede
    		#bus.send(msg) #Enviando para a rede
    		#print("Mensagem enviada para a rede")

        time.sleep(1)
        print(".", end = '')        
        time.sleep(0.5)
        print(".", end = '')        
        time.sleep(0.5)
        print(".\n")
        time.sleep(1)
        self.calendario.setTempoReal(calendario.getTempoReal() + self.__tempoAberturaPorta)

        #Desliga motores e configura como porta aberta
        self.motorPortaEsquerda.setEstado(False)
        self.motorPortaDireita.setEstado(False)
        self.motorPortaEsquerda.setPosicao(True)
        self.motorPortaDireita.setPosicao(True)
        self.__estadoPorta = True
        print("%d segundos decorridos => ACESSO AUTORIZADO" % calendario.getTempoReal())
        print("%d segundos decorridos => SEJA BEM VINDO, USE ALCOOL GEL\n\n" % calendario.getTempoReal())

#Definindo o conteudo das mensagens para a rede CAN

				#cont = ["%d segundos decorridos => ACESSO AUTORIZADO" % calendario.getTempoReal() "\n" "%d segundos decorridos => SEJA BEM VINDO, USE ALCOOL GEL\n\n" % calendario.getTempoReal()]
				#msg = can.Message(arbitration_id = id,data=cont)  #Criando a mensagem que será enviada na rede
    		#bus.send(msg) #Enviando para a rede
    		#print("Mensagem enviada para a rede")
	
    def fechaPorta(self):
        
        # verificação de portas abertas

        if self.motorPortaEsquerda.getPosicao == True and self.motorPortaDireita.getPosicao == True:
            #motores da porta
            self.motorPortaEsquerda.setEstado(True)
            self.motorPortaDireita.setEstado(True)

        print("%d segundos decorridos => FECHANDO PORTAS " % calendario.getTempoReal(), end = '')

#Definindo o conteudo das mensagens para a rede CAN

				#cont = ["%d segundos decorridos => FECHANDO PORTAS " % calendario.getTempoReal(), end = '']
				#msg = can.Message(arbitration_id = id,data=cont)  #Criando a mensagem que será enviada na rede
    		#bus.send(msg) #Enviando para a rede
    		#print("Mensagem enviada para a rede")

        time.sleep(1)
        print(".", end = '')        
        time.sleep(0.5)
        print(".", end = '')        
        time.sleep(0.5)
        print(".\n")
        time.sleep(1)
        self.calendario.setTempoReal(calendario.getTempoReal() + self.__tempoFechamentoPorta)

        #Desliga motores, porta => aberta
        self.motorPortaEsquerda.setEstado(False)
        self.motorPortaDireita.setEstado(False)
        self.motorPortaEsquerda.setPosicao(False)
        self.motorPortaDireita.setPosicao(False)
        self.__estadoPorta = False
        print("%d segundos decorridos => PORTAS FECHADAS" % calendario.getTempoReal())
        print("%d segundos decorridos => HIGIENIZE SUAS MÃOS E CUIDE-SE, OBRIGADO E VOLTE SEMPRE\n\n" % calendario.getTempoReal())

#Definindo o conteudo das mensagens para a rede CAN

				#cont = ["%d segundos decorridos => PORTAS FECHADAS" % calendario.getTempoReal() "\n" "%d segundos decorridos => HIGIENIZE SUAS MÃOS E CUIDE-SE, OBRIGADO E VOLTE SEMPRE\n\n" % calendario.getTempoReal()]
        #msg = can.Message(arbitration_id = id,data=cont)  #Criando a mensagem que será enviada na rede
    		#bus.send(msg) #Enviando para a rede
    		#print("Mensagem enviada para a rede")
	
		
######## Rodando a simulação da lógica de funcionamento do sistema

if __name__ == '__main__':

    #Alocação dos componentes do sistema
    calendario = Calendario()
    sensor_entrada = Sensor()
    sensor_saida = Sensor()
    motor_esquerdo = Motor()
    motor_direito = Motor()
    porta = Porta(calendario, motor_esquerdo, motor_direito, sensor_entrada, sensor_saida)


    #Roda a simulação durante 100 segundos
    while calendario.getTempoReal() < 100:

        #Avança o tempo até a chegada de uma pessoa (entre 1 e 5 segundos)
        calendario.setTempoReal(calendario.getTempoReal() + calendario.geraPessoa())

        #Ativa o sensor de entrada/saída da porta para uma chegada aleatória
        sensor = random.randint(0,1)

        if sensor == 0:
            porta.sensorPortaEntrada.setEstado(True)

        else:
            porta.sensorPortaSaida.setEstado(True)

        porta.detectaPessoa()
        porta.verificaPessoa()


