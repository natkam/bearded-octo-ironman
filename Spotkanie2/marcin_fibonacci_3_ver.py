def fibonacci_numbers_recursion(number):
    if number > 1:
        return fibonacci_numbers_recursion(number - 1) + fibonacci_numbers_recursion(number - 2)
    elif number == 1:
        return 1
    else:
        return 0

def fibonacci_numbers_iteration(number):
    if number > 1:
        prev, prevprev = 1, 0
        for num in range(2, number+1):
            fibo = prev + prevprev
            prevprev = prev
            prev = fibo
        return fibo
    elif number == 1:
        return 1
    else:
        return 0

def fibonacci_generator(how_much):
    prevprev, prev = 0, 1
    iter = 0
    yield prevprev
    yield prev
    while iter < how_much-2:
        fibo = prevprev + prev
        prevprev = prev
        prev = fibo
        iter += 1
        yield prev

if __name__=='__main__':
    # Fibonacci numbers
    tests = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

    print("Tests for fibonacci_numbers_recursion():")
    for num in range(20):
        fibo = fibonacci_numbers_recursion(num)
        print("test nr {0:<2} - {1}.    Fibonacci number is {2:<4}".format(num, fibo == tests[num], fibo))

    print("\nTests for fibonacci_numbers_iteration():")
    for num in range(20):
        fibo = fibonacci_numbers_recursion(num)
        print("test nr {0:<2} - {1}.    Fibonacci number is {2:<4}".format(num, fibo == tests[num], fibo))

    print("\nTests for fibonacci_numbers_generator():")
    no = 0
    for fibo_no in fibonacci_generator(20):
        print("test nr {0:<2} - {1}.    Fibonacci number is {2:<4}".format(no, fibo_no == tests[no], fibo_no))
        no += 1
