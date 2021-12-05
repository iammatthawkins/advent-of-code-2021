from enum import Enum, auto
from collections import namedtuple


class Direction(Enum):
    forward = auto()
    down = auto()
    up = auto()


Command = namedtuple('Command', ['direction', 'units'])


def read_file() -> list:

    list_of_commands = list()

    with open('input.txt', 'r') as f:

        temp_list = [line.split() for line in f.read().strip().split("\n")] 
            
        for line in temp_list:
            list_of_commands.append(Command(Direction[line[0]], int(line[1])))

    return list_of_commands



def part1(commands: list[Command]) -> int: 

    depth, horizontal = 0, 0

    for command in commands:
        if command.direction == Direction.forward:
            horizontal += command.units
        elif command.direction == Direction.up:
            depth -= command.units
        elif command.direction == Direction.down:
            depth += command.units

    return depth * horizontal
    

def part2(commands: list[Command]) -> int: 

    depth, horizontal, aim = 0, 0, 0

    for command in commands:
        if command.direction == Direction.forward:
            horizontal += command.units
            depth += (aim * command.units)
        elif command.direction == Direction.up:
            aim -= command.units
        elif command.direction == Direction.down:
            aim += command.units

    return depth * horizontal

def test():
    test_input = [
         Command(Direction.forward, 5)
        ,Command(Direction.down, 5)
        ,Command(Direction.forward, 8)
        ,Command(Direction.up, 3)
        ,Command(Direction.down, 8)
        ,Command(Direction.forward, 2)
    ]

    assert part1(test_input) == 150
    assert part2(test_input) == 900


if __name__ == '__main__':

    test()
    val = read_file()
    print(f'Answer to Day 1 Part 1 is {part1(val)}')
    print(f'Answer to Day 1 Part 2 is {part2(val)}')