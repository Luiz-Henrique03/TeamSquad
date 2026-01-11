import sqlite3

class DatabaseManager:
    def insert_player(jogador, posicao,nota):
        if jogador == " " or posicao == " ":
                print("Jogador inválido.")
                return
        with sqlite3.connect("team.db") as conexao:
            cursor = conexao.cursor()
            comando_sql = "INSERT INTO lineup (nome, posicao,nota) VALUES (?, ?,?)"
            cursor.execute(comando_sql, (jogador.nome, posicao,nota))
            conexao.commit()
    def get_players_by_position(posicao):
        with sqlite3.connect("team.db") as conexao:
            cursor = conexao.cursor()
            comando_sql = "SELECT nome, posicao,nota FROM lineup WHERE posicao = ?"
            cursor.execute(comando_sql, (posicao,))
            jogadores = cursor.fetchall()
            return jogadores
    def remove_player(nome):
        with sqlite3.connect("team.db") as conexao:
            cursor = conexao.cursor()
            comando_sql = "DELETE FROM lineup WHERE nome = ?"
            cursor.execute(comando_sql, (nome,))
            conexao.commit()
    def clear_lineup():
        with sqlite3.connect("team.db") as conexao:
            cursor = conexao.cursor()
            comando_sql = "DELETE FROM lineup"
            cursor.execute(comando_sql)
            conexao.commit()
    def get_position(name):
        with sqlite3.connect("team.db") as conexao:
            cursor = conexao.cursor()
            comando_sql = "SELECT posicao FROM lineup WHERE nome = ?"
            cursor.execute(comando_sql, (name,))
            posicao = cursor.fetchone()
            return posicao