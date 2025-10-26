# Codeforces Problem 50A - Domino piling
# Solution: The maximum number of dominoes that can fit on an M x N board
# is simply (M * N) // 2, since each domino covers 2 squares

# Read input
m, n = map(int, input().split())

# Calculate maximum number of dominoes
max_dominoes = (m * n) // 2

# Output result
print(max_dominoes)
