import random

def random_select():
    return random.sample(range(1, 46), 6)

selected_numbers = random_select()
print(selected_numbers)

