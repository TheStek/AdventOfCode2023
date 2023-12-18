from part1 import hash


with open('input.txt', 'r') as file:
			input_data = file.read().split('\n')[0]


test = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
boxes = [[] for i in range(256)]


def execute_instruction(instruction):
	if '=' in  instruction:
		label, focal_len = instruction.split('=')
		loc = hash(label)

		for i in range(len(boxes[loc])):
			if boxes[loc][i][0] == label:
				boxes[loc][i][1] = focal_len
				break
		else:
			boxes[loc].append([label, focal_len])

	else:
		label = instruction.split('-')[0]
		loc = hash(label)
		for i in range(len(boxes[loc])):
			if boxes[loc][i][0] == label:
				boxes[loc].pop(i)
				break

def print_boxes(boxes):
	for i, box in enumerate(boxes):
		if len(box) > 0:
			print(f'Box {i}: {box}')



def get_total_focusing_power(bxs):
	total = 0
	for i, bx in enumerate(bxs):
		if len(bx) == 0:
			continue


		for j, (_, f) in enumerate(bx):
			total += (i+1) * (j+1) * int(f)

	return total





print(hash('ksns'))


for instruction in input_data.split(','):
	execute_instruction(instruction)

print_boxes(boxes)


print(get_total_focusing_power(boxes))

print(hash('cm'))

	