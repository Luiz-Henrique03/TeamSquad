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
    maior = 0
    melhor_da_posicao = ""
    print("Convoque sua seleção ")
    
    goleiros = Datamanager.get_players_by_position("Goleiro")
    print("Goleiros convocados:", goleiros)
    for i in range(len(goleiros)):
         maior = goleiros[0][2]
         if goleiros[i][2] >= maior:
            maior = goleiros[i][2]
            melhor_da_posicao = goleiros[i]
            
    print("Melhor goleiro:", melhor_da_posicao[0])
        
      

    

set_lineup()     
    