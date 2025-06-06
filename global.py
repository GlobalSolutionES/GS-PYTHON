'''
Geovana Maria da Silva Cardoso - 566254
Mariana Silva do Egito Moreira - 562544
1ESPF - Equipe HydroSafe
'''

#Guia de Sobrevivência
#Função para que o usuário seja informado do que fazer para Prevenir uma enchente ou de como proceder quando
# estiver em uma situação ANTES, DURANTE, (durante) DENTRO DO CARRO ou APÓS uma enchente
def guiasobre(): 
    while True:
        print("\n-- GUIA DE SOBREVIVÊNCIA --")
        print("1 - Prevenção")
        print("2 - Antes da Enchente")
        print("3 - Durante a Enchente")
        print("4 - No carro")
        print("5 - Após a Enchente")
        print("0 - Voltar ao menu principal")

        escolha = input("Escolha a opção que deseja visualizar: ")

        if escolha == "1":
            prevencao()
        elif escolha == "2":
            antes()
        elif escolha == "3":
            durante()
        elif escolha == "4":
            nocarro()
        elif escolha == "5":
            depois()
        elif escolha == "0":
            break
        else:
            print("Opcão inválida. Tente novamente, por favor.")


#Função feita para que o usuário tenha a opção de ver outra seção do Guia de sobrevivência ou sair dessa função e voltar 
#ao Menu principal
def voltarVerOpcao():
    while True:
        print("\nDeseja: ")
        print("1 - Ver outra seção do guia")
        print("0 - Voltar ao menu principal")
        escolha = input("Digite sua escolha: ")
            
        if escolha == "1":
            return True
        elif escolha == "0":
            return False
        else:
            print("Entrada inválida. Tente novamente, por favor.")


#Funções do Guia de Sobrevivência
#Possuem instruções do que fazer em cada situação envolvendo Enchentes.

#Para ajudar a população a reduzir riscos antes que o desastre aconteça
def prevencao():
    print("\n-- PREVENÇÃO CONTRA ENCHENTES --")
    print("1. Moradores de regiões propensas a inundações devem manter-se informados sobre as condições meteorológicas;")
    print("2. Evite construir em cima e embaixo de barrancos que possam deslizar, carregando sua casa;")
    print("3. Não jogue lixo ou entulho no córrego, para não obstruir a passagem de água, nem em terrenos baldios ou ruas;")
    print("4. Limpe o telhado, calhas, condutores e canaletas para evitar entupimentos.")
    print("\n")
    if voltarVerOpcao(): #A função será executada, se o usuário inserir 1 (função verdadeira), executará o Guia novamente
        guiasobre()

#Para ensinar ações fundamentais que reduzem danos e protegem vidas e bens materiais antes da enchente começar.
def antes():
    print("\n--- ANTES DA ENCHENTE ---")
    print("1. Tenha um lugar previsto, seguro, onde você e sua família possam se alojar no caso de inundação;")
    print("2. Ao primeiro sinal de chuva forte, coloque os móveis, eletrodomésticos e demais objetos em lugares altos;")
    print("3.Coloque documentos e objetos de valor em sacos plásticos bem fechados e em local protegido;")
    print("4. Feche as portas, janelas e o registro de entrada de água;")
    print("5. Desligue aparelhos elétricos e eletrônicos, a chave geral de sua casa e feche os registros de entrada de água e de gás;")
    print("6. Retire todo o lixo e leve-o para áreas não sujeitas a inundações;")
    print("7. Retire os animais de estimação de casa;")
    print("8. Seja solidário: avise seus vizinhos sobre o perigo, no caso de casas construídas em áreas de risco de deslizamentos; avise também, imediatamente,o Corpo de Bombeiros (193) e à Defesa Civil (199);")
    print("\n")
    if voltarVerOpcao():
        guiasobre()
    
