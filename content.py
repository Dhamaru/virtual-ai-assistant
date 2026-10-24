# content.py - Quotes, jokes and facts, picked at random.
# ML idea - Recommendation logic: real apps pick content with a trained model;
# here random.choice() simply picks one item from a list.
import random

QUOTES = [
    "The secret of getting ahead is getting started. - Mark Twain",
    "It always seems impossible until it's done. - Nelson Mandela",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Small steps every day add up to big results.",
]

JOKES = [
    "Why did the developer go broke? Because they used up all their cache.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the neural network go to therapy? It had too many unresolved layers.",
    "Why was the math book sad? It had too many problems.",
    "Why did the Python programmer wear glasses? Because they couldn't C.",
]

FACTS = [
    "The first computer bug was a real moth found in a Harvard computer in 1947.",
    "The perceptron was invented by Frank Rosenblatt in 1958.",
    "The term 'Artificial Intelligence' was first used by John McCarthy in 1956.",
    "Python is named after the comedy group Monty Python, not the snake.",
    "The human brain has roughly 86 billion neurons.",
]


def get_random_quote():
    return random.choice(QUOTES)


def get_random_joke():
    return random.choice(JOKES)


def get_random_fact():
    return random.choice(FACTS)
