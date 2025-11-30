import players
import databaseManager

Datamanager = databaseManager.DatabaseManager

name = input("Digite o nome do jogador: ")
position = input("Digite a posição do jogador: ")
score = float(input("Digite a nota do jogador: "))
player = players.Player(name, position, score)
Datamanager.insert_player(player, position)

        
    