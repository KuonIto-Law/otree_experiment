from otree.api import Currency as c, currency_range
from . import *
from otree.api import Bot

class PlayerBot(Bot):
    def play_round(self):
        yield FirstPage, dict(choice_1='A')
        yield SecondPage, dict(choice_2='1')
