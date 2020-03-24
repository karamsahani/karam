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
	'''
	j=1
	while(j<101):
		if is_prime(j):
			print (j)
		j = j + 1 #j+=1
	'''
print_100_prime() 

def is_even(n):
	return n % 2 == 0

def print_100_even():
	for i in range (1,101):
		if is_even(i): 
			print (i)
print_100_even()

def print_first_100_primes():
	count = 0
	i=1
	while(count < 100):
		if is_prime(i):
			print(i)
			count+=1
		i+=1
print_first_100_primes()