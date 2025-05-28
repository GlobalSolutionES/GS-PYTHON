'''Função para Guia de sobrevivência em Enchentes'''
def guia():
    print("----------------------------------------")
    print("|                                      |")
    print("| Guia de Sobrevivência para Enchentes |")
    print("|                                      |")
    print("----------------------------------------")

    print("Este Guia visa informar, educar e alertar acerca do que deve ser feito ANTES, DURANTE e APÓS a ocorrência de Enchente e, também, como PREVENIR.\nLeia com atenção, compartilhe essas informações e retorne sempre que houver a necessidade.")

    print("--------------------------------------------------------------------------------------------")

    print("Orientações para PREVENIR enchentes:\n1.Moradores de regiões propensas a inundações devem manter-se informados sobre as condições meteorológicas;\n2.Evite construir em cima e embaixo de barrancos que possam deslizar, carregando sua casa;\n3.Não jogue lixo ou entulho no córrego, para não obstruir a passagem de água, nem em terrenos baldios ou ruas;\n4.Limpe o telhado, calhas, condutores e canaletas para evitar entupimentos;")

    print("--------------------------------------------------------------------------------------------")

    print("Você recebeu a informação que a região onde está sob risco de Enchente, seja por notificação, notícia ou experiências anteriores.\nANTES da enchente você deve:\n\n1.Tenha um lugar previsto, seguro, onde você e sua família possam se alojar no caso de inundação;\n2.Ao primeiro sinal de chuva forte, coloque os móveis, eletrodomésticos e demais objetos em lugares altos;\n3.Coloque documentos e objetos de valor em sacos plásticos bem fechados e em local protegido;\n3.Feche as portas, janelas e o registro de entrada de água;\n4.Desligue aparelhos elétricos e eletrônicos, a chave geral de sua casa e feche os registros de entrada de água e de gás;\n5.Retire todo o lixo e leve-o para áreas não sujeitas a inundações;\n6.Retire os animais de estimação de casa.\n7.Seja solidário: avise seus vizinhos sobre o perigo, no caso de casas construídas em áreas de risco de deslizamentos; avise também, imediatamente,\no Corpo de Bombeiros (193) e à Defesa Civil (199);")

    print("--------------------------------------------------------------------------------------------")

    print("Você já está enfrentando uma enchente na região onde mora.\nDURANTE a enchente você deve:\n1.Proteja a sua vida, a de seus familiares e amigos. Evite contato com as águas de enchentes, elas estão contaminadas e podem provocar doenças;\n2.Se estiver em local seguro, procure não se deslocar; não atravesse ruas alagadas, pois você pode ser arrastado pela água;\n3.Em local alagado, preste atenção a buracos e bueiros sem tampas ou encobertos pela água;\n4.Em caso de ventos muito fortes, cuidado com as quedas de árvores, fios, postes, semáforos, etc;\n5.Utilize calçado, calça comprida e blusa para a proteção do corpo; não use bermuda e não fique sem camisa;\n6.Não deixe crianças brincando na enxurrada ou nas águas dos córregos, pois elas podem ser levadas pela correnteza ou contaminar-se,\ncontraindo doenças graves, como hepatite e leptospirose.\n7.Antes de tudo, salve e proteja vidas. Se precisar retirar algo de sua casa, após a inundação, peça ajuda à \nDefesa Civil ou ao Corpo de Bombeiros nos telefones mencionados acima;\n8.Tente convencer as pessoas que moram em áreas de risco a saírem de casa durante as chuvas.\n9.Evite voltar para casa até as águas baixarem e o caminho estar seguro.Só entre na água se for absolutamente necessário, usando botas de borracha.")

    print("--------------------------------------------------------------------------------------------")

    print("Se você estiver em um carro durante a enchente, diminua a velocidade e mantenha distância do veículo da frente. Procure parar o carro em locais altos e livres de enchentes;\ncertifique-se, por intermédio do rádio, de qual é o melhor itinerário a seguir, a fim de escapar das áreas alagadas; nunca atravesse áreas cobertas pela água;\nse isso não for possível, procure dirigir devagar, mantendo o carro acelerado; evite se aproximar de outro veículo, espere que ele passe totalmente para então seguir em frente;\nSe o nível de água estiver subindo, vá com sua família para um lugar seguro;")

    print("--------------------------------------------------------------------------------------------")

    print("Sua região passou por uma inundação/enchente. APÓS a enchente, você deve:\n1.Beber apenas água filtrada ou fervida;\n2.Não utilizar alimentos que estiveram em contato com a água da inundação;\n3.Ficar atento aos sintomas de doenças, tais como febre, vômito, dor de cabeça ou no corpo (principalmente na “batata da perna”), e diarréia; nesses casos,\nprocure os serviços de saúde;\n4.Chuvas de grande intensidade ou longa duração provocam deslizamentos, principalmente em áreas de risco: fique atento a qualquer sinal;\n5.Não use equipamentos elétricos que tenham sido molhados ou que estiveram em locais inundados, pois há risco de choque elétrico e curto-circuito;\n6.Lave e desinfete os objetos atingidos pela enchente usando uma mistura de um copo de água sanitária para cada balde de 20 litros de água limpa, utilizando luvas e botas.")

    print("1 - Prevenção")
    print("2 - Antes da Enchente")
    print("3 - Durante a Enchente")
    print("4 - No carro")
    print("5 - após a Enchente")
    print("0 - Voltar ao menu principal")

    escolha = input("Escolha a seçãpo que deseja visualizar: ")

    if escolha == "1":
        prevencao()
    elif escolha == "2":
        antes()
    elif escolha == "3":
        durante()
    elif escolha == "4":
        nocarro()
    elif escolha "5":
        depois()
    elif escolha "0":
        print("Retornando ao menu principal...")
        return
    else:
        print("Opcão inválida. Retornando ao menu principal.")
        return

