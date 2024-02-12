""" Task 1: Calculate Area with Conditions """

# Calculate the area of a rectangle or return a square 

def calculate_area(length, width):

    if length == width:
        return "This is a square!"
    else:
        return length * width

def main():
    # Input length and width from the user
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    # Call function
    result = calculate_area(length, width)

    # Display result
    print("Area:" if isinstance(result, float) else "Message:", result)

if __name__ == "__main__":
    main()
