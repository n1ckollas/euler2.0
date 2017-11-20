def is_prime(num):
		prime = True
		for x in:
			if num % x == 0:
				prime = False
		return prime

# print(is_prime(600851475143))

def prime_fator(num):
	factor = num - 1 
	while factor > 0:
		if is_prime(factor):
			return factor
		factor -= 1

# print(prime_fator(600851475143))