#Para ajudar a evitar acidentes, doenças e perda de vidas no momento mais crítico do desastre.    
def durante():
    print("\n--- DURANTE A ENCHENTE ---")
    print("1. Proteja a sua vida, a de seus familiares e amigos. Evite contato com as águas de enchentes, elas estão contaminadas e podem provocar doenças;")
    print("2. Se estiver em local seguro, procure não se deslocar; não atravesse ruas alagadas, pois você pode ser arrastado pela água;")
    print("3. Em local alagado, preste atenção a buracos e bueiros sem tampas ou encobertos pela água;")
    print("4. Em caso de ventos muito fortes, cuidado com as quedas de árvores, fios, postes, semáforos, etc;")
    print("5. Utilize calçado, calça comprida e blusa para a proteção do corpo; não use bermuda e não fique sem camisa;")
    print("6. Não deixe crianças brincando na enxurrada ou nas águas dos córregos, pois elas podem ser levadas pela correnteza ou contaminar-se,\ncontraindo doenças graves, como hepatite e leptospirose.")
    print("7. Antes de tudo, salve e proteja vidas. Se precisar retirar algo de sua casa, após a inundação, peça ajuda à \nDefesa Civil (199) ou ao Corpo de Bombeiros (193);")
    print("8. Tente convencer as pessoas que moram em áreas de risco a saírem de casa durante as chuvas;")
    print("9. Evite voltar para casa até as águas baixarem e o caminho estar seguro.Só entre na água se for absolutamente necessário, usando botas de borracha.")
    print("\n")
    if voltarVerOpcao():
        guiasobre()
    
#Para ensinar como agir se for pego de surpresa dentro do carro, o que é uma situação comum e perigosa.
def nocarro():
    print("\n--- SE ESTIVER NO CARRO ---")
    print("1. Diminua a velocidade e mantenha distância do veículo da frente;")
    print("2. Pare o carro em local seguro e alto;")
    print("3. Escute o rádio para saber o melhor caminho;")
    print("4. Nunca atravesse áreas alagadas, caso não for possível, procure dirigir devagar, mantendo o carro acelerado;")
    print("5. Se a água estiver subindo, procure abrigo com sua família.")
    print("\n")
    if voltarVerOpcao():
       guiasobre()
   
#Para garantir que as pessoas saibam como agir após o desastre, prevenindo doenças e novos riscos.  
def depois():
    print("\n--- APÓS A ENCHENTE ---")
    print("1. Beba apenas água filtrada ou fervida;")
    print("2. Não consuma alimentos que tiveram contato com a água;")
    print("3. Fique atento a sintomas de doenças, tais como febre, vômito, dor de cabeça ou no corpo (principalmente na “batata da perna”), e diarreia; nesses casos,\nprocure os serviços de saúde;")
    print("4. Não use aparelhos elétricos que estiveram molhados;")
    print("5. Desinfete objetos com água sanitária (1 copo para 1 balde de 20 litros de água limpa) utilizando luvas e botas;")
    print("6. Chuvas de grande intensidade ou longa duração provocam deslizamentos, principalmente em áreas de risco: fique atento a qualquer sinal;")
    print("\n")
    if voltarVerOpcao():
       guiasobre()
   


#Função do Quiz
#Um quiz com perguntas baseadas no Guia de Sobrevivência e um sistema de pontuação
#Para testar os conhecimentos adquiridos, reforçando o aprendizado e incentivando a revisão do guia.
def quiz():
    print("\nQUIZ: Você sobreviveria a uma Enchente/Inundação?")
    print("Responda com A, B ou C. Digite S a qualquer momento para sair e voltar ao menu.")
    pontos = 0

    perguntas = [
        "O que você deve fazer ao perceber que o nível da água está subindo rapidamente?",
        "Qual desses objetos é essencial em um kit de emergência?",
        "Por que não é seguro andar em água de enchente?",
        "O que fazer antes de uma enchente para proteger seus documentos importantes?",
        "Por que não se deve jogar lixo em córregos ou nas ruas?",
        "Durante uma enchente, o que é mais seguro fazer?",
        "Após uma enchente, o que NÃO deve ser feito?",
        "Se estiver dirigindo e perceber uma área alagada à frente, o que fazer?"
    ]

    alternativas = [
        ["A) Continuar normalmente dentro de casa",
         "B) Subir para um local mais alto ou sair da área com segurança",
         "C) Aguardar ajuda dentro do carro"],

        ["A) Controle remoto",
         "B) Lanterna com pilhas",
         "C) Espelho de maquiagem"],

        ["A) Pode sujar as roupas",
         "B) A água pode esconder buracos e estar contaminada",
         "C) É muito fria"],

        ["A) Jogá-los fora para não se preocupar com eles",
         "B) Deixá-los em cima da mesa da sala",
         "C) Colocá-los em sacos plásticos bem fechados e guardá-los em local seguro"],

        ["A) Porque pode ser multado",
         "B) Porque o lixo enfeia a cidade",
         "C) Porque pode entupir a passagem de água e causar enchentes"],

        ["A) Caminhar pela rua alagada para ver os estragos",
         "B) Ficar em local seguro e evitar sair",
         "C) Brincar com os vizinhos na enxurrada"],

        ["A) Beber apenas água filtrada ou fervida",
         "B) Utilizar aparelhos elétricos molhados",
         "C) Procurar ajuda médica ao apresentar sintomas suspeitos"],

        ["A) Acelerar o carro e tentar passar rápido",
         "B) Procurar um local alto e seguro para parar",
         "C) Esperar a água subir para decidir"]
    ]

    corretas = ["B", "B", "B", "C", "C", "B", "B", "B"]

    for i in range(len(perguntas)):

        print(f"\n{i+1}) {perguntas[i]}")

        for alt in alternativas[i]:
            print(alt)
        resposta = input("Sua resposta: ").upper()

        if resposta == "S":
            print("\nQuiz encerrado. Voltando ao menu principal...")
            return
        elif resposta == corretas[i]:
            print("Correto!")
            pontos += 1
        else:
            print("Resposta incorreta.")

    print(f"\nSua pontuação foi de {pontos} de {len(perguntas)}.")

    if pontos >= 6:
        print("PARABÉNS! Você tem o conhecimento necessário para sobreviver em uma enchente!") 
    else:
        print("Que pena! Sua pontuação foi baixa. Consulte o Guia de Sobrevivência para aprender informações que podem salvar sua vida!")



