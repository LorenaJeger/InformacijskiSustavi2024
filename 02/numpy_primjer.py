import numpy as np


def numpy_example():
    # Kreiranje Numpy niza
    arr = np.array([1, 2, 3, 4, 5])

    # Korištenje Numpy funkcija
    mean_value = np.mean(arr)
    min_value = np.min(arr)
    max_value = np.max(arr)

    print("Mean:", mean_value)
    print("Min:", min_value)
    print("Max:", max_value)


if __name__ == '__main__':
    numpy_example()

# Mean: 3.0
# Min: 1
# Max: 5
