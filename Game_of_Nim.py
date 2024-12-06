import tkinter as tk
from tkinter import messagebox
import random


class GameOfNim:
    def __init__(self):
        self.balls = 15
        self.current_player = "Player 1"
        self.opponent = "Computer"
        self.root = tk.Tk()
        self.root.title("Game of Nim")
        self.setup_menu()

    def setup_menu(self):
        """Set up the main menu."""
        self.clear_screen()
        tk.Label(self.root, text="Welcome to the Game of Nim!", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Player vs Computer", command=self.start_player_vs_computer, width=20).pack(pady=10)
        tk.Button(self.root, text="Player vs Player", command=self.start_player_vs_player, width=20).pack(pady=10)

    def start_player_vs_computer(self):
        self.opponent = "Computer"
        self.get_starting_balls()

    def start_player_vs_player(self):
        self.opponent = "Player 2"
        self.get_starting_balls()

    def get_starting_balls(self):
        """Prompt to set starting balls."""
        self.clear_screen()
        tk.Label(self.root, text="How many balls would you like to start with (min 15)?").pack(pady=10)
        self.starting_balls_entry = tk.Entry(self.root)
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

    def update_game_ui(self):
        """Update the interface with current game state."""
        self.clear_screen()
        tk.Label(self.root, text=f"Balls Remaining: {self.balls}", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text=f"{self.current_player}'s Turn", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Pick 1-4 Balls:").pack()
        self.pick_entry = tk.Entry(self.root)
        self.pick_entry.pack(pady=5)
        tk.Button(self.root, text="Submit", command=self.process_player_turn).pack(pady=10)

    def process_player_turn(self):
        """Process the player's turn."""
        try:
            player_balls = int(self.pick_entry.get())
            if player_balls < 1 or player_balls > 4 or player_balls > self.balls:
                raise ValueError
            self.balls -= player_balls
            if self.balls == 0:
                messagebox.showinfo("Game Over", f"{self.current_player} Wins!")
                self.setup_menu()
            else:
                self.switch_turn()
        except ValueError:
            messagebox.showerror("Error", "Pick a valid number of balls (1-4, and not more than remaining balls).")

    def computer_turn(self):
        """Let the computer play."""
        computer_balls = random.randint(1, min(4, self.balls))
        self.balls -= computer_balls
        messagebox.showinfo("Computer's Turn", f"Computer picked {computer_balls} balls.")
        if self.balls == 0:
            messagebox.showinfo("Game Over", "Computer Wins!")
            self.setup_menu()
        else:
            self.current_player = "Player 1"
            self.update_game_ui()

    def switch_turn(self):
        """Switch turns between players."""
        if self.current_player == "Player 1" and self.opponent == "Computer":
            self.computer_turn()
        else:
            self.current_player = "Player 2" if self.current_player == "Player 1" else "Player 1"
            self.update_game_ui()

    def clear_screen(self):
        """Remove all widgets from the screen."""
        for widget in self.root.winfo_children():
            widget.destroy()


def main():
    game = GameOfNim()
    game.root.mainloop()


if __name__ == "__main__":
    main()

