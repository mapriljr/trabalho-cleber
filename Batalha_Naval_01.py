# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 20:24:57 2023

Autores: Brenda, Cleber, Marcus e Rayssa   # depois vamos colocar os nomes completos...

"""
import random

board_size = 10  # escolha do tamanho do tabuleiro

# criação dos tabuleiros vazios (os dois primeiros é onde o jogo efetivamente ocorre, os dois seguintes são os que
# são visualizados pelos jogadores e mostram os resultados dos "disparos" contra o adversário)

board_1 = [['~' for i in range(board_size)] for j in range(board_size)]
board_2 = [['~' for i in range(board_size)] for j in range(board_size)]

board_o1 = [['~' for i in range(board_size)] for j in range(board_size)]
board_o2 = [['~' for i in range(board_size)] for j in range(board_size)]

ship_sizes = [5, 4, 4, 3, 3, 3, 2, 2, 2, 2]  # registra os tamanhos de cada embarcação (um porta-aviões, dois navios-tanque, três contratorpedeiros e quatro submarinos)

ship_numbers = len(ship_sizes)  # número total de navios

#pa = '1'
#nt = '2'
#ct = '3'
#sm = '4'

    # Place all the ships on the board
#for size in ship_sizes:
#    board_1 = place_ship(board_1, size)

#for size in ship_sizes:
#    board_2 = place_ship(board_2, size)



def place_ship(board, ship_size, nt, ct, sm):
    # Gera coordenadas aleatórias para a posição inicial do navio
    x = random.randint(0, board_size - 1)
    y = random.randint(0, board_size - 1)
    
    # Gera aleatoriamente a orientação do navio (horizontal or vertical)
    is_horizontal = random.choice([True, False])

    # Controles para que os navios caibam no tabuleiro e para evitar colisões
    if is_horizontal:
        if y + ship_size > board_size:
            return place_ship(board, ship_size, nt, ct, sm)
        for i in range(ship_size):
            if board[x][y + i] != '~':
                return place_ship(board, ship_size, nt, ct, sm)
    else:
        if x + ship_size > board_size:
            return place_ship(board, ship_size, nt, ct, sm)
        for i in range(ship_size):
            if board[x + i][y] != '~':
                return place_ship(board, ship_size, nt, ct, sm)

    # Distribui os navios pelo tabuleiro
    if is_horizontal:
        for i in range(ship_size):
            if ship_size == 5: board[x][y + i] = 'P'  #entender melhor o posicionamento ... y+i???
            elif ship_size == 4: 
                board[x][y + i] = ('N' + nt)
            elif ship_size == 3: 
                board[x][y + i] = ('T' + ct)
            elif ship_size == 2: 
                board[x][y + i] = ('S' + sm)
            #board[x][y + i] = 'S'
            #nt = str((int(nt)) - 1)
            #print(nt)
            #ct = str((int(ct)) - 1)
            #print(ct)
            #sm = str((int(sm)) - 1)
            #print(sm)
                        
    else:
        for i in range(ship_size):
            if ship_size == 5: board[x + i][y] = 'P'
            elif ship_size == 4: 
                board[x + i][y] = ('N' + nt)
            elif ship_size == 3: 
                board[x + i][y] = ('T' + ct)
            elif ship_size == 2: 
                board[x + i][y] = ('S' + sm)
            #board[x + i][y] = 'S'
            #nt = str((int(nt)) - 1)
            #print(nt)
            #ct = str((int(ct)) - 1)
            #print(ct)
            #sm = str((int(sm)) - 1)
            #print(sm)
           
    return board

def user_guess(remaining_ships, jogador, board, board_o):
    guess_x = int(input(jogador + " Enter the row (1 to 10): ")) -1
    letrasParaNumeros = {'A':1, 'B':2, 'C':3, 'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10}
    guess_y = int(letrasParaNumeros[((input(jogador + " Enter the column (A to J): ")).upper())]) -1

    if  (board[guess_x][guess_y] == 'S1') or  (board[guess_x][guess_y] == 'S2') or  (board[guess_x][guess_y] == 'S3') or  (board[guess_x][guess_y] == 'S4'):
        print(jogador + " Hit!")
        board[guess_x][guess_y] = 'X'
        board_o[guess_x][guess_y] = 'X'
        remaining_ships -= 1
        display_board(board_o, jogador)
        return user_guess(remaining_ships, jogador, board, board_o)

    elif (board[guess_x][guess_y] == 'T1') or (board[guess_x][guess_y] == 'T2') or (board[guess_x][guess_y] == 'T3'):
        print(jogador + " Hit!")
        board[guess_x][guess_y] = 'X'
        board_o[guess_x][guess_y] = 'X'
        remaining_ships -= 1
        display_board(board_o, jogador)
        return user_guess(remaining_ships, jogador, board, board_o)
    
    elif (board[guess_x][guess_y] == 'N1') or (board[guess_x][guess_y] == 'N2'):
        print(jogador + " Hit!")
        board[guess_x][guess_y] = 'X'
        board_o[guess_x][guess_y] = 'X'
        remaining_ships -= 1
        display_board(board_o, jogador)
        return user_guess(remaining_ships, jogador, board, board_o)
    
    elif (board[guess_x][guess_y] == 'P'):
        print(jogador + " Hit!")
        board[guess_x][guess_y] = 'X'
        board_o[guess_x][guess_y] = 'X'
        remaining_ships -= 1
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
        return


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
    
    
for size in ship_sizes:
    nt = '2'
    ct = '3'
    sm = '4'
    board_1 = place_ship(board_1, size, nt, ct, sm)
    
for size in ship_sizes:
    nt = '2'
    ct = '3'
    sm = '4'
    board_2 = place_ship(board_2, size, nt, ct, sm)
    #nt = str(int(nt) - 1)
    #ct = str(int(ct) - 1)
    #sm = str(int(sm) - 1)



# def main():

# # Place all the ships on the board

    

#     remaining_ships = ship_numbers

#     # Display the guessing board
#     display_board(board_o1, "JOGADOR_1")
#     display_board(board_o2, "JOGADOR_2")

#     #MOSTRA O TABULEIRO COM AS EMBARCAÇÕES
#     #display_board(board_1, "JOGADOR_1")
#     #display_board(board_2, "JOGADOR_2")


#     while remaining_ships > 0:
#         # Display the guessing board
     
#         # Take user input for the guess JOGADOR_1
#         guess = user_guess(remaining_ships, "JOGADOR_1", board_1, board_o1)
    
#         # Display the guessing board JOGADOR_1
#         display_board(board_o1, "JOGADOR_1")    
    
#         # Take user input for the guess JOGADOR_2
#         guess = user_guess(remaining_ships, "JOGADOR_2", board_2, board_o2)
        
#         # Check the guessed position BOARD_2
      
#         # Display the guessing board JOGADOR_2
#         display_board(board_o2, "JOGADOR_2")

#     print("Congratulations! You've sunk all the ships.")
#     return

# main()