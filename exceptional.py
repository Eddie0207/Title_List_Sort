DIGIT_MAP = { 'zero' : '0',
			   'one' : '1',
			   'two' : '2',
			   'three': '3',
			   'four': '4',
			   'five' : '5',
			   'six' : '6',
			   'seven': '7',
			   'eight': '8',
			   'nine' : '9',
			   'ten' : '10',}

def convert(s):
	x=-1
	try:
		number = ''
		for token in s:
			number += DIGIT_MAP[token]
		x= int(number)
		print (f"Converstion succeeded! x={x}")
	except (KeyError, TypeError):
		print ("Conversion Failed!")
	return x

d = ("one three nine six")
x = convert(d.split())
print(x)

e = ('one and two')
y = convert(e.split())
print(y)