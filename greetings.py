# greetings.py - Greeting and name capture.
# ML idea - learning user preferences: the name is stored once and reused later,
# like a trained model "remembering" what it learned.


def get_user_name():
    """Ask for the user's name. Keep asking if they type nothing."""
    name = input("Assistant: Hi! I'm Mini Alexa. What's your name?\nYou: ").strip()
    while name == "":
        name = input("Assistant: I didn't catch that. What's your name?\nYou: ").strip()
    return name


def build_greeting(name):
    """Return the welcome message that uses the user's name."""
    return f"Nice to meet you, {name}! Type 'help' to see what I can do."
