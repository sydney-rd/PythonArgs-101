import math

# compute the area of a circle given the radius
def circle_area(radius):
    return (radius) * (radius) * (math.pi)

# main function to ensure valid input for radius
def main():
    try:
        inp = int(input("enter radius: "))
        print(circle_area(inp))
    except:
        print("input was invalid")

    return
    
# calls the main function
if __name__ == "__main__":
    main()