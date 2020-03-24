def is_prime(n):
	if n == 1:
		return False #once you return, method stops
	for i in range(2,n):
		if n % i == 0:
			return False
	return True

def print_100_prime():
	for j in range (1,101):
		if is_prime(j):
			print (j)
print_100_prime() 

def is_even(n):
	return n % 2 == 0

def print_100_even():
	for i in range (1,101):
		if is_even(i): 
			print (i)
print_100_even()
