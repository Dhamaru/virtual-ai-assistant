# ai_concepts.py - Two small AI / DL demos in plain Python. Nothing here is trained.
from datetime import datetime


# Demo 1: Rule-based recommendation
# AI concept - Rule-Based System: the answer comes from hand-written if/elif rules.
# ML idea - Classification / Decision Tree: the hour is sorted into one category;
# each if/elif is one branch of the tree.
def recommend_activity():
    hour = datetime.now().hour  # 0 to 23
    if hour < 5 or hour >= 22:
        activity = "It's late - you should rest and get some sleep."
    elif hour < 12:
        activity = "Good morning! It's a great time for breakfast and planning your day."
    elif hour < 14:
        activity = "It's lunchtime - take a break and eat something healthy."
    elif hour < 18:
        activity = "Afternoon is perfect for focused work or study."
    else:
        activity = "Evening time - go for a walk or relax with a hobby."
    return f"(The hour is {hour}) {activity}"


# Demo 2: Perceptron (one artificial neuron)
# Input = numbers the user types, Weight = how important each input is,
# Bias = fixed number added at the end, Activation = turns the total into 0 or 1.
# In real deep learning, weights and bias are LEARNED; here they are fixed.
WEIGHTS = [0.5, -0.6, 0.8]
BIAS = -0.2


def step_activation(total):
    """Activation function: 1 if total is above 0, otherwise 0."""
    if total > 0:
        return 1
    return 0


def ask_number(prompt):
    """Keep asking until the user types a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Assistant: Please enter a number.")


def perceptron_demo():
    """Forward Propagation: inputs -> x weights -> + bias -> activation -> output."""
    print("Assistant: Let's run a perceptron! Enter 3 numbers.")
    x1, x2, x3 = ask_number("Input 1: "), ask_number("Input 2: "), ask_number("Input 3: ")

    total = x1 * WEIGHTS[0] + x2 * WEIGHTS[1] + x3 * WEIGHTS[2] + BIAS
    output = step_activation(total)
    print(f"  Weights: {WEIGHTS}   Bias: {BIAS}")
    print(f"  Weighted sum + bias = {round(total, 2)} -> activation -> output = {output}")

    # Hidden Layer: a second neuron takes the first neuron's output as its input.
    # Stacking neurons like this is what makes a network "deep".
    hidden_output = step_activation(output * 1.5 - 1.0)  # weight 1.5, bias -1.0
    print(f"  Second neuron (hidden layer): {output} x 1.5 - 1.0 -> output = {hidden_output}")
