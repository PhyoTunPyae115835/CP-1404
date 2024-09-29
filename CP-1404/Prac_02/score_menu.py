from score import evaluate_score

def main():
    score = get_valid_score()  # Get a valid score before showing the menu
    choice = ''  # Initialize choice with an empty string

    # Menu will run until the user chooses 'Q'
    while choice != 'Q':
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Choose an option: ").upper()  # Get the user choice and convert it to uppercase

        if choice == 'G':
            score = get_valid_score()  # Get a new valid score
        elif choice == 'P':
            result = evaluate_score(score)
            print(f"Result: {result}")
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell")
        else:
            print("Invalid choice. Please try again.")

def get_valid_score():
    score = float(input("Enter a score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Please try again.")
        score = float(input("Enter a score (0-100): "))
    return score

def show_stars(score):
    print('*' * int(score))

main()