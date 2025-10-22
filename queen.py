#to check the code change the ranges from 8 board to 4 board its easier to understand or check smaller game.
import time
def is_consistent(assignment, var, value):
    """Check if placing queen at (var, value) is safe with current assignment."""
    for col in assignment:
        # same row or diagonal → conflict
        if assignment[col] == value:
            return False
        if abs(col - var) == abs(assignment[col] - value):
            return False
    return True
def print_board(assignment):
    """
    Print current board condition (partial or complete).
    'assignment' is a dict {col: row}.
    """
    for row in range(8):
        line = ""
        for col in range(8):
            if col in assignment and assignment[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()
def print_queens(assignment):
    """Print coordinates of all currently placed queens."""
    print("Queen positions (col, row):", end=" ")
    for col in sorted(assignment.keys()):
        print(f"({col},{assignment[col]})", end=" ")
    print("\n")
def backtrack(assignment, variables, domains, delay=0.25):
    """
    Recursive CSP backtracking search with live visualization.
    """
    # visualize current step
    print_board(assignment)
    time.sleep(delay)

    if len(assignment) == len(variables):
        print("✅ Solution found!")
        return dict(assignment)

    var = next(v for v in variables if v not in assignment)

    for value in domains[var]:
        if is_consistent(assignment, var, value):
            assignment[var] = value
            print(f"Placing queen at ({var},{value})")
            result = backtrack(assignment, variables, domains, delay)
            if result:
                return result
            # backtrack
            print(f"❌ Backtracking from ({var},{value})")
            del assignment[var]
            print_board(assignment)
            time.sleep(delay)

    return None
def solve_8_queens(initial_assignment=None, delay=0.25):
    """
    Solves 8 Queens CSP with optional initial placement.
    """
    variables = list(range(8))
    domains = {v: list(range(8)) for v in variables}
    assignment = {}

    if initial_assignment:
        for col, row in initial_assignment.items():
            if 0 <= col <= 7 and 0 <= row <= 7:
                assignment[col] = row

    print("Starting CSP backtracking...\n")
    print_board(assignment)
    time.sleep(1)

    solution = backtrack(assignment, variables, domains, delay)
    return solution
# --- MAIN PROGRAM ---
print("Choose an option:")
print("1. Solver decides all queens (no initial placement)")
print("2. User assigns initial queen(s)")
choice = input("Enter 1 or 2: ").strip()

initial_assignment = {}
if choice == "2":
    while True:
        try:
            col = int(input("Enter column (0–7): ").strip())
            row = int(input("Enter row (0–7): ").strip())
            initial_assignment[col] = row
            print_board(initial_assignment)
        except ValueError:
            print("Invalid input, please enter integers 0–7.")
            continue

        more = input("Add another queen? (y/n): ").lower()
        if more != "y":
            break

print("\nSolving...\n")
solution = solve_8_queens(initial_assignment, delay=0.3)

if solution:
    print("\nFinal Solution:")
    print_board(solution)
    print_queens(solution)
else:
    print("No solution found.")
