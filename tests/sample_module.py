import numpy as np

def play_secret_santa(name, lucky_number, probability):
    ret_str = name + " " 
    a_range = np.arange(0, 100, 0.01)
    np.random.shuffle(a_range)

    if a_range[lucky_number] < probability: ret_str += "WINS"
    else: ret_str += "LOSES"
    return ret_str

def tell_me_how(name):
    return name + " says 'Hello There!'"