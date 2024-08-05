firstStr = input("Enter the first number: ")
secondStr = input("Enter the second number: ")
thirdStr = input("Enter the third number: ")


def cast(number):
    if str(number).isdigit():
        return int(number)
    else:
        return "NaN"  #not a number


first = cast(firstStr)
second = cast(secondStr)
third = cast(thirdStr)

if isinstance(first, int) and isinstance(second, int) and isinstance(third, int):
    if first == second and second == third:
        print(3)
    elif first != second and first != third and second != third:
        print(0)
    else:
        print(2)
else:
    print("Invalid data (string)")