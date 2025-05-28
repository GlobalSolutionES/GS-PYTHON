def menu(): # Menu principal da aplicação
    while True:
        print("\n-- MENU PRINCIPAL --")
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


# Guia de Sobrevivência
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




# Funções do guia

def prevencao():
    print("\n-- PREVENÇÃO CONTRA ENCHENTES --")
    print("1. Moradores de regiões propensas a inundações devem manter-se informados sobre as condições meteorológicas;")
    print("2. Evite construir em cima e embaixo de barrancos que possam deslizar, carregando sua casa;")
    print("3. Não jogue lixo ou entulho no córrego, para não obstruir a passagem de água, nem em terrenos baldios ou ruas;")
    print("4. Limpe o telhado, calhas, condutores e canaletas para evitar entupimentos.")
    print("\n")
    if voltarVerOpcao():
        guiasobre()


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
    
    
def durante():

    print("\n--- DURANTE A ENCHENTE ---")
    print("1. Proteja a sua vida, a de seus familiares e amigos. Evite contato com as águas de enchentes, elas estão contaminadas e podem provocar doenças;")
    print("2. Se estiver em local seguro, procure não se deslocar; não atravesse ruas alagadas, pois você pode ser arrastado pela água;")
    print("3. Em local alagado, preste atenção a buracos e bueiros sem tampas ou encobertos pela água;")
    print("4. Em caso de ventos muito fortes, cuidado com as quedas de árvores, fios, postes, semáforos, etc;")
    print("5. Utilize calçado, calça comprida e blusa para a proteção do corpo; não use bermuda e não fique sem camisa;")
    print("6. Não deixe crianças brincando na enxurrada ou nas águas dos córregos, pois elas podem ser levadas pela correnteza ou contaminar-se,\ncontraindo doenças graves, como hepatite e leptospirose.")
    print("7.Antes de tudo, salve e proteja vidas. Se precisar retirar algo de sua casa, após a inundação, peça ajuda à \nDefesa Civil (199) ou ao Corpo de Bombeiros (193);")
    print("8.Tente convencer as pessoas que moram em áreas de risco a saírem de casa durante as chuvas;")
    print("9.Evite voltar para casa até as águas baixarem e o caminho estar seguro.Só entre na água se for absolutamente necessário, usando botas de borracha.")
    print("\n")
    if voltarVerOpcao():
        guiasobre()
    

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
   
def depois():
    print("\n--- APÓS A ENCHENTE ---")
    print("1. Beba apenas água filtrada ou fervida;")
    print("2. Não consuma alimentos que tiveram contato com a água;")
    print("3. Fique atento a sintomas de doenças, tais como febre, vômito, dor de cabeça ou no corpo (principalmente na “batata da perna”), e diarréia; nesses casos,\nprocure os serviços de saúde;")
    print("4. Não use aparelhos elétricos que estiveram molhados;")
    print("5. Desinfete objetos com água sanitária (1 copo para 1 balde de 20 litros de água limpa) utilizando luvas e botas;")
    print("6. Chuvas de grande intensidade ou longa duração provocam deslizamentos, principalmente em áreas de risco: fique atento a qualquer sinal;")
    print("\n")
    if voltarVerOpcao():
       guiasobre()
   

#Função sobre o Quiz
def quiz():
    print("\n-- QUIZ: Você sobreviveria a uma Enchente/Inundação? --")
    print("Responda com A, B ou C.")
    pontos = 0

    # Pergunta 1
    print("\n1) O que você deve fazer ao perceber que o nível da água está subindo rapidamente?")
    print("A) Continuar normalmente dentro de casa")
    print("B) Subir para um local mais alto ou sair da área com segurança")
    print("C) Aguardar ajuda dentro do carro")
    resposta1 = input("Sua resposta: ").upper()
    if resposta1 == "B":
        print("Correto!")
        pontos += 1
    else:
        print("Resposta incorreta. O ideal é procurar abrigo seguro imediatamente.")


    # Pergunta 2
    print("\n2) Qual desses objetos é essencial em um kit de emergência?")
    print("A) Controle remoto")
    print("B) Lanterna com pilhas")
    print("C) Espelho de maquiagem")
    resposta2 = input("Sua resposta: ").upper()
    if resposta2 == "B":
        print("Correto!")
        pontos += 1
    else:
        print("Resposta incorreta. Uma lanterna pode salvar vidas no escuro.")

    print(f"Sua pontuação foi de {pontos}.")
    if pontos > 3:
        print("PARABÉNS! Você tem o conhecimento necessário para sobreviver em uma enchente!") 
    else:
        print("Que pena! Sua pontuação foi baixa, consulte o Guia de Sobrevivência para aprender informações que podem salvar sua vida!")       

    # Pergunta 3
    print("\n3) Por que não é seguro andar em água de enchente?")
    print("A) Pode sujar as roupas")
    print("B) A água pode esconder buracos e estar contaminada")
    print("C) É muito fria")
    resposta3 = input("Sua resposta: ").upper()
    if resposta3 == "B":
        print("Correto!")
        pontos += 1
    else:
        print("Resposta incorreta. A água pode causar acidentes e doenças.")

    print(f"Sua pontuação foi de {pontos}.")
    if pontos > 3:
        print("PARABÉNS! Você tem o conhecimento necessário para sobreviver em uma enchente!") 
    else:
        print("Que pena! Sua pontuação foi baixa, consulte o Guia de Sobrevivência para aprender informações que podem salvar sua vida!")     

