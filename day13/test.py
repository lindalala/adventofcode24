from math import gcd

# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


# General solution of a single linear Diophantine equation ax + by = c
def solve_single_diophantine(a, b, c):
    g, x0, y0 = extended_gcd(a, b)
    if c % g != 0:
        return None  # No solutions
    scale = c // g
    x0 *= scale
    y0 *= scale
    return x0, y0, a // g, b // g


# Solve Diophantine using bounds to ensure positivity
def find_all_solutions(eq1, eq2):
    a1, b1, c1 = eq1
    a2, b2, c2 = eq2

    # Solve the first Diophantine equation
    solution1 = solve_single_diophantine(a1, b1, c1)
    if solution1 is None:
        print("No solution exists for the first equation")
        return []
    
    x0_1, y0_1, a1_g, b1_g = solution1

    # Now solve the second Diophantine equation
    solution2 = solve_single_diophantine(a2, b2, c2)
    if solution2 is None:
        print("No solution exists for the second equation")
        return []
    
    x0_2, y0_2, a2_g, b2_g = solution2

    # Calculate ranges for x and solve for integer solutions
    potential_solutions = []
    for k in range(-100000, 100000):  # Iterate over a reasonable range
        x = x0_1 + k * b2_g
        y = y0_2 - k * a1_g
        if x > 0 and y > 0:
            potential_solutions.append((x, y))

    return potential_solutions


# Example usage
equation1 = (26, 67, 10000000012748)
equation2 = (66, 21, 10000000012176)

solutions = find_all_solutions(equation1, equation2)

print("Solutions found:")
for x, y in solutions:
  print(f"x = {x}, y = {y}")