'''
Solution for Advent of Code Day 1

Find the Elves carrying the food with the most total calories.

https://adventofcode.com/2022/day/1
'''

import functools
import math

import click


class Elf(object):
    def __init__(self):
        self._calorie_inventory = []

    def add_calorie_item(self, item):
        self._calorie_inventory.append(item)

    def total_calories(self):
        return sum(self._calorie_inventory)


@click.command()
@click.argument('input', type=click.File('r'))
def main(input):
    '''
    Given an input file, finds the Elves carrying the food with the most total
    calories.
    '''
    elves = []

    current_elf = Elf()
    elves.append(current_elf)

    # Load in our input file
    for line in input:
        stripped_line = line.strip()

        if stripped_line == "":
            current_elf = Elf()
            elves.append(current_elf)
        else:
            value = int(stripped_line) # Always an int in the example input
            current_elf.add_calorie_item(value)

    sorted_elves = sorted(elves, key=Elf.total_calories, reverse=True)

    click.secho("Calories of top three Elves:", fg="cyan")
    for elf in sorted_elves[0:3]:
        click.secho(elf.total_calories(), fg="bright_black")

    click.echo()
    calorie_sum = sum([elf.total_calories() for elf in sorted_elves[0:3]])
    click.secho("Sum of top three Elves:", fg="green")
    click.secho(calorie_sum, fg="green", bold=True)
    

if __name__ == "__main__":
    main()