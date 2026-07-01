""" 2. Write a program which contains one function ChkGreater() that accepts two numbers
and prints the greater number.
"""
def ChkGreater(No1, No2):
    if(No1>No2):
        print(No1,"is greater")

    else:
        print(No2,"is greater")

def main():
    Value1 = int(input("Enter first number :"))
    Value2 = int(input("Enter second number :"))

    ChkGreater(Value1,Value2)

if __name__ == "__main__":
    main()

# Input: 10 20
# Output: 20 is greater