
from csv import reader

def read_file() -> list[int]:

    with open('input.csv', 'r') as input:
        csv_reader = reader(input)
        return [int(line[0]) for line in csv_reader]
            

def part1(measurements: list[int]) -> int:

    result = 0

    for i, measurement in enumerate(measurements):
        if i == 0:
            continue
        if measurement > measurements[i-1]:
            result += 1

    return result

def part2(measurements: list[int]) -> int:
    
    windows = dict()
    window_size = 3

    for i, measurement in enumerate(measurements):

        #create a new window group 
        if sum([i, window_size]) <= len(measurements):
            windows[i] = measurement
        
        #if after first element, go back and add measurement to previous
        if i > 0 and (i - 1) in windows:
            windows[i - 1] += measurement

        #if after second element 
        if i > 1 and (i - 2) in windows:
            windows[i - 2] += measurement

    return part1(list(windows.values()))


def test():
    test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert part1(test_input) == 7
    assert part2(test_input) == 5

if __name__ == '__main__':

    test()
    val = read_file()
    print(f'Answer to Day 1 Part 1 is {part1(val)}')
    print(f'Answer to Day 1 Part 2 is {part2(val)}')