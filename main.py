import players
import databaseManager

Datamanager = databaseManager.DatabaseManager

nome = input("Digite o nome do jogador: ")
posicao = input("Digite a posição do jogador: ")
nota = float(input("Digite a nota do jogador: "))
jogador = players.Player(nome, posicao, nota)
Datamanager.inserir_jogador(jogador, posicao)

        
    