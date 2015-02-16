def gcd(a,b):
#gcd of two positive intergers of format int or long
	if a < 0 or b < 0:
		raise ValueError("Please specify positive arguments")
	else:
		try:
			a = int(a)
			b = int(b)
			while b:
				a, b = b, a%b
			return a	
		except ValueError:
			raise TypeError("arguments should be int or long type")	
