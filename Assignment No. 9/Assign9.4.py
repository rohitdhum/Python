"""4. Write a program which accepts one number and prints cube of that number.
"""

def Cube(No):
    return No*No*No

def main():
    Value1 = int(input("Enter number :"))
    Ans = Cube(Value1)
    print("Cube is", Ans)

if __name__ == "__main__":
    main()

# Input : 5
# Output : 125