def consulta_regiao():  # Consulta região
    while True:
        print("\n-- CONSULTA DE ENCHENTES POR REGIÃO --")
        print("1 - Sudeste")
        print("2 - Nordeste")
        print("3 - Sul")
        print("4 - Norte")
        print("5 - Centro-Oeste")
        print("0 - Voltar ao menu")

        regiao = input("Escolha a região: ")

        if regiao == "1":
            print("Sudeste: 42% das ocorrências.")
            consulta_estado_sudeste()
        elif regiao == "2":
            print("Nordeste: 20% das ocorrências.")
            consulta_estado_nordeste()
        elif regiao == "3":
            print("Sul: 18% das ocorrências.")
            consulta_estado_sul()
        elif regiao == "4":
            print("Norte: 12% das ocorrências.")
            consulta_estado_norte()
        elif regiao == "5":
            print("Centro-Oeste: 8% das ocorrências.")
            consulta_estado_centrooeste()
        elif regiao == "0":
            break
        else:
            print("Opção inválida.")


def consulta_estado_sudeste():
    while True:
        print("\nDeseja consultar um estado específico?")
        print("1 - SP (São Paulo)")
        print("2 - MG (Minas Gerais)")
        print("3 - RJ (Rio de Janeiro)")
        print("0 - Voltar")

        escolha = input("Escolha: ")

        if escolha == "1":
            print("SP: 25% das ocorrências da região Sudeste.")
        elif escolha == "2":
            print("MG: 10% das ocorrências.")
        elif escolha == "3":
            print("RJ: 7% das ocorrências.")
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")


def consulta_estado_nordeste():
    while True:
        print("\nDeseja consultar um estado específico?")
        print("1 - BA (Bahia)")
        print("2 - PE (Pernambuco)")
        print("3 - CE (Ceará)")
        print("0 - Voltar")

        escolha = input("Escolha: ")

        if escolha == "1":
            print("BA: 8% das ocorrências da região Nordeste.")
        elif escolha == "2":
            print("PE: 7% das ocorrências.")
        elif escolha == "3":
            print("CE: 5% das ocorrências.")
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")


def consulta_estado_sul():
    while True:
        print("\nDeseja consultar um estado específico?")
        print("1 - RS (Rio Grande do Sul)")
        print("2 - SC (Santa Catarina)")
        print("3 - PR (Paraná)")
        print("0 - Voltar")

        escolha = input("Escolha: ")

        if escolha == "1":
            print("RS: 9% das ocorrências da região Sul.")
        elif escolha == "2":
            print("SC: 6% das ocorrências.")
        elif escolha == "3":
            print("PR: 3% das ocorrências.")
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")


def consulta_estado_norte():
    while True:
        print("\nDeseja consultar um estado específico?")
        print("1 - AM (Amazonas)")
        print("2 - PA (Pará)")
        print("3 - RO (Rondônia)")
        print("0 - Voltar")

        escolha = input("Escolha: ")

        if escolha == "1":
            print("AM: 5% das ocorrências da região Norte.")
        elif escolha == "2":
            print("PA: 4% das ocorrências.")
        elif escolha == "3":
            print("RO: 3% das ocorrências.")
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")


def consulta_estado_centrooeste():
    while True:
        print("\nDeseja consultar um estado específico?")
        print("1 - GO (Goiás)")
        print("2 - MT (Mato Grosso)")
        print("3 - MS (Mato Grosso do Sul)")
        print("0 - Voltar")

        escolha = input("Escolha: ")

        if escolha == "1":
            print("GO: 4% das ocorrências da região Centro-Oeste.")
        elif escolha == "2":
            print("MT: 2% das ocorrências.")
        elif escolha == "3":
            print("MS: 2% das ocorrências.")
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")



registros_enchentes = []

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

    
# Iniciar o sistema
menu()
 




