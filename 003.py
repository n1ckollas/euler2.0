def is_prime(num):
		prime = True
		x  = 2
		while x < num:
			if num % x == 0:
				prime = False
				break
			x += 1
		return prime



def prime_fator(num):
	factor = num - 1 
	while factor > 0:
		if num % factor == 0:
			if is_prime(factor):
				return factor
		factor -= 1
		print(factor)

print(prime_fator(600851475143))




