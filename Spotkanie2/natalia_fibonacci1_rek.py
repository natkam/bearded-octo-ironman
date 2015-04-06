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
		return (Fib_n(n-1) + Fib_n(n-2))

print(Fib_n(50))
print("--- %s seconds ---" % (time.clock() - start_clock))
# dla n = 14 wykonanie trwalo 0.001305... sekund (o rzad wielkosci wiecej niz w wersji bez rekurencji)
# dla n = 800 wykonanie trwalo dobrych pare minut, potem znudzilam sie czekaniem i przerwalam