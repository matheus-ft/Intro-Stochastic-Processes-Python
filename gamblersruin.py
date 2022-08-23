# This is slightly adapted, but the idea is generally the same

from numpy.random import choice
from numpy import mean


def ruin(starting_money: int, goal_amount: int, prob_win: float) -> bool:
    prob_lose = 1 - prob_win
    stake = starting_money
    while stake > 0 and stake < goal_amount:
        bet = choice([-1, 1], size=1, p=[prob_lose, prob_win])
        stake += bet
    if stake == 0:
        return True
    else:
        return False


def prob_ruin(starting_money: int, goal_amount: int, prob_win: float, trials: int):
    return mean([ruin(starting_money, goal_amount, prob_win) for _ in range(trials)])


starting_money = 20
goal_amount = 60
prob_win = 0.5
trials = 1_000
print(prob_ruin(starting_money, goal_amount, prob_win, trials))
