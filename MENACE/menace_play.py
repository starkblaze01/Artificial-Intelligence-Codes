#! /usr/bin/env python3

from collections import Counter
import random
import json


class Board:
    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def __str__(self):
        return("\n 0 | 1 | 2     %s | %s | %s\n"
               "~~~|~~~|~~~   ~~~|~~~|~~~\n"
               " 3 | 4 | 5     %s | %s | %s\n"
               "~~~|~~~|~~~   ~~~|~~~|~~~\n"
               " 6 | 7 | 8     %s | %s | %s" % (self.board[0], self.board[1], self.board[2],
                                                self.board[3], self.board[4], self.board[5],
                                                self.board[6], self.board[7], self.board[8]))

    def valid_move(self, move):
        try:
            move = int(move)
        except ValueError:
            return False
        if 0 <= move <= 8 and self.board[move] == ' ':
            return True
        return False

    def winning(self):
        return ((self.board[0] != ' ' and
                 ((self.board[0] == self.board[1] == self.board[2]) or
                  (self.board[0] == self.board[3] == self.board[6]) or
                  (self.board[0] == self.board[4] == self.board[8])))
                or (self.board[4] != ' ' and
                    ((self.board[1] == self.board[4] == self.board[7]) or
                     (self.board[3] == self.board[4] == self.board[5]) or
                     (self.board[2] == self.board[4] == self.board[6])))
                or (self.board[8] != ' ' and
                    ((self.board[2] == self.board[5] == self.board[8]) or
                     (self.board[6] == self.board[7] == self.board[8]))))

    def draw(self):
        return all((x != ' ' for x in self.board))

    def play_move(self, position, marker):
        self.board[position] = marker

    def board_string(self):
        return ''.join(self.board)


class MenacePlayer:
    def __init__(self):
        self.matchboxes = {}
        self.num_win = 0
        self.num_draw = 0
        self.num_lose = 0

    def start_game(self):
        self.moves_played = []

    def get_move(self, board):
        # Find board in matchboxes and choose a bead
        # If the matchbox is empty, return -1 (resign)
        board = board.board_string()
        if board not in self.matchboxes:
            new_beads = [pos for pos, mark in enumerate(board) if mark == ' ']
            # Early boards start with more beads
            self.matchboxes[board] = new_beads * ((len(new_beads) + 2) // 2)

        beads = self.matchboxes[board]
        if len(beads):
            bead = random.choice(beads)
            self.moves_played.append((board, bead))
        else:
            bead = -1
        return bead

    def win_game(self):
        # We won, add three beads
        for (board, bead) in self.moves_played:
            self.matchboxes[board].extend([bead, bead, bead])
        self.num_win += 1

    def draw_game(self):
        # A draw, add one bead
        for (board, bead) in self.moves_played:
            self.matchboxes[board].append(bead)
        self.num_draw += 1

    def lose_game(self):
        # Lose, remove a bead
        for (board, bead) in self.moves_played:
            matchbox = self.matchboxes[board]
            del matchbox[matchbox.index(bead)]
        self.num_lose += 1

    def print_stats(self):
        print('Have learnt %d boards' % len(self.matchboxes))
        print('Number of Wins: %d' % (self.num_win))
        print('Number of Draws: %d' % (self.num_draw))
        print('Number of Losses: %d' % (self.num_lose))

    def store_data(self, name):
        print(self.matchboxes)
        with open("data"+name+".json", "w") as write_file:
            json.dump(self.matchboxes, write_file)

    def print_probability(self, board):
        board = board.board_string()
        try:
            print("Stats for this board: " +
                  str(Counter(self.matchboxes[board]).most_common()))
        except KeyError:
            print("Never seen this board before.")


class HumanPlayer:
    def __init__(self):
        pass

    def start_game(self):
        print("Get ready!")

    def get_move(self, board):
        while True:
            move = input('Make a move: ')
            if board.valid_move(move):
                break
            print("Not a valid move")
        return int(move)

    def win_game(self):
        print("You won!")

    def draw_game(self):
        print("It's a draw.")

    def lose_game(self):
        print("You lose.")

    def print_probability(self, board):
        pass


def play_game(first, second, silent=False):
    first.start_game()
    second.start_game()
    board = Board()

    if not silent:
        print("\n\nStarting a new game!")
        print(board)

    while True:
        if not silent:
            first.print_probability(board)
        move = first.get_move(board)
        if move == -1:
            if not silent:
                print("Player resigns")
            first.lose_game()
            second.win_game()
            break
        board.play_move(move, 'X')
        if not silent:
            print(board)
        if board.winning():
            first.win_game()
            second.lose_game()
            break
        if board.draw():
            first.draw_game()
            second.draw_game()
            break

        if not silent:
            second.print_probability(board)
        move = second.get_move(board)
        if move == -1:
            if not silent:
                print("Player resigns")
            second.lose_game()
            first.win_game()
            break
        board.play_move(move, 'O')
        if not silent:
            print(board)
        if board.winning():
            second.win_game()
            first.lose_game()
            break


if __name__ == '__main__':
    go_first_menace = MenacePlayer()
    go_second_menace = MenacePlayer()
    human = HumanPlayer()

    # Open json files and set the menace data
    with open("datafirst.json", "r") as first_file:
        first_data = json.load(first_file)
    first_file.close()
    with open("datasecond.json", "r") as second_file:
        second_data = json.load(second_file)
    second_file.close()

    go_first_menace.matchboxes = first_data
    go_second_menace.matchboxes = second_data
    play_game(go_first_menace, human)
    play_game(human, go_second_menace)
