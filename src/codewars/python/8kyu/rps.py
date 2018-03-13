"""

Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples:

rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!

"""


def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    if p1 == "rock":
        result = p1_rock(p2)
    elif p1 == "scissors":
        result = p1_scissors(p2)
    else:
        result = p1_paper(p2)
    return result


def p1_rock(p2):
    if p2 == "paper":
        return "Player 2 won!"
    else:
        return "Player 1 won!"


def p1_scissors(p2):
    if p2 == "paper":
        return "Player 1 won!"
    else:
        return "Player 2 won!"


def p1_paper(p2):
    if p2 == "rock":
        return "Player 1 won!"
    else:
        return "Player 2 won!"
