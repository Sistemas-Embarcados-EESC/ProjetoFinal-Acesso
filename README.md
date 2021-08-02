
# Projeto Proposto - Controle de Acessos em Grandes Obras
Repositório voltado para desenvolvimento do projeto proposto para a disciplina de Sistemas Embarcados, 2021/1, do Curso de Engenharia Mecatrônica EESC-USP.

# Integrantes
Alex José Arantes\
Artur Magalhães\
Angela Alves \
Arthur Monte

*todos os integrantes participaram efetivamente da elaboração do trabalho e definição das premissas e requisitos utilizados.

# Motivação
A Valorização do ambiente, sofisticação aliada a tecnologia, acessibilidade a idosos e cadeirantes, eficiência energética em ambientes climatizados, conforto térmico e acústico a clientes e funcionários, integração com diversos controles de acesso e a consideração com o atual cenário mundial aliada aos cuidados inerentes à prevenção do Covid.

# Descrição do Projeto
Pretende-se implementar os componentes requisitados para este projeto (Beaglebone, comunicação CAN, controlador e motor) de forma a desenvolver uma porta de acesso à obras que seja acionada automaticamente ao identificar a presença de um usuário. 

![image](https://user-images.githubusercontent.com/86329504/127577392-621da455-ae77-4f92-adc5-c0075e5cf13d.png)

O funcionamento do sistema se dará através da utilização de sensores de proximidade (ultra sônico), de modo que o acionamento de dois motores será referente à abertura da porta. Caso a distância detectada volte à leitura inicial, ou seja, não exista usuário próximo, os motores serão acionados no sentido contrário, realizando o fechamento da porta.

A comunicação com a placa lógica será implementada seguindo critérios do protocolo CAN, através dele serão enviadas à rede CAN informações referentes ao estado de abertura da porta que possibilitam monitorar o sistema a partir de outro dispositivo conectado na rede. No mais, também será  registrado os momentos em que a porta atingirá sua abertura e fechamento, visando obter o período que a porta permaneceu aberta e sua frequência de abertura ao longo do tempo.


# Parâmetros de Funcionamento

O sistema deverá acionar os motores responsáveis pela abertura das portas quando detectada a presença de uma pessoa (gerando um sinal de entrada).

O sistema manterá as portas fechadas caso não haja detecção pelos sensores.

O sistema monitorará as leituras dos sensores constantemente.

Após uma variação de sinal entre uma distância maior que a pré-definida para uma menor, a porta deverá aguardar uma nova leitura de sinal durante um tempo pré-estabelecido.

Serão registrados os horários de acionamento dos motores e sentido de rotação.


![image](https://user-images.githubusercontent.com/86329504/127406284-50d9922a-ed76-4323-9e3e-c1f34bf78af2.png)

# Considerações e Validação dos Parâmetros

Por conta da situação atual decorrente da pandemia de Covid 19, que dificulta a interação presencial entre os alunos integrantes do grupo para a construção de um protótipo funcional e o acesso aos materiais fornecidos pela universidade, optamos por validar o funcionamento do projeto através de uma simulação da lógica contida no código base escrito em Python que seria utilizada para controlar os dispositivos.


![simulação_controle_de_acessos](https://user-images.githubusercontent.com/83198956/127705301-8f679736-6e7b-4b9c-9d11-5e8319891887.jpg)
