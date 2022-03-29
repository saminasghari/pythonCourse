def func(x):
    return x * x * x - x * x + 2


def dFunc(x):
    return 3 * x * x - 2 * x


def newtonRaphson(x):
    h = func(x) / dFunc(x)
    while abs(h) >= 0.0001:
        h = func(x) / dFunc(x)
        x = x - h
    print("The value of the root is : %.5f" % x)


x0 = -20
newtonRaphson(x0)