
# Projeto Proposto - Controle de Acessos em Grandes Obras
Repositório voltado para desenvolvimento do projeto proposto para a disciplina de Sistemas Embarcados, 2021/1, do Curso de Engenharia Mecatrônica EESC-USP.

# Integrantes
Alex José Arantes			NºUSP 9806791\
Artur Magalhães				NºUSP 9051612\
Angela Alves					NºUSP 9850311\
Arthur Monte					NºUSP 9805612

*todos os integrantes participaram efetivamente da elaboração do trabalho e definição das premissas e requisitos utilizados.


# Descrição do Projeto
Pretende-se implementar os componentes requisitados para este projeto (Beaglebone, comunicação CAN, sensor e motor) de forma a desenvolver uma porta de acesso à obras que seja acionada automaticamente ao identificar a presença de um usuário, e, que alerte sobre os cuidados sanitários caso haja mais de um usuário na entrada, promovendo assim um controle dos acessos de modo que aglomerações sejam evitadas sem sacrificar a agilidade na entrada e saída de clientes e funcionários.

![image](https://user-images.githubusercontent.com/86329504/127577392-621da455-ae77-4f92-adc5-c0075e5cf13d.png)

O funcionamento do sistema se dará através da utilização de sensores de proximidade (ultra sônico) e o acionamento de dois motores será referente à abertura da porta. Caso a distância detectada volte à leitura inicial, ou seja, não exista usuário próximo, os motores serão acionados no sentido contrário, realizando o fechamento da porta.

A comunicação com a placa lógica será implementada seguindo critérios do protocolo CAN, através dele serão enviadas à rede CAN informações referentes ao estado de abertura da porta, o que possibilita monitorar o sistema a partir de outro dispositivo conectado na rede. No mais, também serão registrados os momentos em que a porta atingirá sua abertura e fechamento, visando obter o período que a porta permaneceu aberta e sua frequência de abertura ao longo do tempo.


![Diagrama de rede simples](https://user-images.githubusercontent.com/83198956/127915540-0deab4db-77e0-4373-bfaa-65ade2738867.png)


# Parâmetros de Funcionamento

O sistema deverá acionar os motores responsáveis pela abertura das portas quando detectada a presença de uma pessoa (gerando um sinal de entrada).

O sistema manterá as portas fechadas caso não haja detecção pelos sensores.

O sistema monitorará as leituras dos sensores constantemente.

Após uma variação de sinal entre uma distância maior que a pré-definida para uma menor, a porta deverá aguardar uma nova leitura de sinal durante um tempo pré-estabelecido.

Serão registrados os horários de acionamento dos motores e sentido de rotação.


![image](https://user-images.githubusercontent.com/86329504/127406284-50d9922a-ed76-4323-9e3e-c1f34bf78af2.png)

# Considerações e Validação dos Parâmetros

Por conta da situação atual decorrente da pandemia de Covid 19, que dificulta a interação presencial entre os alunos integrantes do grupo para a construção de um protótipo funcional e o acesso aos materiais fornecidos pela universidade, optamos por validar o funcionamento do projeto através de uma simulação da lógica contida no código base escrito em Python (https://github.com/Sistemas-Embarcados-EESC/ProjetoFinal-Acesso/blob/main/Controle_de_acesso.py) que seria utilizada para controlar os dispositivos.

Para executar a configuração e ativação da rede CAN basta seguir o arquivo Instruções (https://github.com/Sistemas-Embarcados-EESC/ProjetoFinal-Acesso/blob/main/Instru%C3%A7%C3%B5es)

![simulação_controle_de_acessos](https://user-images.githubusercontent.com/83198956/127705301-8f679736-6e7b-4b9c-9d11-5e8319891887.jpg)

# Conclusão

A Valorização do ambiente, sofisticação aliada a tecnologia, acessibilidade a idosos e cadeirantes, eficiência energética em ambientes climatizados, conforto térmico e acústico a clientes e funcionários, integração com diversos sistemas de controle e a consideração com o atual cenário mundial aliada aos cuidados inerentes à prevenção do Covid têm se provado aspectos essenciais a serem considerados em projetos que buscam trazer diferenciação e inovação em diversos setores. Através da utilização de sistemas embarcados é possível implementar soluções inteligentes que, além de contemplar os aspectos mencionados, agregam imenso valor a empresas e consumidores na forma de agilidade e produtividade de tal forma que, após uma completa integração na dinâmica de trabalho, esses sistemas chegam a serem vistos como indispensáveis para atender o mercado atual.

