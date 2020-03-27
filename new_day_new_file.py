def is_prime(n): #made function, takes input n (n is conditional number entered by user)
	if n == 1: #special case for 1 (1 is not prime number)
		return False
	i = 2 #start loop with 2
	while (i < n): #running loop until i is less than n 
		if n % i == 0: #check if i is a divisor of n 
			return False #if it is divisible stop 
		i += 1 #add 1 value to check for divisor
	return True #after loop is over when divisor is not found print true
print (is_prime (7)) #entering value 7 as n

def pronic(n): #find if a no. is pronic number
	i = 0
	while(i*(i+1)<n):
		if i*(i+1) == n: 
			return False
		i += 1
	return True
print (pronic(6))

def leap_year(n):
	if n % 400 == 0:
		print("Its a leap year!")
	elif n % 100 == 0 :
		print("Try again!")
	elif n % 4 == 0:
		print("Its a leap year!")
	else:
		print("Try again!")
leap_year(2988)

def math(n,m):
	a = n - m
	b = n + m
	return a, b
ans1 , ans2 = math(8,3)
def print_each_digit(n):
	while(n > 0):
		print(n%10)
		n = n // 10

def is_disarium(n):
	copy_n = n
	sum = 0 
	while(n > 0):
		sum += (n % 10) ** len(str(n))
		n = n // 10
	return sum == copy_n 
is_disarium(89)
