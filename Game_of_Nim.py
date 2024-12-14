######################################################################
# Author: DieuMerci Nshizirungu
# Username: nshizirungud
#
#
#
# Purpose: A Tkinter-based interactive game of Nim allowing players to play against
# the computer or another player with configurable game settings such as difficulty level and starting number of balls.
#
#
#
######################################################################
# Acknowledgements: TA's Gagan Phuyal, HW07 Game of nim
#
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################


import tkinter as tk
from tkinter import messagebox
import random


class GameOfNim:
    def __init__(self):
        self.balls = 15
        self.current_player = "Player 1"
        self.opponent = "Computer"
        self.difficulty = "Easy"  # Default difficulty
        self.root = tk.Tk()
        self.root.title("Game of Nim")
        self.setup_menu()

    def setup_menu(self):     # setting up the main menu
        self.clear_screen()
        tk.Label(self.root, text="Welcome to the Game of Nim!", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Player vs Computer (Easy)", command=self.start_easy_mode, width=25).pack(pady=10)
        tk.Button(self.root, text="Player vs Computer (Hard)", command=self.start_hard_mode, width=25).pack(pady=10)
        tk.Button(self.root, text="Player vs Player", command=self.start_player_vs_player, width=25).pack(pady=10)

    def start_easy_mode(self):
        self.opponent = "Computer"
        self.difficulty = "Easy"
        self.get_starting_balls()

    def start_hard_mode(self):
        self.opponent = "Computer"
        self.difficulty = "Hard"

        self.get_starting_balls()

    def start_player_vs_player(self):
        self.opponent = "Player 2"
        self.get_starting_balls()

    def get_starting_balls(self):    # prompt for user to set the starting balls
        self.clear_screen()
        tk.Label(self.root, text="How many balls would you like to start with (min 15)?").pack(pady=10)
        self.starting_balls_entry = tk.Entry(self.root, highlightthickness="2", highlightcolor="blue",
                                             highlightbackground="black")
        self.starting_balls_entry.pack(pady=10)
        tk.Button(self.root, text="Submit", command=self.set_starting_balls).pack(pady=10)

    def set_starting_balls(self):
        try:
            balls = int(self.starting_balls_entry.get())
            if balls < 15:
                raise ValueError("Minimum 15 balls required.")
            self.balls = balls
            self.start_game()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of balls (minimum 15).")

    def start_game(self):
        """Set up the game interface."""
        self.clear_screen()
        self.update_game_ui()

    def create_ball_display(self, parent):      # creates the display for the balls
        ball_frame = tk.Frame(parent)
        ball_frame.pack(pady=10)

        # Create ball circles
        self.ball_circles = []
        for _ in range(self.balls):
            ball = tk.Canvas(ball_frame, width=30, height=30, bg='white', highlightthickness=0)
            ball.create_oval(5, 5, 25, 25, fill='blue', tags='ball')
            ball.pack(side=tk.LEFT, padx=2)
            self.ball_circles.append(ball)

    def update_game_ui(self):          # Updates the games interface with the current state of the game
        self.clear_screen()

        # Game state labels
        tk.Label(self.root, text=f"Balls Remaining: {self.balls}", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text=f"{self.current_player}'s Turn", font=("Arial", 14)).pack(pady=10)

        # Ball display
        self.create_ball_display(self.root)

        # Input and submit
        tk.Label(self.root, text="Pick 1-4 Balls:").pack()
        self.pick_entry = tk.Entry(self.root, highlightthickness="2", highlightcolor="blue",
                                   highlightbackground="black")
        self.pick_entry.pack(pady=5)
        tk.Button(self.root, text="Submit", command=self.process_player_turn).pack(pady=10)

    def process_player_turn(self):     # processes the players turn
        try:
            player_balls = int(self.pick_entry.get())
            if player_balls < 1 or player_balls > 4 or player_balls > self.balls:
                raise ValueError

            # Remove balls from visual display
            for _ in range(player_balls):
                if self.ball_circles:
                    self.ball_circles.pop().destroy()

            self.balls -= player_balls
            if self.balls == 0:
                messagebox.showinfo("Game Over", f"{self.current_player} Wins!")
                self.setup_menu()
            else:
                self.switch_turn()
        except ValueError:
            messagebox.showerror("Error", "Pick a valid number of balls (1-4, and not more than remaining balls).")

    def computer_turn(self):        # allows the computer to play
        if self.difficulty == "Easy":
            computer_balls = random.randint(1, min(4, self.balls))
        else:  # Hard difficulty
            computer_balls = self.balls % 5 or random.randint(1, min(4, self.balls))

        # Remove balls from visual display
        for _ in range(computer_balls):
            if self.ball_circles:
                self.ball_circles.pop().destroy()

        self.balls -= computer_balls
        messagebox.showinfo("Computer's Turn", f"Computer picked {computer_balls} balls.")
        if self.balls == 0:
            messagebox.showinfo("Game Over", "Computer Wins!")
            self.setup_menu()
        else:
            self.current_player = "Player 1"
            self.update_game_ui()

    def switch_turn(self):
        if self.current_player == "Player 1" and self.opponent == "Computer":  # switches turns between players
            self.computer_turn()
        else:
            self.current_player = "Player 2" if self.current_player == "Player 1" else "Player 1"
            self.update_game_ui()

    def clear_screen(self):
        for widget in self.root.winfo_children():  # removes widgets from the screen
            widget.destroy()


def main():
    game = GameOfNim()
    game.root.mainloop()


if __name__ == "__main__":
    main()
