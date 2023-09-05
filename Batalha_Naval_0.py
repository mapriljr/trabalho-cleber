# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 20:24:57 2023

@author: mapjr
"""
import random

board_size = 10  # Adjust the size of the board as per your requirements

board_1 = [['~' for i in range(board_size)] for j in range(board_size)]
board_2 = [['~' for i in range(board_size)] for j in range(board_size)]

board_o1 = [['~' for i in range(board_size)] for j in range(board_size)]
board_o2 = [['~' for i in range(board_size)] for j in range(board_size)]

ship_sizes = [5, 4, 4, 3, 3, 3, 2, 2, 2, 2]  # Example ship sizes


ship_numbers = 30  # Número de posições ocupadas pelas embarcações

# Listas vazias para armazenar os contadores de acertos na função contador()
cont_p1, cont_p2 = [] , []
cont_n11, cont_n12, cont_n21, cont_n22 = [], [], [], []
cont_t11, cont_t12, cont_t13, cont_t21, cont_t22, cont_t23 = [], [], [], [], [], []
cont_s11, cont_s12, cont_s13, cont_s14, cont_s21, cont_s22, cont_s23, cont_s24 = [], [], [], [], [], [], [], []

def contador(jogador, embarcação): # função para indicar se afundou alguma embarcação
    if jogador == "JOGADOR_1": 
        if embarcação == 'P':
            cont_p1.append(embarcação) # coloca o identificador da embarcação acertada numa lista
            cp1 = ''.join(cont_p1) # passa a lista para string
            if cp1 == 'PPPPP' : print("Você afundou meu porta-avião") # imprime quando alcançar a quantidade

        elif embarcação == 'N1':
            cont_n11.append(embarcação)
            cn11 = ''.join(cont_n11)
            if cn11 == 'N1N1N1N1' : print("Você afundou meu navio-tanque")

        elif embarcação == 'N2':
            cont_n12.append(embarcação)
            cn12 = ''.join(cont_n12)
            if cn12 == 'N2N2N2N2' : print("Você afundou meu navio-tanque")

        elif embarcação == 'T3':
            cont_t11.append(embarcação)
            ct11 = ''.join(cont_t11)
            if ct11 == 'T3T3T3' : print("Você afundou meu contratorpedeiro")

        elif embarcação == 'T4':
            cont_t12.append(embarcação)
            ct12 = ''.join(cont_t12)
            if ct12 == 'T4T4T4' : print("Você afundou meu contratorpedeiro")

        elif embarcação == 'T5':
            cont_t13.append(embarcação)
            ct13 = ''.join(cont_t13)
            if ct13 == 'T5T5T5' : print("Você afundou meu contratorpedeiro")

        elif embarcação == 'S6':
            cont_s11.append(embarcação)
            cs11 = ''.join(cont_s11) 
            if cs11 == 'S6S6' : print("Você afundou meu submarino") 

        elif embarcação == 'S7':
            cont_s12.append(embarcação)
            cs12 = ''.join(cont_s12) 
            if cs12 == 'S7S7' : print("Você afundou meu submarino") 

        elif embarcação == 'S8':
            cont_s13.append(embarcação)
            cs13 = ''.join(cont_s13) 
            if cs13 == 'S8S8' : print("Você afundou meu submarino") 

        elif embarcação == 'S9':
            cont_s14.append(embarcação)
            cs14 = ''.join(cont_s14) 
            if cs14 == 'S9S9' : print("Você afundou meu submarino") 

    elif jogador == "JOGADOR_2": 
        if embarcação == 'P':   
            cont_p2.append(embarcação)
            cp2 = ''.join(cont_p2) 
            if cp2 == 'PPPPP' : print("Você afundou meu porta-avião")

        elif embarcação == 'N1':
            cont_n21.append(embarcação)
            cn21 = ''.join(cont_n21)
            if cn21 == 'N1N1N1N1' : print("Você afundou meu navio-tanque")

        elif embarcação == 'N2':
            cont_n22.append(embarcação)
            cn22 = ''.join(cont_n22)
            if cn22 == 'N2N2N2N2' : print("Você afundou meu navio-tanque")

        elif embarcação == 'T3':
            cont_t21.append(embarcação)
            ct21 = ''.join(cont_t21)
            if ct21 == 'T3T3T3' : print("Você afundou meu contratorpedeiro")

        elif embarcação == 'T4':
            cont_t22.append(embarcação)
            ct22 = ''.join(cont_t22)
            if ct22 == 'T4T4T4' : print("Você afundou meu contratorpedeiro")

        elif embarcação == 'T5':
            cont_t23.append(embarcação)
            ct23 = ''.join(cont_t23)
            if ct23 == 'T5T5T5' : print("Você afundou meu contratorpedeiro")

        elif embarcação == 'S6':
            cont_s21.append(embarcação)
            cs21 = ''.join(cont_s21) 
            if cs21 == 'S6S6' : print("Você afundou meu submarino") 

        elif embarcação == 'S7':
            cont_s22.append(embarcação)
            cs22 = ''.join(cont_s22) 
            if cs22 == 'S7S7' : print("Você afundou meu submarino") 

        elif embarcação == 'S8':
            cont_s23.append(embarcação)
            cs23 = ''.join(cont_s23) 
            if cs23 == 'S8S8' : print("Você afundou meu submarino") 

        elif embarcação == 'S9':
            cont_s24.append(embarcação)
            cs24 = ''.join(cont_s24) 
            if cs24 == 'S9S9' : print("Você afundou meu submarino") 

    return

def place_ship(board, ship_size, ship_id):
    # Gera coordenadas da embarcação
    x = random.randint(0, board_size - 1)
    y = random.randint(0, board_size - 1)
    
    # Gera a orientação da embarcação (horizontal or vertical)
    is_horizontal = random.choice([True, False])

    # Check if the ship can be placed at the randomly chosen coordinates
    if is_horizontal:
        if y + ship_size > board_size:
            return place_ship(board, ship_size, ship_id)
        for i in range(ship_size):
            if board[x][y + i] != '~':
                return place_ship(board, ship_size, ship_id)
    else:
        if x + ship_size > board_size:
            return place_ship(board, ship_size, ship_id)
        for i in range(ship_size):
            if board[x + i][y] != '~':
                return place_ship(board, ship_size, ship_id)

    # Coloca embarcação no tabuleiro
    if is_horizontal:
        for i in range(ship_size):
            if ship_size == 5: board[x][y + i] = 'P'
            elif ship_size == 4: 
                board[x][y + i] = ('N' + str(ship_id))  
            elif ship_size == 3: 
                board[x][y + i] = ('T' + str(ship_id))
            elif ship_size == 2: 
                board[x][y + i] = ('S' + str(ship_id))
                                    
    else:
        for i in range(ship_size):
            if ship_size == 5: board[x + i][y] = 'P'
            elif ship_size == 4: 
                board[x + i][y] = ('N' + str(ship_id))
            elif ship_size == 3: 
                board[x + i][y] = ('T' + str(ship_id))
            elif ship_size == 2: 
                board[x + i][y] = ('S' + str(ship_id))
                               
    return board

def user_guess(remaining_ships, jogador, board, board_o):
    if remaining_ships == 0: return remaining_ships # Testa se ainda restam posições ocupadas, se não tiver retorna remaining_ships == 0 

    else:
        guess_x = int(input(jogador + " Enter the row (1 to 10): ")) -1
        letrasParaNumeros = {'A':1, 'B':2, 'C':3, 'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10}
        guess_y = int(letrasParaNumeros[((input(jogador + " Enter the column (A to J): ")).upper())]) -1
        
    if  (board[guess_x][guess_y] == 'S6') or (board[guess_x][guess_y] == 'S7') or (board[guess_x][guess_y] == 'S8') or (board[guess_x][guess_y] == 'S9'):
        print(jogador + " Hit!")
        embarcação = board[guess_x][guess_y] # Armazena o identificador da embarcação atingida
        board[guess_x][guess_y] = 'X'
        board_o[guess_x][guess_y] = 'X'
        remaining_ships -= 1
        contador(jogador, embarcação)
        display_board(board_o, jogador)
        return user_guess(remaining_ships, jogador, board, board_o)

    elif (board[guess_x][guess_y] == 'T3') or (board[guess_x][guess_y] == 'T4') or (board[guess_x][guess_y] == 'T5'):
        print(jogador + " Hit!")
        embarcação = board[guess_x][guess_y]
        board[guess_x][guess_y] = 'X'
        board_o[guess_x][guess_y] = 'X'
        remaining_ships -= 1
        contador(jogador, embarcação)
        display_board(board_o, jogador)
        return user_guess(remaining_ships, jogador, board, board_o)
    
    elif (board[guess_x][guess_y] == 'N1') or (board[guess_x][guess_y] == 'N2'):
        print(jogador + " Hit!")
        embarcação = board[guess_x][guess_y]
        board[guess_x][guess_y] = 'X'
        board_o[guess_x][guess_y] = 'X'
        remaining_ships -= 1
        contador(jogador, embarcação)
        display_board(board_o, jogador)
        return user_guess(remaining_ships, jogador, board, board_o)
    
    elif (board[guess_x][guess_y] == 'P'):
        print(jogador + " Hit!")
        embarcação = board[guess_x][guess_y] 
        board[guess_x][guess_y] = 'X'
        board_o[guess_x][guess_y] = 'X'
        remaining_ships -= 1
        contador(jogador, embarcação)
        display_board(board_o, jogador)
        return user_guess(remaining_ships, jogador, board, board_o)
        
    elif board[guess_x][guess_y] == 'X' or board[guess_x][guess_y] == '*':
        print(jogador + " You've already guessed this position.")
        display_board(board_o, jogador)
        return user_guess(remaining_ships, jogador, board, board_o)
       
    else:
        print(jogador + " Miss!")
        board[guess_x][guess_y] = '*'
        board_o[guess_x][guess_y] = '*'
        return remaining_ships

def display_board(board, jogador):
    num_linha = 1
    print("\nGuess Board: " + jogador + "\n")
    print('   A B C D E F G H I J')
    for row in board:
        if num_linha < 10:
            print("%d |%s" % (num_linha, " " .join(row)))
        else:
            print("%d|%s" % (num_linha, " " .join(row)))
        num_linha += 1
    return
        
ship_id = 0 # Id para cada embarcação criada
for size in ship_sizes:
    board_1 = place_ship(board_1, size, ship_id) # pega a tabela criada anteriormente e preenche com as embarcações no tabuleiro do Jogador 1
    ship_id += 1
    
ship_id = 0
for size in ship_sizes:
    board_2 = place_ship(board_2, size, ship_id) # tabuleiro do Jogador 2
    ship_id += 1
    
def main():

# Place all the ships on the board


    remaining_ships_1, remaining_ships_2 = ship_numbers, ship_numbers # Quantidade de posições ocupadas para cada jogador 

    # Display the guessing board
    display_board(board_o1, "JOGADOR_1")
    display_board(board_o2, "JOGADOR_2")

    #MOSTRA O TABULEIRO COM AS EMBARCAÇÕES | remover o # para visualizar as embarcações posicionadas
    #display_board(board_1, "JOGADOR_1")
    #display_board(board_2, "JOGADOR_2")


    while (remaining_ships_1 > 0) and (remaining_ships_2 > 0):
     
        # Take user input for the guess JOGADOR_1
        remaining_ships_1 = user_guess(remaining_ships_1, "JOGADOR_1", board_1, board_o1)
    
        # Display the guessing board JOGADOR_1
        display_board(board_o1, "JOGADOR_1")
        if remaining_ships_1 == 0 : break # Quando o jogador 1 afundar todos os navios ele volta pra testar e sair do loop     
    
        # Take user input for the guess JOGADOR_2
        remaining_ships_2 = user_guess(remaining_ships_2, "JOGADOR_2", board_2, board_o2)
        
        # Display the guessing board JOGADOR_2
        display_board(board_o2, "JOGADOR_2")

    print("Congratulations! You've sunk all the ships.")
    return

main()