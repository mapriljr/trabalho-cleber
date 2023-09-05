# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 05:39:59 2023

@author: mapjr
"""

from Batalha_Naval_0 import *



def main():

# Place all the ships on the board

    

    remaining_ships = ship_numbers

    # Display the guessing board
    display_board(board_o1, "JOGADOR_1")
    display_board(board_o2, "JOGADOR_2")

    #MOSTRA O TABULEIRO COM AS EMBARCAÇÕES
    display_board(board_1, "JOGADOR_1")
    display_board(board_2, "JOGADOR_2")


    while remaining_ships > 0:
        # Display the guessing board
     
        # Take user input for the guess JOGADOR_1
        guess = user_guess(remaining_ships, "JOGADOR_1", board_1, board_o1)
    
        # Display the guessing board JOGADOR_1
        display_board(board_o1, "JOGADOR_1")    
    
        # Take user input for the guess JOGADOR_2
        guess = user_guess(remaining_ships, "JOGADOR_2", board_2, board_o2)
        
        # Check the guessed position BOARD_2
      
        # Display the guessing board JOGADOR_2
        display_board(board_o2, "JOGADOR_2")

    print("Congratulations! You've sunk all the ships.")
    return


if __name__ == "__main__":
    main()