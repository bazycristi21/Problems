n = 19
result = [0]*1000

def is_prime(number):
	if number < 2:
		return False

	i = 2
	while i**2 <= number:
		if not number % i:
			return False
		i += 1
	return True


def split_bt(number, k):
	if number == 0:
		for element in result[1:]:
			if element == 0:
				break
			print(element, end=' ')
		print()
	elif number < 0:
		return
	else:
		for i in range(result[k - 1], n):
			if is_prime(i):
				result[k] = i
				k += 1
				number -= i
				split_bt(number, k)
				result[k] = 0
				number += i
				k -= 1

split_bt(n, 1)