def voltarouveroutraopcao():
    print("\nDeseja: ")
    print("1 - Ver outra seção do guia")
    print("0 - Voltar ao menu principal")

    escolha = input("Digite sua escolha: ")
    
    if escolha == "1":
        guia()
    else:
        print("Retornando ao menu principal...")

def prevencao():
    print("\n-- PREVENÇÃO --")
    print("1. - Moradores de regiões propensas a inundações devem manter-se informados sobre as condições meteorológicas;")
    print("2. - Evite construir em cima e embaixo de barrancos que possam deslizar, carregando sua casa;")
    print("3. Não jogue lixo ou entulho no córrego, para não obstruir a passagem de água, nem em terrenos baldios ou ruas;")
    print("4. Limpe o telhado, calhas, condutores e canaletas para evitar entupimentos.")
    voltarouveroutraopcao()

def antes():

    print("\n--- ANTES DA ENCHENTE ---")
    print("1. Tenha um lugar seguro para você e sua família;")
    print("2. Coloque móveis e objetos de valor em lugares altos;")
    print("3. Use sacos plásticos para proteger documentos;")
    print("4. Desligue aparelhos e feche registros de água e gás;")
    print("5. Retire o lixo e leve animais para locais seguros;")
    print("6. Avise vizinhos e acione Corpo de Bombeiros (193) e Defesa Civil (199).")
    voltarouveroutraopcao()

def durante():

    print("\n--- DURANTE A ENCHENTE ---")
    print("1. Evite contato com a água de enchente;")
    print("2. Não se desloque se estiver em local seguro;")
    print("3. Atenção a bueiros abertos;")
    print("4. Proteja o corpo com roupas adequadas;")
    print("5. Não deixe crianças brincarem na água;")
    print("6. Só volte para casa após segurança garantida.")
    voltarouveroutraopcao()

def nocarro():
    print("\n--- SE ESTIVER NO CARRO ---")
    print("1. Diminua a velocidade e mantenha distância do veículo da frente;")
    print("2. Pare o carro em local seguro e alto;")
    print("3. Escute o rádio para saber o melhor caminho;")
    print("4. Nunca atravesse áreas alagadas;")
    print("5. Se a água estiver subindo, procure abrigo com sua família.")
    voltarouveroutraopcao()

def depois():
    print("\n--- APÓS A ENCHENTE ---")
    print("1. Beba apenas água filtrada ou fervida;")
    print("2. Não consuma alimentos que tiveram contato com a água;")
    print("3. Fique atento a sintomas de doenças;")
    print("4. Não use aparelhos que estiveram molhados;")
    print("5. Desinfete objetos com água sanitária (1 copo para 1 balde de 20 litros de água limpa).")


