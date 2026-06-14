"""Python Day 4 practice.

Run:
    python scripts/python_basics_day4.py

Goal:
    Practice functions and return values.
"""


def get_status_label(status_code: int) -> str:
    if 200 <= status_code < 400:
        return "ok"
    if 400 <= status_code < 500:
        return "warn"
    return "fail"


def main() -> None:
    status_codes = [200, 301, 404, 500,333,444,555,111]

    print("Python Day 4")
    print("Status code labels")

    for code in status_codes:
        label = get_status_label(code)
        print("status_code =", code, "label =", label)

    print()
    print("Your turn:")
    print("- Change one status code in the list.")
    print("- Add one more status code.")
    print("- Explain what the function returns for each case.")


if __name__ == "__main__":
    main()

