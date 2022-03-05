from ast import arg
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--f1")
parser.add_argument("--f2")

args = vars(parser.parse_args())
sum_func = args['f1']
mul_func = args['f2']

def run():
    return os.system('python {}'.format(sum_func)), os.system('python {}'.format(mul_func))

if __name__=="__main__":
    print(run())
