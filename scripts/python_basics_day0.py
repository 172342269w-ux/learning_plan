"""Python Day 0 practice.

Run:
    python scripts/python_basics_day0.py

Goal:
    Understand print, variables, if/else, lists, loops, and functions.
"""


def say_hello(name: str) -> str:
    return f"Hello, {name}!"


def is_adult(age: int) -> bool:
    return age >= 18


def main() -> None:
    name = "lenxuan"
    age = 19

    print("1. print text")
    print("Python is running.")

    print()
    print("2. variables")
    print("name =", name)
    print("age =", age)

    print()
    print("3. if / else")
    if is_adult(age):
        print(name, "is an adult.")
    else:
        print(name, "is not an adult yet.")

    print()
    print("4. list and loop")
    tasks = ["learn print", "learn variables", "learn if", "learn function","learn list"]
    for task in tasks:
        print("- TODO:", task)

    print()
    print("5. function")
    message = say_hello(name)
    print(message)

    print()
    print("Your turn:")
    print("- Change name and age.")
    print("- Add one task to the tasks list.")
    print("- Run this file again.")


if __name__ == "__main__":
    main()

