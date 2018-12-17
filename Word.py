import Settings

from vnl import rbnode,rbtree

abc = rbtree()

if Settings.dictionary1 == 1:
    with open("dic.txt") as f:
        content = f.read().split()
    for i in range(0, 178690):
        abc.insert_key(content[i])

else:
    with open("dicrom.txt") as f:
        content = f.read().split()
    for i in range(0,75338):
        abc.insert_key(content[i])


class Word:
    def __init__(self, word, location, player, direction, board):
        self.word = word
        self.word.upper()
        self.location = location
        self.player = player
        self.direction = direction.lower()
        self.board = board

    def check_word(self):
        word_score = 0

        current_board_ltr = ""
        needed_tiles = ""
        blank_tile_val = ""

        if self.word != "":

            if "#" in self.word:
                while len(blank_tile_val) != 1:
                    blank_tile_val = input("Please enter the letter value of the blank tile: ")
                self.word = self.word[:self.word.index("#")] + blank_tile_val.upper() + self.word[(self.word.index("#")+1):]

            if self.direction == "right":
                for i in range(len(self.word)):
                    if self.board[self.location[0]][self.location[1]+i][1] == " " or self.board[self.location[0]][self.location[1]+i] == "TLS" or self.board[self.location[0]][self.location[1]+i] == "TWS" or self.board[self.location[0]][self.location[1]+i] == "DLS" or self.board[self.location[0]][self.location[1]+i] == "DWS" or self.board[self.location[0]][self.location[1]+i][1] == "*":
                        current_board_ltr += " "
                        v = len(current_board_ltr)
                    else:
                        current_board_ltr += self.board[self.location[0]][self.location[1]+i][1]
            elif self.direction == "down":
                for i in range(len(self.word)):
                    if self.board[self.location[0]+i][self.location[1]] == "   " or self.board[self.location[0]+i][self.location[1]] == "TLS" or self.board[self.location[0]+i][self.location[1]] == "TWS" or self.board[self.location[0]+i][self.location[1]] == "DLS" or self.board[self.location[0]+i][self.location[1]] == "DWS" or self.board[self.location[0]+i][self.location[1]] == " * ":
                        current_board_ltr += " "
                    else:
                        current_board_ltr += self.board[self.location[0]+i][self.location[1]][1]
            else:
                return "Error: please enter a valid direction."
            if (not abc.search(self.word)):
                return "Please enter a valid dictionary word.\n"

            for i in range(len(self.word)):
                if current_board_ltr[i] == " ":
                    needed_tiles += self.word[i]
                elif current_board_ltr[i] != self.word[i]:
                    print("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + self.word + ", Needed_Tiles: " + needed_tiles)
                    return "The letters do not overlap correctly, please choose another word."

            if blank_tile_val != "":
                needed_tiles = needed_tiles[needed_tiles.index(blank_tile_val):] + needed_tiles[:needed_tiles.index(blank_tile_val)]
            if (Settings.round_number!=0):
                print("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + self.word + ", Needed_Tiles: " + needed_tiles)
                return "Please connect the word to a previously played letter."

            for letter in needed_tiles:
                if letter.upper() not in self.player.get_rack_str() or self.player.get_rack_str().count(letter.upper()) < needed_tiles.count(letter):
                    return "You do not have the tiles for this word\n"

            if self.location[0] > 14 or self.location[1] > 14 or self.location[0] < 0 or self.location[1] < 0 or (self.direction == "down" and (self.location[0]+len(self.word)-1) > 14) or (self.direction == "right" and (self.location[1]+len(self.word)-1) > 14):
                return "Location out of bounds.\n"

            if Settings.round_number == 1 and Settings.players[0] == self.player and self.location != [7,7]:
                return "The first turn must begin at location (7, 7).\n"
            return True

        else:
            if input("Are you sure you would like to skip your turn? (y/n)").upper() == "Y" or input("Are you sure you would like to skip your turn? (y/n)").upper() =="":
                return True
            else:
                return "Please enter a word."

    def calculate_word_score(self):
        premium_spots = []
        word_score = 0
        for letter in self.word:
            for spot in premium_spots:
                if letter == spot[0]:
                    if spot[1] == "TLS":
                        word_score += Settings.LETTER_VALUES[letter] * 2
                    elif spot[2] == "DLS":
                        word_score +=Settings.LETTER_VALUES[letter]
            word_score += Settings.LETTER_VALUES[letter]
        for spot in premium_spots:
            if spot[1] == "TWS":
                word_score *= 3
            elif spot[1] == "DWS":
                word_score *= 2
        self.player.increase_score(word_score)

    def set_word(self, word):
        self.word = word

    def set_location(self, location):
        self.location = location

    def set_direction(self, direction):
        self.direction = direction

    def get_word(self):
        return self.word