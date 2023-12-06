with open('input.txt') as file:
	input_data = file.read()[:-1]
parse_data = lambda inp: zip(*list(map(lambda x: list(map(int, x)), map(lambda x: list(filter(lambda x: all([y.isdigit() for y in x]) and x != '', x)),map(lambda x: x.split(' '),inp.split('\n'))))))
get_distance = lambda X: X[0]*(X[1] - X[0])
count_solutions = lambda time, distance: len(list(filter(lambda x: x>distance, map(get_distance, [(x, time) for x in range(time+1)]))))
print(list(map(lambda x: count_solutions(*x), parse_data(input_data))))
get_big_race = lambda inp: tuple(map(lambda x: int(''.join(list(filter(lambda y: y.isdigit(), x)))),inp.split('\n')))
print(count_solutions(*get_big_race(input_data)))

