import players
import databaseManager

Datamanager = databaseManager.DatabaseManager

def Goleiros():
    i = 1
    while i < 4:
            if i < 1:
                i = 1
            name = input("Nome goleiro: ")
            if name == "": 
                print("Entrada inválida. Tente novamente.")
                i = i - 1
                print(i)
            elif name != "":
                position = "Goleiro"
                score = float(input("Digite a nota do jogador: "))
            
                player = players.Player(name, position, score)
                Datamanager.insert_player(player, position,score)
                i+=1

def Laterais():
    i = 1
    while i < 5:
            if i < 1:
                i = 1
            name = input("Nome Lateral: ")
            if name == "": 
                print("Entrada inválida. Tente novamente.")
                i = i - 1
                print(i)
            elif name != "":
                position = "Lateral"
                score = float(input("Digite a nota do jogador: "))
            
                player = players.Player(name, position, score)
                Datamanager.insert_player(player, position,score)
                i+=1

def Zagueiros():
    i = 1
    while i < 6:
            if i < 1:
                i = 1
            name = input("Nome Zagueiro: ")
            if name == "": 
                print("Entrada inválida. Tente novamente.")
                i = i - 1
                print(i)
            elif name != "":
                position = "Zagueiro"
                score = float(input("Digite a nota do jogador: "))
            
                player = players.Player(name, position, score)
                Datamanager.insert_player(player, position,score)
                i+=1

def Meio():
    i = 1
    while i < 6:
            if i < 1:
                i = 1
            name = input("Nome do meia: ")
            if name == "": 
                print("Entrada inválida. Tente novamente.")
                i = i - 1
                print(i)
            elif name != "":
                position = "Meio-campista"
                score = float(input("Digite a nota do jogador: "))
            
                player = players.Player(name, position, score)
                Datamanager.insert_player(player, position,score)
                i+=1


def Atacante():
    i = 1
    while i < 7:
            if i < 1:
                i = 1
            name = input("Nome do atacante: ")
            if name == "": 
                print("Entrada inválida. Tente novamente.")
                i = i - 1
                print(i)
            elif name != "":
                position = "Atacante"
                score = float(input("Digite a nota do jogador: "))
            
                player = players.Player(name, position, score)
                Datamanager.insert_player(player, position,score)
                i+=1

def set_lineup():
    i = 1
    contador_posicao = 1
    contador_laterais = 0
    contador_zagueiros = 0
    contador_meiocampo = 0
    
    maior = 0
    goleiros_titulares = []
    laterais_titulares = []
    zagueiros_titulares = [] 
    Meias_titulares = []
    Atacantes_titulares = []

    print("Convoque sua seleção ")
    
    goleiros = Datamanager.get_players_by_position("Goleiro")
    print("Goleiros convocados:", goleiros)
    for i in range(len(goleiros)):
         maior = goleiros[0][2]
         if goleiros[i][2] >= maior:
            maior = goleiros[i][2]
            goleiros_titulares.append(goleiros[i])

    Laterais = Datamanager.get_players_by_position("Lateral")
    for contador_laterais in range(0,2):
        for i in range(len(Laterais)):
            maior = Laterais[0][2]
            if Laterais[i][2] >= maior:
                maior = Laterais[i][2]
                if Laterais[i] not in laterais_titulares:
                    laterais_titulares.append(Laterais[i])
    
    Zagueiros = Datamanager.get_players_by_position("Zagueiro")
    print("Zagueiros convocados:", Zagueiros)
    for contador_zagueiros in range(0,2):
        for i in range(len(Zagueiros)):
            maior = Zagueiros[0][2]
            if Zagueiros[i][2] >= maior:
                maior = Zagueiros[i][2]
                if Zagueiros[i] not in zagueiros_titulares:
                    zagueiros_titulares.append(Zagueiros[i])

    Meias = Datamanager.get_players_by_position("Meio-campista")
    print("Meias convocados:", Meias)                

    for contador_meiocampo in range(0,3):
        for i in range(len(Meias)):
            maior = Meias[0][2]
            if Meias[i][2] >= maior:
                maior = Meias[i][2]
                if Meias[i] not in Meias_titulares:
                    Meias_titulares.append(Meias[i])

    Atacantes = Datamanager.get_players_by_position("Atacante")
    print("Atacantes convocados:", Atacantes)
    for i in range(len(Atacantes)):
            maior = Atacantes[0][2]
            if Atacantes[i][2] >= maior:
                maior = Atacantes[i][2]
                Atacantes_titulares.append(Atacantes[i])

    print("Melhor goleiro:", goleiros_titulares)
    print("Melhores laterais:", laterais_titulares)
    print("Melhores zagueiros:", zagueiros_titulares)
    print("Melhores Meias:", Meias_titulares)
    print("Melhores Atacantes:", Atacantes_titulares)
    

        
      

    

set_lineup()     
    