# What Would Python Print

square = lambda x: x * x
def test(f, x):
	if f(x) % 2 == 0:
		return lambda g, x: g(square, x)
	else:
		return f(x)
print(test(lambda s: s // 2, 20)(test, 7))