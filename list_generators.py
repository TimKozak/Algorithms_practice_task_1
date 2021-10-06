import random

class Gen:

    # RANDOM ARRAY WITH NUMBERS FROM {1, ..., n}
    @staticmethod
    def random_array(n: int):
        array = random.sample(range(n), n)
        return array

    # SORTED ARRAY IN ASCENDING ORDER
    @staticmethod
    def sorted_array(n: int):
        array = random.sample(range(n), n)
        return sorted(array)

    # SORTED ARRAY IN DESCENDING ORDER
    @staticmethod
    def reversed_array(n: int):
        array = random.sample(range(n), n)
        return sorted(array, reverse=True)

    # ARRAY CONTAINING NUMBERS FROM {1, 2, 3}
    @staticmethod
    def repetitive_array(n: int):
        array = [random.choice([1, 2, 3]) for _ in range(n)]
        return array
