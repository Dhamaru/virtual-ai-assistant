# help_menu.py - Prints every command the assistant understands.

# Dictionary: command (key) -> short description (value)
COMMANDS = {
    "hello": "say hello",
    "time": "show current time",
    "date": "show current date",
    "calculate": "do a calculation, e.g. calculate 12 + 8",
    "joke": "tell a joke",
    "quote": "motivational quote",
    "fact": "random fact",
    "game": "play number guessing game",
    "recommend": "suggest an activity for this time of day",
    "perceptron": "run a simple artificial neuron demo",
    "help": "show this menu",
    "exit": "quit the assistant",
}


def print_help():
    print("Assistant: Here is what I can do:")
    for command in COMMANDS:
        print("  -", command.ljust(15), COMMANDS[command])  # ljust(15) lines up the columns
