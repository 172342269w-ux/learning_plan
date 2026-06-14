"""Python Day 3 practice.

Run:
    python scripts/python_basics_day3.py

Goal:
    Practice lists and for loops.
"""


def main() -> None:
    tasks = [
        "run the Day 3 script",
        "add one new task",
        "explain what a for loop does",
        "write Day3 learning log",
    ]

    completed_tasks = [
        "run the Day 3 script",
        "add one new task",
        "explain what a for loop does"
    ]

    print("Python Day 3")
    print("Daily task checklist")

    for task in tasks:
        if task in completed_tasks:
            print("[x]", task)
        else:
            print("[ ]", task)

    print()
    print("Task count:", len(tasks))
    print("Completed count:", len(completed_tasks))
    print("Remaining count:", len(tasks) - len(completed_tasks))

    print()
    print("Your turn:")
    print("- Add one task to tasks.")
    print("- Add one completed task to completed_tasks.")
    print("- Run this file again and watch the counts change.")


if __name__ == "__main__":
    main()

