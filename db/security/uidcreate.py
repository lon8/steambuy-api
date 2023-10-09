import random

def generate_seven_digit_id() -> int:
    return ''.join(random.choice('0123456789') for _ in range(7))