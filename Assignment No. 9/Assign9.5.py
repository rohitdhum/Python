"""5. Write a program which accepts one number and checks whether it is divisible by 3 and
5
"""

def Divisible(No):
    if (No % 3 == 0 and No % 5 == 0):
        print("Divisible by 3 and 5")
    
    else:
        print("Not Dvisible by 3 and 5")


def main():
    Value1 = int(input("Enter number :"))
    Ans = Divisible(Value1)

if __name__ == "__main__":
    main()

# Input: 15
# Output: Divisible by 3 and 5