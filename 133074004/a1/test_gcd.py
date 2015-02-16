#testbench for gcd
from gcd import gcd
#functional assertion
assert gcd(48, 64) == 16
assert gcd(44, 19) == 1
print "Functional assertions passed"
#ValueError assertion
try:
	gcd(-1,2)
	gcd(1,-2)
except ValueError:
	print "ValueError assertion passed"
else:
	print "ValueError assertion failed"
#TypeError assertion
try:
	gcd('a',2)
	gcd(2,'b')
	gcd(2,'2222222222')
except TypeError:
	print "TypeError assertion passed"
else:
	print "TypeError assertion failed"
