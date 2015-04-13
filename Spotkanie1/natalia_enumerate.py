from itertools import count

# def my_enum(seq):
# 	numbers = range(1,len(seq)+1)
# 	zipped = zip(numbers, seq)
# 	return(zipped)

# ladniej z iteratorem:

def my_enum(seq):
	return zip(count(start=1), seq)


weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
enum_days = my_enum(weekdays)
print(*enum_days)
