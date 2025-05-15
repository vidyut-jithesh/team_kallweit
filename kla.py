import random

def generate_random_numbers(count, start, end):
    """Generate a list of random numbers."""
    return [random.randint(start, end) for _ in range(count)]

if __name__ == "__main__":
    numbers = generate_random_numbers(5, 1, 100)
    print("Random numbers:", numbers)
