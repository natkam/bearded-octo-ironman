def bubble_sort(numbers):
	sorted = False
	while not sorted:
		sorted = True
		for i in range(len(numbers)-1):
			if numbers[i] <= numbers[i+1]:
				continue
			else:
				numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
				sorted = False
	return numbers

numbers = [7, 6, 6, 5, 4, 1, 2, 6, 3]
posortowana = bubble_sort(numbers)
print(posortowana)
