"""
    Desafio Avançado Hackathon Imagimaker
    
"""
import random

class velhota():
    def __init__(self):
        #
        # Inicialização das Variáveis
        #
        self.computador = False # Modo computador desativado
        self.tabuleiro = [x  for x in range(9)] # Inicializando o tabuleiro
        self.restantes = [x for x in range(9)] # posições restantes
        self.placar = [0,0,0] # placar vitorias(1ª,2ª) empates (3ª)
        self.ordem=[] #ordem das jogadas X ou O
        self.vez = 0 # vez de cada jogador
    
    def imprimir(self):
        #
        # Imprime o tabuleiro
        #
        
        print(" {} | {} | {}".format(self.tabuleiro[0],self.tabuleiro[1],self.tabuleiro[2]))
        print("--- --- ---")
        print(" {} | {} | {}".format(self.tabuleiro[3],self.tabuleiro[4],self.tabuleiro[5]))
        print("--- --- ---")
        print(" {} | {} | {}\n".format(self.tabuleiro[6],self.tabuleiro[7],self.tabuleiro[8]))

    def imprimir_placar(self,frase=''):
        #
        # Imprime o placar 
        #
        if self.computador:
            print("PLACAR "+frase,": \n\nPlayer1 | {} | Empate\n   {}           {}          {}\n\n".format("Computador",self.placar[0],self.placar[1],self.placar[2]))
        else:
            print("PLACAR: \n\nPlayer1 | {} | Empate\n   {}           {}          {}\n\n".format("Player2",self.placar[0],self.placar[1],self.placar[2]))


    def jogo(self):
        while True:
            self.imprimir() # imprime o tabuleiro

            #
            # Printar corretamente
            #

            print("-- Vez do jogador {} -- \n".format(self.ordem[self.vez]))
            
            #
            # jogada do computador 
            #

            if self.vez ==1 and self.computador:
                jogada = self.jogadaComputador()
            else:
                jogada = int(input("Qual sua jogada (apenas numeros)?\n>> ")) # jogada do player

                #
                # Tratamentos de erros
                #

                if jogada < 0 and jogada > 8: #caso não seja numeros do tabuleiro
                    print(jogada, " Jogada inválida, tente de 0 a 8\n")
                    continue

                if self.tabuleiro[jogada] in self.ordem: #caso as jogadas sejam repetidas
                    print("\nPosição ",jogada," Ocupada\n")
            resultado = self.jogada(jogada)
            if resultado != 2:
                self.encerramento(resultado)
                break
    
    def jogada(self,posicao):

        #
        # Adiciona no tabuleiro e remove as posições já usadas
        #

        self.tabuleiro[posicao] = self.ordem[self.vez]
        self.restantes.remove(posicao)

        #
        # Verifica se Houve um ganhador
        #
        if self.tabuleiro[0] == self.tabuleiro[1] == self.tabuleiro[2]:
            return 1
        elif self.tabuleiro[3] == self.tabuleiro[4] == self.tabuleiro[5]:
            return 1
        elif self.tabuleiro[6] == self.tabuleiro[7] == self.tabuleiro[8]:
            return 1
        elif self.tabuleiro[0] == self.tabuleiro[4] == self.tabuleiro[8]:
            return 1
        elif self.tabuleiro[2] == self.tabuleiro[4] == self.tabuleiro[6]:
            return 1
        elif self.tabuleiro[0] == self.tabuleiro[3] == self.tabuleiro[6]:
            return 1
        elif self.tabuleiro[1] == self.tabuleiro[4] == self.tabuleiro[7]:
            return 1
        elif self.tabuleiro[2] == self.tabuleiro[5] == self.tabuleiro[8]:
            return 1
        elif self.restantes == []: # Verifica se todos os campos foram preenchidos
            return 3

        #
        # Se nao muda a vez
        #
        
        if self.vez == 0:
            self.vez = 1
        else:
            self.vez = 0
        return 2

    def encerramento(self,tipo): 
        #
        # Imprime mensagens dos Resultados
        #
        if tipo == 3:
            print("------------------------")
            print("\nResultado: EMPATE\n")
            print("------------------------")
            self.placar[2]+=1
            return 3
        elif self.computador:
            if self.vez == 0:
                print("------------------------")
                print("\nResultado: Você Ganhou\n")
                print("------------------------")
            else:
                print("------------------------")
                print("\nResultado: Você Perdeu\n")
                print("------------------------")
            self.placar[self.vez]+=1
            return 2
        else:
            print("------------------------")
            print("\nResultado: Jogador {} Ganhou!\n".format(self.ordem[self.vez]))
            print("------------------------")
            self.placar[self.vez]+=1
            return 2



    def jogadaComputador(self):
        #
        # O computador pega um número aleatório
        #
        jogada = int(random.choice(self.restantes))
        return jogada

    def start(self):
        #
        # Qual cursor ele quer jogar
        #

        cursor = input("Deseja jogar usando 'X' ou 'O'?\n>> ")
        
        #
        # Tratamento de Erro
        #
        cursor = cursor.upper()

        if cursor not in ["O","X"]:
            print(cursor," Não é uma opção válida -- Encerrando o jogo.")
            exit(1)
        self.ordem.append(cursor)
        if cursor == "X":
            self.ordem.append("O")
        else:
            self.ordem.append("X")
        #
        # Computador ou Player?
        #

        player = input("Deseja jogar contra COMPUTADOR (C) ou HUMANO (H)?\n>> ")
        player = player.upper()

        #
        # Tratamento de Erro
        #

        if player not in ['COMPUTADOR',"HUMANO","C","H"]:
            print(player," Não é uma opção válida -- Encerrando o jogo.")
            exit(1)
        elif player in ['COMPUTADOR','C']:
            self.computador = True
        
        #
        # Começa o jogo
        #

        while True:
            self.jogo() # Inicia o jogo
            self.imprimir_placar() # imprime o placar uma vez por jogo
            esc = str(input("Deseja continuar jogando? (S/N)\n>> ")).upper()
            #
            # Tratamento de Erro
            #
            if esc not in ['S','N']:
                print(esc, " Jogada inválida, Jogo Encerrado\n")
                break
            if esc == 'S':
                #
                # Reseta as variáveis
                #
                self.tabuleiro = [x  for x in range(9)]
                self.restantes = [x for x in range(9)]
                self.vez = 0
                continue
            else: 
                break
        
        
        self.imprimir_placar(frase="FINAL")

        print("\n\n Obrigado por jogar \n\n")
                
game = velhota()
game.start()
