import sqlite3

class DatabaseManager:
    def inserir_jogador(jogador, posicao):
        if jogador == " " or posicao == " ":
                print("Jogador inválido.")
                return
        with sqlite3.connect("team.db") as conexao:
            cursor = conexao.cursor()
            comando_sql = "INSERT INTO lineup (nome, posicao) VALUES (?, ?)"
            cursor.execute(comando_sql, (jogador.nome, posicao))
            conexao.commit()