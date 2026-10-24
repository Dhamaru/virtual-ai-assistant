# Virtual AI Assistant (Mini Alexa)

AI Internship Project 1 (AI-INT-P1-VAA). Text-based, rule-based assistant
that runs fully offline. Uses only the Python standard library: no external packages, no APIs, no internet access.

## Setup

Requires Python 3.x only. No installation step, no network dependency.

```
cd virtual-ai-assistant
python main.py
```

## Commands

| Command | What it does |
|---|---|
| `hello` | Returns a greeting using the stored user name |
| `time` | Reads the system clock, returns the current time |
| `date` | Reads the system clock, returns today's date |
| `calculate 12 + 8` | Performs +, -, *, / on two numbers. Spaces optional: `12*80` and `12 * 80` both work |
| `joke` | Returns one random joke from a predefined list |
| `quote` | Returns one random motivational quote from a predefined list |
| `fact` | Returns one random fact from a predefined list |
| `game` | Starts the number guessing game: range 1-20, 5 tries, higher/lower hints |
| `recommend` | Recommends an activity based on the current hour |
| `perceptron` | Runs a single artificial neuron demo: inputs → weights → bias → activation → output |
| `help` | Prints every supported command with a one-line description |
| `exit` / `quit` / `bye` | Ends the main loop with a farewell message |

## Files

| File | Responsibility |
|---|---|
| `main.py` | Imports all modules, runs the input → match → respond loop, handles top-level exceptions (Ctrl+C) |
| `greetings.py` | `get_user_name()`, `build_greeting()`: captures the name once, reuses it across the session |
| `datetime_utils.py` | `get_current_time()`, `get_current_date()`: formats the system clock via `datetime` |
| `calculator.py` | `parse_expression()`, `calculate()`: extracts number-operator-number, handles divide-by-zero and non-numeric input |
| `content.py` | `QUOTES`, `JOKES`, `FACTS`, `get_random_quote()`, `get_random_joke()`, `get_random_fact()`: list storage + `random.choice` selection |
| `game.py` | `play_guessing_game()`: random target via `random.randint`, attempt limit enforced |
| `ai_concepts.py` | `recommend_activity()`, `perceptron_demo()`: rule-based decision + single-neuron forward pass |
| `help_menu.py` | `print_help()`: formats the command dictionary into aligned columns |

## Where the AI / ML / DL concepts appear

| Concept | Where in the code |
|---|---|
| Rule-based system | `main.py` if/elif chain maps input → response; `ai_concepts.recommend_activity()` maps hour → activity |
| Intent recognition / keyword detection | `main.py` trigger words (`time`, `joke`, `calculate`, ...) route input to the correct function |
| Pattern matching | `main.py` lowercase + split normalizes input; `calculator.parse_expression()` detects number-operator-number |
| Learning user preferences (ML analogy) | User name stored once, reused in later replies. Mirrors a model retaining learned parameters |
| Classification / decision tree (ML analogy) | `recommend_activity()` assigns the hour to one category. Each if/elif acts as one tree branch |
| Recommendation logic (ML analogy) | `content.py` random selection stands in for a recommendation engine's content choice |
| Artificial neuron, weights, bias, activation | `ai_concepts.WEIGHTS`, `BIAS`, `step_activation()`: fixed values, no training |
| Forward propagation, hidden layer, perceptron | `ai_concepts.perceptron_demo()`: inputs → weighted sum + bias → step activation → 0/1, then a second neuron as hidden layer |

## Known limitations

Matching is keyword-based. Reasonable phrasings without a trigger word (e.g. "what's the hour?") fall through to the
fallback message instead of crashing. Expected behaviour for a rule-based system: discussed, not fixed with an
external NLP library (PRD §35).

## OUTPUT (generated)

Full session as user Dhamaru, every command from `help` executed once.

```
===========================================
        MINI ALEXA - VIRTUAL ASSISTANT
===========================================
Assistant: Hi! I'm Mini Alexa. What's your name?
You: Dhamaru
Assistant: Nice to meet you, Dhamaru! Type 'help' to see what I can do.
You: help
Assistant: Here is what I can do:
  - hello           say hello
  - time            show current time
  - date            show current date
  - calculate       do a calculation, e.g. calculate 12 + 8
  - joke            tell a joke
  - quote           motivational quote
  - fact            random fact
  - game            play number guessing game
  - recommend       suggest an activity for this time of day
  - perceptron      run a simple artificial neuron demo
  - help            show this menu
  - exit            quit the assistant
You: hello
Assistant: Hello again, Dhamaru! How can I help?
You: time
Assistant: It's currently 12:48 PM.
You: date
Assistant: Today is Saturday, 24 October 2026.
You: calculate 12 + 8
Assistant: The result is 20
You: joke
Assistant: Why did the Python programmer wear glasses? Because they couldn't C.
You: quote
Assistant: It always seems impossible until it's done. - Nelson Mandela
You: fact
Assistant: Python is named after the comedy group Monty Python, not the snake.
You: game
Assistant: I'm thinking of a number between 1 and 20. You have 5 tries.
Guess a number: 10
Assistant: Go lower. Tries left: 4
Guess a number: 5
Assistant: Go lower. Tries left: 3
Guess a number: 2
Assistant: Go higher. Tries left: 2
Guess a number: 3
Assistant: Correct, Dhamaru! You guessed it.
You: recommend
Assistant: (The hour is 12) It's lunchtime - take a break and eat something healthy.
You: perceptron
Assistant: Let's run a perceptron! Enter 3 numbers.
Input 1: 1
Input 2: 0
Input 3: 1
  Weights: [0.5, -0.6, 0.8]   Bias: -0.2
  Weighted sum + bias = 1.1 -> activation -> output = 1
  Second neuron (hidden layer): 1 x 1.5 - 1.0 -> output = 1
You: exit
Assistant: Goodbye, Dhamaru! Have a great day.
```
