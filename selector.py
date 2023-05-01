import random

def random_select(n):
    results = []
    for _ in range(n):
        numbers = random.sample(range(1, 46), 6)
        results.append(sorted(numbers))
    return results

num_draws = int(input("Enter the number of times you want to pick six numbers: "))
selected_numbers = random_select(num_draws)

for i, numbers in enumerate(selected_numbers, 1):
    print(f"Draw {i}: {numbers}")

