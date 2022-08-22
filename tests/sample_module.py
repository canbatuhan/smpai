import numpy as np

def play_secret_santa(name, lucky_number, probability):
    a_range = np.arange(0, 100, 0.01)
    np.random.shuffle(a_range)

    if a_range[lucky_number] < probability:
        lucky_number += 1

    else:
        lucky_number -= 1

    return {"lucky_number": lucky_number}