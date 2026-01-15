import players
import databaseManager

class Team:
    def __init__(self):
        self.db_manager = databaseManager.DatabaseManager

    def _cadastrar_posicao(self, nome_posicao, quantidade_limite):
        """
        Método auxiliar genérico para cadastrar jogadores de qualquer posição.
        Evita a repetição de código (DRY - Don't Repeat Yourself).
        """
        i = 1

        while i <= quantidade_limite:
            nome = input(f"Nome {nome_posicao} ({i}/{quantidade_limite}): ").strip()
            
            if name == "":
                print("Entrada inválida. Tente novamente.")
            else:
                try:
                    nota = float(input(f"Digite a nota do {nome}: "))
                    
                    novo_jogador = players.Player(nome, nome_posicao, nota)
                    
                    self.db_manager.insert_player(novo_jogador, nome_posicao, nota)
                    print(f"{nome_posicao} inserido com sucesso!")
                    i += 1
                except ValueError:
                    print("Por favor, digite uma nota válida (número).")

    
    def Goleiros(self):
        print("\n--- Cadastro de Goleiros ---")
        self._cadastrar_posicao("Goleiro", 3)

    def Laterais(self):
        print("\n--- Cadastro de Laterais ---")
        self._cadastrar_posicao("Lateral", 4)

    def Zagueiros(self):
        print("\n--- Cadastro de Zagueiros ---")
        self._cadastrar_posicao("Zagueiro", 5)

    def Meio(self):
        print("\n--- Cadastro de Meio-campistas ---")
        self._cadastrar_posicao("Meio-campista", 5)

    def Atacante(self):
        print("\n--- Cadastro de Atacantes ---")
        self._cadastrar_posicao("Atacante", 6)

    def set_lineup(self):
        print("\n========= Convocando sua Seleção =========")
        

        configuracao_tatica = [
            ("Goleiro", 1),
            ("Lateral", 2),
            ("Zagueiro", 2),
            ("Meio-campista", 3),
            ("Atacante", 3) 
        ]

        escalacao_final = {}

        for posicao, qtd_titulares in configuracao_tatica:
            todos_jogadores = self.db_manager.get_players_by_position(posicao)
            print(f"{posicao}s disponíveis: {len(todos_jogadores)}")

            if not todos_jogadores:
                escalacao_final[posicao] = []
                continue


            jogadores_ordenados = sorted(todos_jogadores, key=lambda x: x[2], reverse=True)

            titulares = jogadores_ordenados[:qtd_titulares]
            escalacao_final[posicao] = titulares

        print("\n========= TIME TITULAR =========")
        print(f"Melhor Goleiro: {escalacao_final['Goleiro']}")
        print(f"Melhores Laterais: {escalacao_final['Lateral']}")
        print(f"Melhores Zagueiros: {escalacao_final['Zagueiro']}")
        print(f"Melhores Meias: {escalacao_final['Meio-campista']}")
        print(f"Melhores Atacantes: {escalacao_final['Atacante']}")

    def menu(self):
        while True:
            print("\nBem vindo ao app de convocação")
            print("1. Cadastrar Goleiros")
            print("2. Cadastrar Laterais")
            print("3. Cadastrar Zagueiros")
            print("4. Cadastrar Meio-campo")
            print("5. Cadastrar Atacantes")
            print("6. Escalar Time (Set Lineup)")
            print("0. Sair")
            
            opcao = input("Escolha uma opção: ")

            if opcao == "1": self.Goleiros()
            elif opcao == "2": self.Laterais()
            elif opcao == "3": self.Zagueiros()
            elif opcao == "4": self.Meio()
            elif opcao == "5": self.Atacante()
            elif opcao == "6": self.set_lineup()
            elif opcao == "0": break
            else: print("Opção inválida.")

if __name__ == "__main__":
    time = Team()
    time.menu()