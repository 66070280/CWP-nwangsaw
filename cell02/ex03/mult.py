number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
result = number1 * number2
print(f"{number1} x {number2} = {result}")
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")