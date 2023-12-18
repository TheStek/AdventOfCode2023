
test = '?###???????? 3,2,1'

def parse_line(line):
    string, nums = line.split(' ')
    nums = list(map(int, nums.split(',')))
    return string, nums


def get_combos(string, nums):
    print(string, nums)

    if len(string) < sum(nums):
        return 0

    if len(nums) == 0:
        return 1

    if len(string) == 0:
        if len(nums) == 0:
            return 1
        return 0

    if string[0] == '.':
        return get_combos(string[1:], nums)

    if string[0] == '?':
        return get_combos('.' + string[1:], nums) + get_combos('#' + string[1:], nums)

    if string[0] == '#':
        first_group = string[:nums[0] + 1]
        if '.' not in first_group[:-1] and first_group[-1] in ('?.'):
            print(f'Trimming {string} to {string[nums[0]: + 1]}')
            return get_combos(string[nums[0] + 1:], nums[1:])
        else:
            return 0

print(get_combos(*parse_line(test)))