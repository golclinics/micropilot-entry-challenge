def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i}: FizzBuzz")
        elif i % 5 == 0:
            print(f"{i}: Buzz")
        elif i % 3 == 0:
            print(f"{i}: Fizz")
        else:
            print(i)

if __name__ == "__main__":
    fizzbuzz()