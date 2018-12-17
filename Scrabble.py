from Bag import Bag
from Player import Player
from Board import Board
from Word import Word
from SimpleLinkedList import Node, LinkedList
import Settings
def turn(player, board, bag):
    global round_number, players, skipped_turns
    skipped_turns = Settings.skipped_turns

    if (skipped_turns < 6) or (player.rack.get_rack_length() == 0 and bag.get_remaining_tiles() == 0):

        print("\nRound " + str(round_number) + ": " + player.get_name() + "'s turn \n")
        print(board.get_board())
        print("\n" + player.get_name() + "'s Letter Rack: " + player.get_rack_str())
        word_to_play = input("Word to play: ")
        location = []
        col = input("Column number: ")
        row = input("Row number ")
        if (col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
            location = [-1, -1]
        else:
            location = [int(row), int(col)]
        direction = input("Direction of word (right or down): ")

        word = Word(word_to_play, location, player, direction, board.board_array())

        while word.check_word() != True:
            print (word.check_word())
            word.set_word(input("Word to play: "))
            location = []
            col = input("Column number: ")
            row = input("Row number: ")
            if (col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
                location = [-1, -1]
            else:
                word.set_location([int(row), int(col)])
            word.set_direction(input("Direction of word (right or down): "))

        if word.get_word() == "":
            print("Your turn has been skipped.")
            skipped_turns += 1
        else:
            board.place_word(word_to_play, location, direction, player)
            word.calculate_word_score()
            skipped_turns = 0

        print("\n" + player.get_name() + "'s score is: " + str(player.get_score()))

        if players.index(player) != (len(players)-1):
            player = players[players.index(player)+1]
        else:
            player = players[0]
            round_number += 1

        turn(player, board, bag)

    else:
        end_game()

def start_game():
    global round_number, players, skipped_turns
    board = Board()
    bag = Bag()
    Settings.dictionary1 = int(input("For English Dictionary enter 1 for Romanian Dictionary enter 2: "))
    num_of_players = int(input("\nPlease enter the number of players (2-4): "))
    while num_of_players < 2 or num_of_players > 4:
        num_of_players = int(input("This number is invalid. Please enter the number of players (2-4): "))

    print("\nWelcome to Scrabble! Please enter the names of the players below ")
    players = []
    for i in range(num_of_players):
        players.append(Player(bag))
        players[i].set_name(input("Please enter player " + str(i+1) + "'s name: "))

    round_number = 1
    skipped_turns = 0
    current_player = players[0]
    turn(current_player, board, bag)

def end_game():
    global players
    highest_score = 0
    winning_player = ""
    for player in players:
        if player.get_score > highest_score:
            highest_score = player.get_score()
            winning_player = player.get_name()
    print("The game is over! " + player.get_name() + ", you have won!")

    if input("\nWould you like to play again? (y/n)").upper() == "Y":
        start_game()

start_game()
