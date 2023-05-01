import random

def random_select():
    numbers = random.sample(range(1, 46), 6)
    return sorted(numbers, reverse=True)

selected_numbers = random_select()
print(selected_numbers)

