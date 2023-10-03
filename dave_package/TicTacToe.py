import itertools
import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i, j in itertools.product(range(3), range(3)):
            self.buttons[i][j] = tk.Button(self.window, text='', font=('normal', 24), width=8, height=2,
                                           command=lambda row=i, col=j: self.make_move(row, col))
            self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if winner := self.check_winner():
                self.end_game(winner)
            elif ' ' not in [cell for row in self.board for cell in row]:
                self.end_game('Draw')
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def end_game(self, winner):
        if winner == 'Draw':
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()
