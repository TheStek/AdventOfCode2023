

def hash(string):
	total = 0
	for char in string:
		total += ord(char)
		total *= 17
		total %= 256
	return total


if __name__ == '__main__':

	print(hash('HASH'))


	test = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

	with open('input.txt', 'r') as file:
			input_data = file.read().split('\n')[0]
	print(input_data)
	print(input_data)

	print(sum(map(hash, input_data.split(','))))