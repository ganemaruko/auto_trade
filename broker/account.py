from abc import ABC


class Account(ABC):
    def __init__(self, initial_amount):
        self.amount = initial_amount