#Função para consultar a porcentagem de risco de desastres causados #por chuva em cada região 
#Para aumentar a consciência do risco por região, ajudando na preparação e prevenção.
def consulta_regiao():  
    while True:
        print("\n-- CONSULTA DE RISCO DE ENCHENTES POR REGIÃO --")
        print("1 - Sudeste")
        print("2 - Nordeste")
        print("3 - Sul")
        print("4 - Norte")
        print("5 - Centro-Oeste")
        print("0 - Voltar ao menu")

        regiao = input("Escolha a região: ")

        if regiao == "1":
            print("\nSudeste: 36,04% dos municípios possuem risco de desastres causados por chuva, de um total de 1.668 municípios.")
            
        elif regiao == "2":
            print("\nNordeste: 34% dos municípios possuem risco de desastres causados por chuva, de um total de 1.794 municípios.")
            

        elif regiao == "3":
            print("\nSul: 36,03% dos municípios possuem risco de desastres causados por chuva, de um total de 1.191 municípios.")
          
        elif regiao == "4":
            print("\nNorte: 46.22% dos municípios possuem risco de desastres causados por chuva, de um total de 450 municípios.")
            

        elif regiao == "5":
            print("\nCentro-Oeste: 20,12% dos municípios possuem risco de desastres causados por chuva, de um total de 467 municípios.")
           
        elif regiao == "0":
            break
        else:
            print("Opção inválida.")


#Lista para armazenar os registros de enchentes adicionados pelo usuário
registros_enchentes = []

#Função que permite registrar e consultar ocorrências de enchentes
#Para ajudar a criar uma base de dados local com ocorrências, incentivando a conscientização e a memória coletiva.

def registrar_enchente():
    while True:
        print("\n-- REGISTROS DE ENCHENTES --")
        print("1 - Adicionar novo registro")
        print("2 - Listar todos os registros")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            estado = input("Digite o estado (sigla): ").strip().upper()
            cidade = input("Digite a cidade: ").strip().title()
            data = input("Digite a data (DD/MM/AAAA): ").strip()
            if estado and cidade and data:
                registros_enchentes.append([estado, cidade, data])
                print("Registro adicionado com sucesso!")
            else:
                print("Todos os campos são obrigatórios.")

        elif opcao == "2":
            if registros_enchentes:
                print("\n--- REGISTROS DE ENCHENTES ---")
                for i, registro in enumerate(registros_enchentes, start=1):
                    print(f"{i}. Estado: {registro[0]} | Cidade: {registro[1]} | Data: {registro[2]}")
            else:
                print("Nenhum registro encontrado.")

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")



#Menu principal da aplicação
#Por meio dele o usuário acessará as funções ao inserir o número correspondente á ela
#Ele repetirá (será executado) até que o usuário insira 0
def menu(): 
    while True:
        print("\n-- MENU PRINCIPAL - HYDROSAFE --")
        print("1 - Guia de Sobrevivência para Enchentes")
        print("2 - Quiz: Você sobreviveria a uma inundação?")
        print("3 - Consultar ocorrências de enchentes por região")
        print("4 - Registrar e consultar ocorrências de Enchente")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            guiasobre()
        elif opcao == "2":
            quiz()
        elif opcao == "3":
            consulta_regiao()
        elif opcao == "4":
            registrar_enchente()    
        elif opcao == "0":
            print("Saindo... Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")

    
#Chamando a função Menu que iniciará todo o sistema
menu()
 




