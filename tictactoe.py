
"""
Tic Tac Toe game with GUI using tkinter.

This script allows users to play Tic Tac Toe in single-player 
(against computer) or multiplayer mode.
It features a graphical interface, win/tie detection, and computer AI for single-player mode.

Functions:
	winner(b, l): Check if a player has won.
	get_text(i, j, gb, l1, l2): Handle player moves in multiplayer mode.
	isfree(i, j): Check if a cell is free.
	isfull(): Check if the board is full.
	gameboard_pl(game_board, l1, l2): Create multiplayer game board.
	pc(): Decide computer's next move.
	get_text_pc(i, j, gb, l1, l2): Handle moves in single-player mode.
	gameboard_pc(game_board, l1, l2): Create single-player game board.
	withpc(game_board): Start single-player game.
	withplayer(game_board): Start multiplayer game.
	play(): Main menu and game launcher.
"""


# Standard library imports
import random
from functools import partial
from copy import deepcopy

# Third-party imports
from tkinter import Tk, Button, DISABLED, ACTIVE, messagebox

class TicTacToeGame:
    """
    A class representing a Tic Tac Toe game with both single-player and multiplayer modes.

    This class manages the game state, handles player moves, provides computer AI for 
    single-player mode, and manages the graphical interface using tkinter. It supports 
    both player vs player and player vs computer gameplay modes.

    Attributes:
        board (list): 3x3 game board representing the current game state
        sign (int): Counter to track player turns (even=X, odd=O)
        button (list): 2D list of tkinter Button widgets for the game board GUI
    """

    def __init__(self):
        """Initialize an empty game board and turn counter."""
        # Creates an empty board
        self.board = [[" " for x in range(3)] for y in range(3)]
        # Turn counter: even=X's turn, odd=O's turn
        self.sign = 0
        # Will store the GUI buttons
        self.button = None
        # Flag to indicate if the game should stop (for single-player mode)
        self.stop_game = False

    def winner(self, l, board=None):
        """
        Check if player l ('X' or 'O') has won the game.

        Args:
            l (str): The player's symbol ('X' or 'O').
            board (list, optional): The board to check. Defaults to self.board.
        Returns:
            bool: True if the player has won, False otherwise.
        """
        b = board if board is not None else self.board
        return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
                (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
                (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
                (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
                (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
                (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
                (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
                (b[0][2] == l and b[1][1] == l and b[2][0] == l))

    def handle_multiplayer_move(self, i, j, gb, l1, l2):
        """
        Handle a player's move in multiplayer mode, update board and check for win/tie.

        Args:
            i (int): Row index.
            j (int): Column index.
            gb: Game board window.
            l1: Player 1 label/button.
            l2: Player 2 label/button.
        """
        if self.board[i][j] == ' ':
            if self.sign % 2 == 0:
                l1.config(state=DISABLED)
                l2.config(state=ACTIVE)
                self.board[i][j] = "X"
            else:
                l2.config(state=DISABLED)
                l1.config(state=ACTIVE)
                self.board[i][j] = "O"
            self.sign += 1
            self.button[i][j].config(text=self.board[i][j])

        if self.winner("X"):
            gb.destroy()
            messagebox.showinfo("Winner", "Player 1 won the match")
        elif self.winner("O"):
            gb.destroy()
            messagebox.showinfo("Winner", "Player 2 won the match")
        elif self.is_full():
            gb.destroy()
            messagebox.showinfo("Tie Game", "Tie Game")

    def is_free(self, i, j):
        """
        Check if the cell at (i, j) is free.

        Args:
            i (int): Row index.
            j (int): Column index.
        Returns:
            bool: True if cell is free, False otherwise.
        """
        return self.board[i][j] == " "

    def is_full(self):
        """
        Check if the board is full (no empty spaces).

        Returns:
            bool: True if board is full, False otherwise.
        """
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def create_multiplayer_board(self, game_board, l1, l2):
        """
        Create the multiplayer game board GUI.

        Args:
            game_board: The main game window.
            l1: Player 1 label/button.
            l2: Player 2 label/button.
        """
        self.button = []
        for i in range(3):
            m = 3+i
            self.button.append([])
            for j in range(3):
                get_t = partial(self.handle_multiplayer_move, i, j, game_board, l1, l2)
                self.button[i].append(
                    Button(
                        game_board, 
                        bd=5, 
                        command=get_t, 
                        height=4, 
                        width=8
                    )
                )
                self.button[i][j].grid(row=m, column=j)
        game_board.mainloop()

    def get_computer_move(self):
        """
        Decide the computer's next move using basic AI.
        
        The AI follows these rules in order:
        1. Win if possible
        2. Block opponent's win
        3. Take center if free
        4. Take a corner if free
        5. Take any edge

        Returns:
            list: The [row, col] of the next move, or None if no moves left.
        """
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    possible_moves.append([i, j])

        if not possible_moves:
            return None
     
        # Check for winning move or blocking opponent's win
        for symbol in ['O', 'X']:
            for move in possible_moves:
                board_copy = deepcopy(self.board)
                board_copy[move[0]][move[1]] = symbol
                if self.winner(symbol, board_copy):
                    return move
                    
        # Take center if available
        if [1, 1] in possible_moves:
            return [1, 1]
            
        # Take corners
        corners = [move for move in possible_moves 
                  if move in [[0, 0], [0, 2], [2, 0], [2, 2]]]
        if corners:
            return corners[random.randint(0, len(corners)-1)]
            
        # Take edges
        edges = [move for move in possible_moves 
                if move in [[0, 1], [1, 0], [1, 2], [2, 1]]]
        if edges:
            return edges[random.randint(0, len(edges)-1)]
            
        return None

    def handle_singleplayer_move(self, i, j, gb, l1, l2):
        """
        Handle a move in single-player mode, update board, check for win/tie, and trigger computer move.

        Args:
            i (int): Row index.
            j (int): Column index.
            gb: Game board window.
            l1: Player label/button.
            l2: Computer label/button.
        """
        if self.board[i][j] == ' ' and not self.stop_game:
            # Player's move
            if self.sign % 2 == 0:
                l1.config(state=DISABLED)
                l2.config(state=ACTIVE)
                self.board[i][j] = "X"
                self.button[i][j].config(text="X")
                self.sign += 1

                # Check if player won or game is tied
                if self.winner("X"):
                    gb.destroy()
                    messagebox.showinfo("Winner", "Player won the match")
                    return
                elif self.is_full():
                    gb.destroy()
                    messagebox.showinfo("Tie Game", "Tie Game")
                    return

                # Computer's move
                move = self.get_computer_move()
                if move:
                    self.button[move[0]][move[1]].config(state=DISABLED)
                    self.board[move[0]][move[1]] = "O"
                    self.button[move[0]][move[1]].config(text="O")
                    self.sign += 1
                    
                    # Check if computer won
                    if self.winner("O"):
                        gb.destroy()
                        messagebox.showinfo("Winner", "Computer won the match")

    def create_singleplayer_board(self, game_board, l1, l2):
        """
        Create the single-player game board GUI.

        Args:
            game_board: The main game window.
            l1: Player label/button.
            l2: Computer label/button.
        """
        self.button = []
        for i in range(3):
            m = 3+i
            self.button.append([])
            for j in range(3):
                get_t = partial(self.handle_singleplayer_move, i, j, game_board, l1, l2)
                self.button[i].append(
                    Button(
                        game_board,
                        bd=5,
                        command=get_t,
                        height=4,
                        width=8
                    )
                )
                self.button[i][j].grid(row=m, column=j)
        game_board.mainloop()

    # Game initialization methods


    def start_singleplayer(self, menu):
        """
        Initialize and start a single-player game against the computer.

        Args:
            menu: The main menu window.
        """
        menu.destroy()
        game_board = Tk()
        game_board.title("Tic Tac Toe")
        
        # Create player buttons/labels
        l1 = Button(game_board, text="Player : X", width=10)
        l1.grid(row=1, column=1)
        l2 = Button(game_board, text="Computer : O", width=10, state=DISABLED)
        l2.grid(row=2, column=1)
        
        # Initialize game board
        self.create_singleplayer_board(game_board, l1, l2)

    # Initialize the game board for multiplayer mode


    def start_multiplayer(self, menu):
        """
        Initialize and start a multiplayer game.

        Args:
            menu: The main menu window.
        """
        menu.destroy()
        game_board = Tk()
        game_board.title("Tic Tac Toe")
        
        # Create player buttons/labels
        l1 = Button(game_board, text="Player 1 : X", width=10)
        l1.grid(row=1, column=1)
        l2 = Button(game_board, text="Player 2 : O", width=10, state=DISABLED)
        l2.grid(row=2, column=1)
        
        # Initialize game board
        self.create_multiplayer_board(game_board, l1, l2)

    def start_game(self):
        """
        Launch the main menu and handle user selection for game mode or exit.
        """
        menu = Tk()
        menu.geometry("250x250")
        menu.title("Tic Tac Toe")

        # Create menu buttons
        head = Button(menu,
                    text="---Welcome to tic-tac-toe---",
                    activeforeground='red',
                    activebackground="yellow",
                    bg="red",
                    fg="yellow",
                    width=500,
                    font='summer',
                    bd=5)

        B1 = Button(menu,
                    text="Single Player",
                    command=lambda: self.start_singleplayer(menu),
                    activeforeground='red',
                    activebackground="yellow",
                    bg="red",
                    fg="yellow",
                    width=500,
                    font='summer',
                    bd=5)

        B2 = Button(menu,
                    text="Multi Player",
                    command=lambda: self.start_multiplayer(menu),
                    activeforeground='red',
                    activebackground="yellow",
                    bg="red",
                    fg="yellow",
                    width=500,
                    font='summer',
                    bd=5)

        B3 = Button(menu,
                    text="Exit",
                    command=menu.quit,
                    activeforeground='red',
                    activebackground="yellow",
                    bg="red",
                    fg="yellow",
                    width=500,
                    font='summer',
                    bd=5)

        # Pack buttons in order
        head.pack(side='top')
        B1.pack(side='top')
        B2.pack(side='top')
        B3.pack(side='top')

        menu.mainloop()


# Initialize and start game
if __name__ == '__main__':
    game = TicTacToeGame()
    game.start_game()
