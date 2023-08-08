import random


def DNA(length: int) -> str:
    """Returns a random DNA sequence of the given length."""
    return "".join(random.choice("acgt") for _ in range(length))


for i in range(1000):
    print(DNA(1000))
