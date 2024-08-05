import tkinter as tk
from tkinter import messagebox
from player import Player
class PokerGUI:
    def __init__(self, root, players):
        self.root = root
        self.players = players # List of Player class
        self.root.title("Poker Game")

        # Frame for player information
        self.player_frame = tk.Frame(root)
        self.player_frame.pack(pady=10)

        # Player and stack labels
        self.player_labels = []
        self.stack_labels = []
        for i, player in enumerate(players):
            player_label = tk.Label(self.player_frame, text = f"{player.name}")
            player_label.grid(row=i, column=0, padx=10)
            self.player_labels.append(player_label)

            stack_label = tk.Label(self.player_frame, text = f"Stack: {player.stack}")
            stack_label.grid(row=i, column=1, padx=10)
            self.stack_labels.append(stack_label)
        
        #Frame for actions
        self.action_frame = tk.Frame(root)
        self.action_frame.pack(pady=10)

        # Entry for raise amount
        self.raise_amount_label = tk.Label(self.action_frame, text="Raise Amount")
        self.raise_amount_label.pack(side=tk.LEFT, padx=5)

        self.raise_amount_entry = tk.Entry(self.action_frame)
        self.raise_amount_entry.pack(side=tk.LEFT, padx=5)

        # Action buttons
        self.bet_button = tk.Button(self.action_frame, text="Bet", command=self.bet_action)
        self.bet_button.pack(side=tk.LEFT, padx=5)

        # Fold button
        self.fold_button = tk.Button(self.action_frame, text="Fold", command=self.fold_action)
        self.fold_button.pack(side=tk.LEFT, padx=5)

        # Raise button
        self.raise_button = tk.Button(self.action_frame, text="Raise", command=self.raise_action)
        self.raise_button.pack(side=tk.LEFT, padx=5)

        self.status_message = tk.Label(root, text="Welcome to Poker!")
        self.status_message.pack(pady=10)

    def bet_action(self):
        player = self.players[0]
        current_bet = 100
        try:
            player.bet(current_bet)
            self.update_player_stack(0, player.stack)
            self.update_status(f"{player.name} bet {current_bet}")
        except ValueError as e:
            self.update_status(str(e))
        messagebox.showinfo("Action", "Bet action triggered")

    def fold_action(self):
        messagebox.showinfo("Action", "Bet action triggered")
    
    def raise_action(self):
        player = self.players[0]
        current_bet = 100
        raise_amount_str = self.raise_amount_entry.get()
        try:
            raise_amount = int(raise_amount_str)
            player.raise_bet(current_bet, raise_amount)
            self.update_player_stack(0, player.stack)
            self.update_status(f"{player.name} raised by {raise_amount}")
        except ValueError:
            self.update_status("Invalid raise amount. Please enter a valid number")

    def update_player_stack(self, player_index, new_stack):
        self.stack_labels[player_index].config(text=f"Stack: {new_stack}")
    
    def update_player_hand(self, player_index, hand):
        self.player_labels[player_index].config(text=f"Hand: {hand}")
    
    def update_status(self, message):
        self.status_message.config(text=message)
root = tk.Tk()
gui = PokerGUI(root, [Player("Jack", 1000), Player("Jill", 1000)])
root.mainloop()