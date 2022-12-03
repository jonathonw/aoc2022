'''
Solution for Advent of Code Day 2

Rock Paper Scissors evaluator.

https://adventofcode.com/2022/day/2
'''

from enum import Enum

import click

# First column of input is what the opponent plays:
# A for Rock, B for Paper, C for Scissors
# Second column of input is what you play:
# Presumed to be X for Rock, Y for Paper, Z for Scissors

class RockPaperScissorsMove(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return (self.value - other.value) % 3 == 2

    def shape_score(self):
        return self.value + 1

    def next_move_from_strategy(self, my_str):
        if my_str == "X": # Need to lose
            return RockPaperScissorsMove((self.value - 1) % 3)
        elif my_str == "Y": # Need to draw
            return self
        elif my_str == "Z": # Need to win
            return RockPaperScissorsMove((self.value + 1) % 3)

    @classmethod
    def from_string(cls, input_str):
        if input_str == "A" or input_str == "X":
            return cls.ROCK
        elif input_str == "B" or input_str == "Y":
            return cls.PAPER
        elif input_str == "C" or input_str == "Z":
            return cls.SCISSORS


def evaluate_move_points(opponent_move, my_move):
    score = my_move.shape_score()

    if my_move > opponent_move:
        score += 6
    elif my_move == opponent_move:
        score += 3

    return score

@click.group()
def main():
    '''
    Given an input file, evaluates the score when playing Rock Paper Scissors
    using that strategy
    '''
    pass


@main.command()
@click.argument('input', type=click.File('r'))
def part1(input):
    '''
    Evaluate using strategy where our input maps X,Y,Z to Rock,Paper,Scissors respectively
    '''
    score = 0

    for line in input:
        stripped_line = line.strip()
        [opponent_str, my_str] = stripped_line.split(" ")
        opponent_move = RockPaperScissorsMove.from_string(opponent_str)
        my_move = RockPaperScissorsMove.from_string(my_str)

        score += evaluate_move_points(opponent_move, my_move)

    click.secho("Total score using this strategy:", fg="green")
    click.secho(score, fg="green", bold=True)


@main.command()
@click.argument('input', type=click.File('r'))
def part2(input):
    '''
    Evaluate using strategy where our input maps X,Y,Z to Lose,Draw,Win respectively
    '''
    score = 0

    for line in input:
        stripped_line = line.strip()
        [opponent_str, my_str] = stripped_line.split(" ")
        opponent_move = RockPaperScissorsMove.from_string(opponent_str)
        my_move = opponent_move.next_move_from_strategy(my_str)

        score += evaluate_move_points(opponent_move, my_move)

    click.secho("Total score using this strategy:", fg="green")
    click.secho(score, fg="green", bold=True)


if __name__ == "__main__":
    main()