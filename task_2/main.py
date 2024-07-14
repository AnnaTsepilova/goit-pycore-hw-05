import re
from typing import Callable

def generator_numbers(text: str):
    '''
    Generator return float from text
    '''
    for word in text.split(' '):
        if re.match(r"\d", word):
            yield float(word)

def sum_profit(text: str, func: Callable):
    total_amount = 0
    for amount in func(text):
        total_amount += amount

    return total_amount


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
