# main.py - Program entry point. Runs the loop: read input -> match keyword -> reply.
# AI concepts:
# - Rule-Based System: every reply is chosen by an if/elif rule written by hand.
# - Keyword Detection / Intent Recognition: trigger words ("time", "joke") tell us what the user wants.
# - Pattern Matching: text is lowercased and split into words before matching.

from greetings import get_user_name, build_greeting
from datetime_utils import get_current_time, get_current_date
from calculator import calculate
from content import get_random_quote, get_random_joke, get_random_fact
from game import play_guessing_game
from ai_concepts import recommend_activity, perceptron_demo
from help_menu import print_help


def main():
    print("=" * 43)
    print("        MINI ALEXA - VIRTUAL ASSISTANT")
    print("=" * 43)

    name = get_user_name()  # remembered for the whole session
    print("Assistant:", build_greeting(name))

    while True:
        command = input("You: ").lower().strip()
        words = command.split()  # "tell me a joke" -> ["tell", "me", "a", "joke"]

        # Exit is checked first so "bye" always ends the program
        if "exit" in words or "quit" in words or "bye" in words:
            print(f"Assistant: Goodbye, {name}! Have a great day.")
            break
        elif "calculate" in words:
            print("Assistant:", calculate(command))
        elif "hi" in words or "hello" in words or "hey" in words:
            print(f"Assistant: Hello again, {name}! How can I help?")
        elif "time" in words:
            print("Assistant:", get_current_time())
        elif "date" in words:
            print("Assistant:", get_current_date())
        elif "quote" in words:
            print("Assistant:", get_random_quote())
        elif "joke" in words:
            print("Assistant:", get_random_joke())
        elif "fact" in words:
            print("Assistant:", get_random_fact())
        elif "game" in words:
            play_guessing_game(name)
        elif "recommend" in words:
            print("Assistant:", recommend_activity())
        elif "perceptron" in words:
            perceptron_demo()
        elif "help" in words:
            print_help()
        else:  # Fallback: nothing matched, reply politely instead of crashing
            print("Assistant: I'm not sure I understood that - type 'help' to see what I can do.")


if __name__ == "__main__":  # run main() only when started with: python main.py
    try:
        main()
    except KeyboardInterrupt:  # Ctrl+C closes politely instead of showing an error
        print("\nAssistant: Goodbye!")
