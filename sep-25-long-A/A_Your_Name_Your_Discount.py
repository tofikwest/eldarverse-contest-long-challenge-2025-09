# Problem A: Your Name, Your Discount
# Contest: Eldarverse Long Challenge – September 2025
# Author: Tofik Hasanov


def solve_one(case_idx, name):
    validate_name = name.lower()
    visited = set()

    for ch in validate_name:
        visited.add(ch)

    unique_letter = len(visited)
    total_price = 100 - (unique_letter * 5)

    print(f"Case #{case_idx}: {total_price}")


def main():
    T = int(input().strip())
    for case_idx in range(1, T + 1):
        name = input().strip()
        solve_one(case_idx, name)


if __name__ == "__main__":
    main()
