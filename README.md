# Projeto
Repositório voltado para desenvolvimento do projeto de Sistemas Embarcados, 2021/1, do Curso de Engenharia Mecatrônica EESC-USP.


# Motivação
A Valorização do ambiente, sofisticação aliada a tecnologia, acessibilidade a idosos e cadeirantes, eficiência energética em ambientes climatizados, conforto térmico e acústico a clientes e funcionários, integração com diversos controles de acesso e a consideração com o atual cenário mundial aliada aos cuidados inerentes à prevenção do Covid.

# Descrição
Pretende-se implementar componentes pré requisitados neste projeto (Beaglebone, comunicação CAN, controlador e motor) de forma a desenvolver uma porta de acesso à obras que seja acionada de forma automatica ao identificar a presença de um usuário.

Seu funcionamento será pautado com a utilização de sensores de proximidade (ultra sônico), de modo que movimento um determinado motor que simulará a abertura da porta. Caso a distância detectada volte à leitura inicial, o motor irá rotacionar em sentido contrário, simulando o fechamento da porta.

Toda a comunicação do motor com a placa lógica será implementada seguindo critérios do protocolo CAN, bem como o envio do sinal do sensor para a placa. No mais, também será  registrado os momentos em que a porta atingirá sua abertura e fechamento. Dadas as informações, pode-se obter o período que a porta permaneceu aberta e sua frequência de abertura ao longo do tempo.
# Integrantes
Alex José Arantes\
Artur Maglhães\
Angela Alves \
Arthur Monte


# Requisitos funcionais
O sistema manterá as portas fechadas até que os sensores acusem a presença de um usuário.

Uma vez detectada a presença de uma pessoa (gerando um sinal de entrada), o sistema deverá acionar os motores responsáveis pela abertura das portas.

O sistema monitorará as leituras dos sensores constantemente.

Após uma variação de sinal entre uma distância maior que a pré-definida para uma menor, a porta deverá permanecer em repouso durante um tempo pré-estabelecido.

Área de leitura dos sensores devem preencher totalmente a área de travessia dos usuários.

Registrar os horários de acionamento dos motores e sentido de rotação.

# Requisitos não funcionais
O sensor deve detectar corretamente a presença de 95% das vezes em menos de 3 segundos.

O sistema fechará as portas após um intervalo de tempo, sem mudança no sinal do sensor.

# Como faremos para contemplar os requisitos
O sistema fará constante leitura dos sensores para garantir a correta detecção de pessoas, e consequentemente o devido acionamento dos motores para abertura da porta, e também fechá-la conforme as condições especificadas;

Para cumprir as especificações de desempenho mostradas (tempo de resposta e recorrência de falhas), a porta contará com mecanismo de fácil movimentação, oferencendo a menor restencia possível, dentro de um bom custo benefício. Além disso, utilizaremos motores que forneçam uma resposta adequada ao comportamento desejado.

A grande maioria das portas automáticas comerciais têm mecanismo composto por motor, atuador e correia dentada para transmissão do movimento. O grupo realizaria a confecção do protótipo seguindo a mesma ideia, uma vez se trata de uma solução barata e eficiente para o sistema.

# Simulação
Dada a situação de Pandamia do Covid-19, e as necessidades de afastamento de alunos e professores, a construção física do projeto não poderá ser realizada, limitando-se a simulações. Desenvolveu-se uma aplicação em Python simulando o cenário de controle e automação das portas.
