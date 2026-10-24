# calculator.py - Turns "calculate 12 + 8" into an answer.
# AI concept - Pattern Matching: we expect  calculate <number> <operator> <number>


def parse_expression(command):
    """Split "calculate 12 + 8" into 12.0, "+", 8.0. Return None if it doesn't fit."""
    text = command.replace("calculate", "").replace(" ", "")  # "calculate 12 + 8" -> "12+8"
    for operator in ["+", "*", "/", "-"]:
        # Search from position 1, so a minus sign at the start ("-5-2") stays part of the number
        position = text.find(operator, 1)
        if position != -1:
            try:
                return float(text[:position]), operator, float(text[position + 1:])
            except ValueError:  # float("abc") fails -> not a number
                return None
    return None


def calculate(command):
    """Return the answer as a sentence. Never crashes on bad input."""
    parsed = parse_expression(command)
    if parsed is None:
        return "Please type it like this: calculate 12 + 8"

    a, operator, b = parsed
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif b == 0:
        return "I can't divide by zero - try a different number."
    else:
        result = a / b

    result = round(result, 4)  # 12/880 -> 0.0136 instead of 0.013636363636363636
    if result == int(result):  # show 20 instead of 20.0
        result = int(result)
    return f"The result is {result}"
