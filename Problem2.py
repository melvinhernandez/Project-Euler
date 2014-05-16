def fib(n):
	if n < 2:
		return n
	else:
		return fib(n-1) + fib(n-2)

term = 0
total = 0
prev_value = fib(term)
while prev_value <= 4000000:
	if prev_value % 2 == 0:
		total += prev_value
	term += 1
	prev_value = fib(term)

print(total)