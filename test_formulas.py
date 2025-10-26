# Testing different formulas for domino piling

def formula_simple(m, n):
    """Simple formula: M * N // 2"""
    return (m * n) // 2

def formula_conditional(m, n):
    """User's formula: M * N // 2 + M // 2 if N is odd"""
    result = (m * n) // 2
    if n % 2 == 1:  # N is odd
        result += m // 2
    return result

# Test cases
test_cases = [
    (2, 3),
    (2, 4),
    (3, 3),
    (3, 4),
    (4, 5),
    (5, 5),
    (1, 16),
]

print("M  N  | Simple | Conditional | Match?")
print("-" * 45)
for m, n in test_cases:
    simple = formula_simple(m, n)
    conditional = formula_conditional(m, n)
    match = "✓" if simple == conditional else "✗"
    print(f"{m:2} {n:2} | {simple:6} | {conditional:11} | {match}")
