import random

def main():
    # Ask the user for their score
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(f"Your result: {result}")

    random_score = random.randint(0, 100)
    random_result = evaluate_score(random_score)
    print(f"Random score: {random_score}, Result: {random_result}")

def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
