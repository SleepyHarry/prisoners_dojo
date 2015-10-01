from axelrod.player import Player

from axelrod.strategies import demo_strategies as opponents

from random import choice
from itertools import count

# 	Cooperate	Defect
# Cooperate	(3,3)	(0,5)
# Defect	(5,0)	(1,1)

OUTCOMES = {
    'CC': ('You go to prison for two years, so does your opponent. '
           '(You both cooperated)'),
    'CD': ('You go to prison for five years, your opponent goes free. '
           '(You FOOLISHLY cooperated, whereas your oppenent stabbed you in the back.)'),
    'DC': ('You go free, your opponent goes to prison for five years. '
           '(You BASTARD. You stabbed your oppenent in the back when all he showed you was LOVE.)'),
    'DD': ('You go to prison for four years, so does your opponent. '
           '(You\'re both BASTARDS.)'),
}


class UserPlayer(Player):
    def __init__(self):
        super().__init__()

    def strategy(self, opponent):
        valid_strats = 'C D'.split()

        user_choice = ''
        while user_choice not in valid_strats:
            user_choice = input(
                'Pick a strategy ({}): '.format(
                    ', '.join(valid_strats)
                )
            ).upper()

        return user_choice

p1 = UserPlayer()
p2 = choice(opponents)()
# print(p2.name)

# p1.play(p2)
#
# print('You played {}, opponent played {}.'.format(
#     p1.history[-1], p2.history[-1]
# ))


def play():
    mode = ''

    while mode not in 'P G'.split():
        mode = input(
            'Would you like to [P]lay or [G]uess?: '
        ).upper()

    if mode == 'P':
        p1.play(p2)

        print(OUTCOMES[''.join(
            [p1.history[-1], p2.history[-1]]
        )])
        return

    # The user wants to guess
    possibles = [opp.name for opp in opponents]

    guess = ''
    while guess not in list(map(str, range(len(opponents)))):
        guess = input(
            '\nPick a number:\n{}\n\nGuess: '.format(
                '\n'.join('{}: {}'.format(i, x) for i, x in enumerate(possibles))
            )
        )

    if opponents[int(guess)].name == p2.name:
        return True
    return False

if __name__ == '__main__':
    for tries in count():
        result = play()
        if result is not None:
            break

    if result:
        print('Correct! ', end='')
    else:
        print('Incorrect. ', end='')

    print('You were playing against a {}.'.format(
        p2.name
    ))
    print('Only took you {} moves'.format(tries))

