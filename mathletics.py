import random
import time
import json
import math

# Define questions per level
level_questions = {
    1: ["1-10 addition", "doubles up to 10"],
    2: ["1-20 addition", "1-20 subtraction"],
    3: ["1-50 addition", "1-50 subtraction", "2s, 3s, 4s, 5s, 10s Times Tables", "doubles and halves up to 50"],
    4: ["1-100 addition", "1-100 subtraction", "Times Tables to 10x10", "doubles and halves up to 100"],
    5: ["1-500 addition", "1-100 subtraction", "1-100 addition with a missing addend"],
    6: ["operations with decimals", "calculations using brackets", "simple percentages"],
    7: ["sum, difference, product, and quotient", "cubes", "operations with integers"],
    8: ["statistical measures", "simplifying algebra I", "algebraic substitution I"],
    9: ["algebraic substitution II", "factoring II", "order operation III"],
    10: ["logarithms", "solving equations", "algebraic substitution III"]
}

def generate_question(level):
    topic = random.choice(level_questions[level])
    if "addition" in topic:
        a, b = random.randint(1, 10**level), random.randint(1, 10**level)
        return f"What is {a} + {b}?", a + b
    elif "subtraction" in topic:
        a, b = random.randint(1, 10**level), random.randint(1, 10**level)
        return f"What is {a} - {b}?", a - b
    elif "Times Tables" in topic:
        a = random.randint(1, 10)
        b = random.choice([2, 3, 4, 5, 10])
        return f"What is {a} x {b}?", a * b
    elif "doubles" in topic:
        a = random.randint(1, 10**(level//2))
        return f"What is double {a}?", a * 2
    elif "halves" in topic:
        a = random.randint(1, 10**(level//2))
        return f"What is half of {a}?", a / 2
    elif "operations with decimals" in topic:
        a, b = random.uniform(1, 10), random.uniform(1, 10)
        return f"What is {a:.1f} + {b:.1f}?", round(a + b, 1)
    elif "calculations using brackets" in topic:
        a, b, c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
        return f"What is ({a} + {b}) * {c}?", (a + b) * c
    elif "simple percentages" in topic:
        a = random.randint(1, 100)
        return f"What is 10% of {a}?", a * 0.1
    elif "sum, difference, product, and quotient" in topic:
        a, b = random.randint(1, 100), random.randint(1, 100)
        op = random.choice(['+', '-', '*', '//'])
        question = f"What is {a} {op} {b}?"
        answer = eval(f"{a} {op} {b}")
        return question, answer
    elif "cubes" in topic:
        a = random.randint(1, 10)
        return f"What is {a}^3?", a**3
    elif "operations with integers" in topic:
        a, b = random.randint(-50, 50), random.randint(-50, 50)
        op = random.choice(['+', '-', '*', '//'])
        question = f"What is {a} {op} {b}?"
        answer = eval(f"{a} {op} {b}")
        return question, answer
    elif "statistical measures" in topic:
        numbers = [random.randint(1, 100) for _ in range(5)]
        mean = sum(numbers) / len(numbers)
        return f"What is the mean of {numbers}?", mean
    elif "simplifying algebra I" in topic:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        return f"Simplify: {x}x + {y}x", (x + y)
    elif "algebraic substitution I" in topic:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        return f"Evaluate: {x}*{y} + {z}", (x * y + z)
    elif "algebraic substitution II" in topic:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        return f"Evaluate: {x}^2 + {y}^2", (x**2 + y**2)
    elif "factoring II" in topic:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        return f"Factor: {a*b} into {a} and {b}", (a, b)
    elif "order operation III" in topic:
        a, b, c, d = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
        return f"Evaluate: ({a} + {b}) * {c} / {d}", (a + b) * c / d
    elif "logarithms" in topic:
        a = random.randint(1, 100)
        return f"Evaluate log10({a})", round(math.log10(a), 2)
    elif "solving equations" in topic:
        x = random.randint(1, 10)
        return f"Solve for x: 2x + 3 = {2*x + 3}", x
    else:
        return "Complex question based on level", None

def ask_question(question):
    try:
        user_answer = float(input(question + " "))
        return user_answer
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def save_stats(username, stats):
    with open(f"{username}_stats.json", "w") as f:
        json.dump(stats, f)

def load_stats(username):
    try:
        with open(f"{username}_stats.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {str(level): {"matches_played": 0, "high_score": 0, "total_points": 0, "total_correct": 0, "total_questions": 0} for level in range(1, 11)}

def main():
    username = input("Enter your username: ")
    stats = load_stats(username)
    
    print("Select level (1-10):")
    level = int(input())
    if level not in range(1, 11):
        print("Invalid level selected.")
        return

    start_time = time.time()
    correct_answers = 0
    total_questions = 0
    wrong_answers = 0
    points = 0

    while time.time() - start_time < 60:
        question, answer = generate_question(level)
        user_answer = ask_question(question)
        if user_answer is None:
            continue
        if user_answer == answer:
            correct_answers += 1
            points += 1
        else:
            wrong_answers += 1
            print(f"Wrong! You have {3 - wrong_answers} chances left.")
            if wrong_answers == 3:
                print("You have been eliminated!")
                break
        total_questions += 1

    match_score = correct_answers / total_questions * 100 if total_questions else 0
    print(f"Time's up! You got {correct_answers} out of {total_questions} questions right.")
    print(f"Your score for this match is {match_score:.2f}%")

    stats[str(level)]["matches_played"] += 1
    stats[str(level)]["total_points"] += points
    stats[str(level)]["total_correct"] += correct_answers
    stats[str(level)]["total_questions"] += total_questions
    if correct_answers > stats[str(level)]["high_score"]:
        stats[str(level)]["high_score"] = correct_answers

    save_stats(username, stats)

    print(f"Stats for Level {level}:")
    print(f"Matches played: {stats[str(level)]['matches_played']}")
    print(f"High score: {stats[str(level)]['high_score']}")
    print(f"Total points: {stats[str(level)]['total_points']}")
    print(f"Total questions answered: {stats[str(level)]['total_questions']}")
    print(f"Total correct answers: {stats[str(level)]['total_correct']}")
    print(f"Overall accuracy: {stats[str(level)]['total_correct'] / stats[str(level)]['total_questions'] * 100:.2f}%")

if __name__ == "__main__":
    main()
