import random

def get_numbers_ticket(min_val:int, max_val:int, quantity:int)->list:
    
    if not (1 <= min_val <= max_val <= 1000) or not (min_val <= quantity <= max_val):
        return []
    
    
    random_numbers = set()
    while len(random_numbers) < quantity:
        random_numbers.add(random.randint(min_val, max_val))
    
    
    return sorted(list(random_numbers))

print(get_numbers_ticket(1, 49, 6))