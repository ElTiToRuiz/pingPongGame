import tkinter as tk
from tkinter import messagebox
import pingpong

def start_game():
    """
    Starts the Ping Pong game with the provided user names and target score.
    Retrieves user input from the GUI, validates the target score, and then
    calls the pingpong.start() function with the appropriate arguments.

    Raises
    ------
    ValueError
        If the target score is not a positive integer.
    """
    user1 = user1_entry.get()
    user2 = user2_entry.get()
    target = target_entry.get()

    if not target.isdigit():
        messagebox.showerror("Invalid Input", "Target must be a positive integer")
        return

    target = int(target)
    if user1 != '' and user2 != '':
        pingpong.start(user1, user2, target)
    else:
        pingpong.start(target=target)

def initialize():
    """
    Initializes the GUI for the Ping Pong game setup.
    Creates the main window, labels, entry fields, and start button.
    """
    root = tk.Tk()
    root.title("Ping Pong Game Setup")

    global user1_entry, user2_entry, target_entry

    tk.Label(root, text="User 1 Name:").grid(row=0, column=0, padx=10, pady=10)
    user1_entry = tk.Entry(root)
    user1_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="User 2 Name:").grid(row=1, column=0, padx=10, pady=10)
    user2_entry = tk.Entry(root)
    user2_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="Target Score:").grid(row=2, column=0, padx=10, pady=10)
    target_entry = tk.Entry(root)
    target_entry.grid(row=2, column=1, padx=10, pady=10)

    start_button = tk.Button(root, text="Start Game", command=start_game)
    start_button.grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()

def main():
    """
    Main function to initialize the GUI.
    """
    initialize()

if __name__ == '__main__':
    main()