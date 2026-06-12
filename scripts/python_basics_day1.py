"""Python Day 1 practice.

Run:
    python scripts/python_basics_day1.py

Goal:
    Practice print, variables, strings, numbers, and simple calculations.
"""


def main() -> None:
    # Your turn: change these values first.
    name = "lenxuan"
    age = 19
    learning_goal = "学会 Python 变量和简单计算"
    today_task = "改变量并运行 Day 1 脚本"

    print("Python Day 1")
    print("Name:", name)
    print("Age:", age)
    print("Learning goal:", learning_goal)
    print("Today's task:", today_task)

    print()
    print("Simple calculations")
    next_year_age = age + 1
    days_in_one_week = 7
    study_days = 6
    rest_days = days_in_one_week - study_days

    print("Next year age:", next_year_age)
    print("Study days this week:", study_days)
    print("Rest days this week:", rest_days)

    print()
    print("Your turn:")
    print("- Change learning_goal to your real current goal.")
    print("- Change today_task to what you will do today.")
    print("- Change study_days and watch rest_days change.")


if __name__ == "__main__":
    main()

