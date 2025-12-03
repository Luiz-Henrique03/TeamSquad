import players
import databaseManager

Datamanager = databaseManager.DatabaseManager


def set_lineup():
    i = 1
    print("Convoque sua seleção ")
    while i < 3:
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
        
      

    

set_lineup()     
    