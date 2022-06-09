import math
import argparse

# compute the area of a circle given the radius
def circle_area(radius):
    return (radius) * (radius) * (math.pi)    

# main function that uses argparse to allow the user to enter three different radius'
def main():
    parser = argparse.ArgumentParser(description="Enter three radius' of a circle and we will calculate the area of each")
    parser.add_argument("-r", "--radius", type=int, required=True, help="Radius of a circle")
    parser.add_argument("-r2", "--radius2", type=int, required=True, help="Second radius of a circle")
    parser.add_argument("-r3", "--radius3", type=int, required=True, help="Third radius of a circle")
    args = parser.parse_args()

    print(circle_area(args.radius))
    print(circle_area(args.radius2))
    print(circle_area(args.radius3))

# calls the main function
if __name__ == "__main__":
    main()