def quiz():
    print("\n-- QUIZ DE CONHECIMENTO --")
    pontos = 0

    print("1) O que deve ser feito com documentos importantes?")
    print("a) Jogar fora")
    print("b) Guardar em um local alto e protegido com plástico")
    print("c) Esquecer deles")
    resposta == input("Resposta: ")
    if resposta.lower() == "b":
        pontos += 1

    print("2) O que deve ser evitado durante uma enchente?")
    print("a) Andar na água da enchente")
    print("b) Usar bota e luva")
    print("c) Avisar vizinhos")
    resposta == input("Resposta: ")
    if resposta.lower() == "a":
        pontos += 1

    print("3) Qual é o número da Defesa Civil?")
    print("a) 192")
    print("b) 199")
    print("c) 190")
    resposta == input("Resposta: ")
    if resposta.lower() == "b":
        pontos += 1

    print(f"\n Você fez {pontos} ponto(s) de 3.")
    input("Pressione Enter para entrar no menu...")
    menu()

def consulta_regiao():
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
        return

    else:
        print("Opção inválida.")
        consulta_regiao()

def consulta_estado_sudeste():
    print("Deseja consultar um estado específico?")
    print("1 - SP (São Paulo)")
    print("2 - MG (Minas Gerais)")
    print("3 - RJ (Rio de Janeiro)")
    print("0 - Não")

    escolha = input("Escolha: ")

    if escolha == "1":
        print("SP: 25% das ocorrências da região Sudeste.")

    elif escolha == "2":
        print("MG: 10% das ocorrências.")

    elif escolha == "3":
        print("RJ: 7% das ocorrências.")

    elif escolha == "0":
        return

    else:

        print("Opção inválida.")
        consulta_estado_sudeste()

def consulta_estado_nordeste():

    print("1 - BA")
    print("2 - PE")
    print("3 - CE")
    print("0 - Não")

    escolha = input("Escolha: ")

    if escolha == "1":
        print("BA: 8% das ocorrências.")

    elif escolha == "2":
        print("PE: 7% das ocorrências.")

    elif escolha == "3":
        print("CE: 5% das ocorrências.")

def consulta_estado_sul():

    print("1 - RS")
    print("2 - SC")
    print("3 - PR")
    print("0 - Não")

    escolha = input("Escolha: ")

    if escolha == "1":
        print("RS: 10% das ocorrências.")

    elif escolha == "2":
        print("SC: 5% das ocorrências.")

    elif escolha == "3":
        print("PR: 3% das ocorrências.")

def consulta_estado_norte():
    print("1 - PA")
    print("2 - AM")
    print("3 - RO")
    print("0 - Não")

    escolha = input("Escolha: ")

    if escolha == "1":
        print("PA: 5% das ocorrências.")

    elif escolha == "2":
        print("AM: 4% das ocorrências.")

    elif escolha == "3":
        print("RO: 3% das ocorrências.")

def consulta_estado_centrooeste():
    print("1 - DF")
    print("2 - GO")
    print("3 - MT")
    print("0 - Não")

    escolha = input("Escolha: ")

    if escolha == "1":
        print("DF: 3% das ocorrências.")

    elif escolha == "2":
        print("GO: 3% das ocorrências.")

    elif escolha == "3":
        print("MT: 2% das ocorrências.")

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Ver Guia de Sobrevivência")
        print("2 - Fazer o Quiz")
        print("3 - Consultar porcentagens por região")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            guia()

        elif opcao == "2":
            quiz()

        elif opcao == "3":
            consulta_regiao()

        elif opcao == "0":
            print("Saindo... Até a próxima!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o sistema
menu()
 






#Função Guia está incompleta, falta fazer o sistema para que o usuário tenha opção 
#de exibir uma seção específica, voltar para o menu inicial do sistema final (que não foi criado), 
# e sempre que exibir uma seção: dar opção de voltar para o sistema final ou se quer exibir outra


'''
Funções que faltam: Quiz com base nas informações do Guia de Sobrevivência (sistema com alternativas e pontuação)

Consulta de porcentagem de enchentes por região/estado: Perguntar ao usuário qual região ele deseja consultar, após isso, exibir a porcentagem dessa região e perguntar se quer consultar um estado específico da região, se sim, mostrar as opções de estados (sempre com a opção de voltar ao menu inicial) e perguntar qual, e no fim exibir a porcentagem da região (sudeste, nordeste, etc) e do estado escolhido

Outra opção para o Consulta: Quando a região for escolhida e exibida sua porcentagem, perguntar se deseja ver as porcentagens dos estados, se sim, mostrar todos os estados daquela região e seus respectivos dados
a diferença é que nessa opção todos os estados são exibidos, ao invés do usuário escolher um estado específico

Por fim: Falta o sistema final, aquele que terá um menu que será usado para executar as nossas funções de maneira adequada
'''


