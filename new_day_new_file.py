def pr():
	print(5)

pr()
pr()
# % division is remainder division
if True:
	print("yay")
print(5%2)
def is_even(n):
	print(n % 2 == 0)
is_even(5)
is_even(6)
def p(a, b):# inputs are parameters
	return a + b #actually gives you the value

x = p(5,5)
print(p(x,x)) 

def is_prime(n):
	if n == 1:
		return False #once you return, method stops
	for i in range(2,n):
		if n % i == 0:
			return False
	return True

def print_100_primes():
	for i in range(2,101):
		if not is_prime (i):
			print (i)
		

def square(n):
	return n**2
print (square (5))

def square_100():
	for i in range (0,101):
		print (square(i))
square_100()

