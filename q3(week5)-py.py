def armstrong(number):
    number = str(number)
    sum = 0
    for i in number:
        sum += pow(int(i), len(number))
    if str(sum) == number:
        return True
    else:
        return False


for i in range(1, 10001):
    if armstrong(i):
        print(i)