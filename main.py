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
                Datamanager.insert_player(player, position)
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
                Datamanager.insert_player(player, position)
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
                Datamanager.insert_player(player, position)

def set_lineup():
    i = 1
    print("Convoque sua seleção ")
    Goleiros()
    Laterais()
    Zagueiros()
    
        
      

    

set_lineup()     
    