"""Python Day 2 practice.

Run:
    python scripts/python_basics_day2.py

Goal:
    Practice if, else, and comparison operators.
"""


def main() -> None:
    # Your turn: change these values first.
    name = "lenxuan"
    score = 50
    pass_line = 60

    print("Python Day 2")
    print("Name:", name)
    print("Score:", score)
    print("Pass line:", pass_line)

    print()
    print("Result")
    if score >= pass_line:
        print(name, "passed the test.")
    else:
        print(name, "did not pass the test yet.")

    print()
    print("Comparison checks")
    print("score >= pass_line:", score >= pass_line)
    print("score < pass_line:", score < pass_line)

    print()
    print("Your turn:")
    print("- Change score and run the file again.")
    print("- Try one score above 60 and one score below 60.")
    print("- Explain why the program entered the if branch or the else branch.")


if __name__ == "__main__":
    main()

