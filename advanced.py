import math
import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-n" ,"--numberone", type=int, required=True)
    parser.add_argument("-ntwo" ,"--numbertwo", type=str, required=True)
    parser.add_argument("-nthree" ,"--numberthree", type=bool, required=True)
    
    
    args = parser.parse_args()

    return

if __name__ == "__main__":
    main()