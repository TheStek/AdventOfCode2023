from numpy import unique

with open('input.txt') as file:
	input_data = file.read().split('\n')[:-1]

test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split('\n')


cards_map = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def get_card_order(card):
	return int(cards_map.get(card, card))

def parse_line(line):
	hand, bet = line.split(' ')
	return list(map(get_card_order, hand)), int(bet)

def get_hand_rank(hand):
	unique_values, value_counts = unique(hand, return_counts = True)

	if len(unique_values) == 1:
		return 6

	if len(unique_values) == 2:
		if max(value_counts) == 4:
			return 5
		
		return 4

	if len(unique_values) == 3:
		if max(value_counts) == 3:
			return 3 

		return 2

	if len(unique_values) == 4:
		return 1

	return 0



def order_hands(inp):
	raw_hands = list(map(parse_line, inp))
	hand_data = [[get_hand_rank(cards), cards, bet] for cards, bet in raw_hands]
	return sorted(hand_data)

if __name__ == '__main__':

	total = 0
	for rank, hand_data in enumerate(order_hands(input_data)):
		total += (rank + 1) * hand_data[2]
	print(total)

	print(order_hands(test_input))



