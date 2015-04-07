# Fibonacci - tym razem tworze liste, a nie tylko licze n-ta liczbe

import itertools
import time
start_clock = time.clock()

def gen_Fib(n):	# n - max. nr liczby
# stosuje konwencje podana w arykule wikipedii: F0 = 0, F1 = 1
	F0 = 0
	Fib_list = [F0]
	yield F0
	F1 = 1
	Fib_list.append(F1)
	yield F1
	for i in itertools.count(2):
		if i > n:
			break
		F0, F1 = F1, F0+F1
		Fib_list.append(F1)
		yield F1

n = 800

Fib_list = []

for i in gen_Fib(n):
	Fib_list.append(i)

print(Fib_list[n])


print("--- %s seconds ---" % (time.clock() - start_clock))
# dla n = 14 wykonanie trwalo ok. 0.000493 s
# dla n = 800 wykonanie trwalo ok. 0.00135 s