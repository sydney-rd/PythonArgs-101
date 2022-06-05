import math
import argparse

# compute the area of a circle given the radius
def circle_area(radius):
    return (radius) * (radius) * (math.pi)

def main():

    parser = argparse.ArgumentParser(description="Enter radius of a circle and we will calculate the area")
    parser.add_argument("-r", "--radius", type=int, required=True, help="Radius of a circle")
    args = parser.parse_args()

    print(circle_area(args.radius))

    return

if __name__ == "__main__":
    main()