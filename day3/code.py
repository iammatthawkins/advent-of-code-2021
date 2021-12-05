def read_file() -> list[str]:

    with open('input.txt', 'r') as f:
        return [line for line in f.read().strip().split("\n")]


def part1(diagnostics: list[str]) -> int:

    number_diagnostics = len(diagnostics)
    bin_count = {i:0 for i in range(len(diagnostics[0]))}
    
    for binary in diagnostics:
        for i, character in enumerate(binary):
            if character == '1':
                bin_count[i] += 1

    gamma_rate, epsilon_rate = '0b', '0b'

    for value in bin_count.values():
        gamma_rate += '1' if value > number_diagnostics / 2 else '0'

    for value in bin_count.values():
        epsilon_rate += '1' if value < number_diagnostics / 2 else '0'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)
  

def return_rating(diagnostics: list, type: str) -> int:

    # make a copy of the list because lists pass by reference
    binary_list = [x for x in diagnostics]
    temp_binary = str()

    for i in range(len(binary_list[0])):

        # find the most common bit in first position
        common_bit_list = {0: 0, 1: 0}
        common_bit = str()

        for binary in binary_list:
            if binary is None:
                continue
            if binary[i] == '0':
                common_bit_list[0] += 1
            elif binary[i] == '1':
                common_bit_list[1] += 1

        if type == 'oxygen':
            if common_bit_list[0] > common_bit_list[1]:
                common_bit = '0'
            elif common_bit_list[0] < common_bit_list[1]:
                common_bit = '1'
            else: #if they are equal
                common_bit = '1'
        elif type == 'co2':
            if common_bit_list[0] < common_bit_list[1]:
                common_bit = '0'
            elif common_bit_list[0] > common_bit_list[1]:
                common_bit = '1'
            else: #if they are equal
                common_bit = '0'

        for j, binary in enumerate(binary_list):
            if binary is not None and binary[i] != common_bit:
                temp_binary = binary
                binary_list[j] = None
    
    final_binary = temp_binary
    for item in binary_list:
        if item is not None:
            final_binary = item

    return int(final_binary, 2)


def part2(diagnostics: list[str]) -> int: 

    oxygen_rating = return_rating(diagnostics, 'oxygen')
    co2_rating = return_rating(diagnostics, 'co2')

    return oxygen_rating * co2_rating


def test():
    test_input = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
    assert part1(test_input) == 198
    assert part2(test_input) == 230


if __name__ == '__main__':
    test()
    val = read_file()
    print(f'Answer to Day 1 Part 1 is {part1(val)}')
    print(f'Answer to Day 1 Part 2 is {part2(val)}')
