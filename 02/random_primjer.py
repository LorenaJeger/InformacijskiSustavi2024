from random import choice as rnd_choice
import random


def random_okus(seed=None):
    # Postavljanje sjemena
    random.seed(seed)

    # slučajan odabir okusa sladoleda:
    print(rnd_choice(["vanilija", "čokolada", "lješnjak"]))


if __name__ == '__main__':
    # Postavljanje sjemena na određenu vrijednost (npr. 44)
    seed_value = 44
    random_okus(seed=seed_value)



