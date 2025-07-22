
"""
Tic Tac Toe game with GUI interface.

This script allows two players to play Tic Tac Toe on a 3x3 grid.
It features a graphical interface, win/tie detection, and alternating turns.
"""
# Importing Packages from tkinter
from tkinter import Button, messagebox, Tk
# Initialize the game board buttons
b = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Initialize the game state
states = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

class TicTacToe:
    """
    A class representing a Tic Tac Toe game with a graphical interface.

    This class manages the game state, handles player moves, and checks for win/tie conditions.
    It uses tkinter buttons for the game board and displays message boxes for game outcomes.

    Attributes:
        current_player (str): The symbol ('X' or 'O') of the current player.
        stop_game (bool): Flag indicating whether the game has ended.
    """
    def __init__(self):
        self.current_player = 'X'
        self.stop_game = False

    def clicked(self, r, c):
        """
        Handle a player's move, update the board, and check for a win or tie.

        Args:
            r (int): Row index.
            c (int): Column index.
        """
        if self.current_player == "X" and states[r][c] == 0 and not self.stop_game:
            b[r][c].configure(text="X")
            states[r][c] = 'X'
            self.current_player = 'O'

        if self.current_player == 'O' and states[r][c] == 0 and not self.stop_game:
            b[r][c].configure(text='O')
            states[r][c] = "O"
            self.current_player = "X"

        self.check_if_win()

    def check_if_win(self):
        """
        Check for a win or tie after each move and display a message box if the game ends.
        """

        # Check rows
        for row in range(3):
            if states[row][0] == states[row][1] == states[row][2] != 0:
                self.stop_game = True
                messagebox.showinfo("Winner", states[row][0] + " Won!")
                return

            # Check columns
            if states[0][row] == states[1][row] == states[2][row] != 0:
                self.stop_game = True
                messagebox.showinfo("Winner", states[0][row] + " Won!")
                return

        # Check diagonals
        if states[0][0] == states[1][1] == states[2][2] != 0:
            self.stop_game = True
            messagebox.showinfo("Winner", states[0][0] + " Won!")
            return

        if states[0][2] == states[1][1] == states[2][0] != 0:
            self.stop_game = True
            messagebox.showinfo("Winner", states[0][2] + " Won!")
            return

        # Check for tie
        if all(states[x][y] != 0 for x in range(3) for y in range(3)):
            self.stop_game = True
            messagebox.showinfo("Tie", "It's a tie!")

# Initialize game
game = TicTacToe()

# Design window
#Creating the Canvas
root = Tk()
# Title of the window
root.title("GeeksForGeeks-:Tic Tac Toe")
root.resizable(0,0)

#Button
b = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]

#text for buttons
states = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]

# Create buttons
for i in range(3):
    for j in range(3):
        b[i][j] = Button(
            height=4, width=8,
            font=("Helvetica", "20"),
            command=lambda r=i, c=j: game.clicked(r, c)
        )
        b[i][j].grid(row=i, column=j)


root.mainloop()
