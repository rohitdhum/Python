""" 3. Write a program which accepts one number and prints square of that number.
"""
def Square(No):
    return No*No

def main():
    Value1 = int(input("Enter number :"))
    Ans = Square(Value1)
    print("Square is", Ans)

if __name__ == "__main__":
    main()

# Input: 5
# Output: 25