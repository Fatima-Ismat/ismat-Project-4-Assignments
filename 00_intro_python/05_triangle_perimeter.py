## Problem Statement
## Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

## Here's a sample run of the program (user input is in bold italics):

## What is the length of side 1? 3

## What is the length of side 2? 4

## What is the length of side 3? 5.5

## The perimeter of the triangle is 12.5

## Starter Code

# def main():
#     print("Delete this line and write your code here! :)")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

## Solution

def main():
# Get the 3 side lengths of the triangle
    
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))

# Print out the perimeter (sum of the sides) of the triangle, make sure to cast it to a str when concatenating!
    print("The perimeter of the triangle is " + str(side1 + side2 + side3))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

#Final Solution

def main():
    side1 = float(input("What is the length of side 1? "))  
    side2 = float(input("What is the length of side 2? "))  
    side3 = float(input("What is the length of side 3? "))  

    perimeter = side1 + side2 + side3  # Total sum kar rahe hain

    print(f"The perimeter of the triangle is {perimeter}")  # Clean output

if __name__ == '__main__':
    main()

# Output

# What is the length of side 1? 3
# What is the length of side 2? 4
# What is the length of side 3? 5.5
# The perimeter of the triangle is 12.5

