from numpy import unique
from part1 import get_hand_rank as get_hand_rank_part_1

with open('input.txt') as file:
	input_data = file.read().split('\n')[:-1]

test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split('\n')


orders = {0: 'high card', 1: 'pair', 2: '2 pair', 3: '3 OAK', 4: 'full house', 5: '4 OAK', 6: '5 OAK'}


cards_map = {'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}

def get_card_order(card):
	return int(cards_map.get(card, card))

def parse_line(line):
	hand, bet = line.split(' ')
	return list(map(get_card_order, hand)), int(bet)


def get_hand_rank(hand):
	hand_without_jacks = list(filter(lambda x: x != 1, hand))
	jacks = len(hand) - len(hand_without_jacks)

	if jacks == 5:
		return 6

	if jacks == 0:
		return get_hand_rank_part_1(hand)

	unique_values, value_counts = unique(hand_without_jacks, return_counts = True)

	if max(value_counts) + jacks == 5:
		return 6

	if max(value_counts) + jacks == 4:
		return 5

	if jacks == 1:
		if len(value_counts) == 4:
			return 1

		if len(value_counts) == 3:
			return 3

		if len(value_counts) == 2:
			if max(value_counts) == 3:
				return 5
			else:
				return 4
	if jacks == 2:
		if len(value_counts) == 3:
			return 3

		if len(value_counts) == 2:
			return 5
	
	if jacks == 3:
		return 5
		
def order_hands(inp):
	raw_hands = list(map(parse_line, inp))
	hand_data = [[get_hand_rank(cards), cards, bet] for cards, bet in raw_hands]
	return sorted(hand_data)


total = 0
for rank, hand_data in enumerate(order_hands(input_data)):
	total += (rank + 1) * hand_data[2]
print(total)


