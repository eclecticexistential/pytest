def get_name(x):
	array = []
	x = list(x)
	for item in x:
		try:
			int(item)
		except ValueError:
			array.append(item)
	return ('').join(array)

def test_answer():
    assert get_name("Jessica123") == "Jessica"