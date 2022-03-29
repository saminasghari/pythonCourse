a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b != 0:
    t = a
    a = b
    b = t % b
print("GCD:", a)
