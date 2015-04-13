# Fibonacci

import time
start_clock = time.clock()

def Fib_n(n):
# stosuje konwencje podana w arykule wikipedii: F0 = 0, F1 = 1
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		F0 = 0
		F1 = 1
		i = 2
		while i<=n:
			F0, F1 = F1, F0+F1
			i += 1
			#print(i, F0, F1)
		return F1

print(Fib_n(800))
print("--- %s seconds ---" % (time.clock() - start_clock))
# dla n = 14 wykonanie trwalo 0.000205... sekund
# dla n = 800 wykonanie trwalo 