import numpy as np


def add_two_integer_lists(a: list[int], b: list[int]) -> str:
    """
    Function adding two integer lists together
    """
    return np.array(a) + np.array(b)


if __name__ == "__main__":
    print("My added array:", add_two_integer_lists([1, 2, 3], [4, 5, 6]))
