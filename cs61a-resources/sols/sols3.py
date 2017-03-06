# What Would Python Print?
[[x for x in range(y)] for y in range(3)]

#Implement the following function
def pairs_to_dict(pairs):
	"""
	Convert a list of pairs into a dictionary.
	>>> p = [['c', 6], ['s', 1], ['c', 'a']]
	>>> pairs_to_dict(p)
	{'c': 'a', 's': 1}
	"""
	result = {}
	for p in pairs:
		result[p[0]] = p[1]
	return result