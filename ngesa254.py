def getX(x1, x2):
    if x1 > x2:
        return x1
    else:
        return x2

x1 = input("> x1: ")
x2 = input("> x2: ")
print (getX(x1, x2))