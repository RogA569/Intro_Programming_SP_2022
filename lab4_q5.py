"""
This program displays a half times table from 1-10.
In others words, only half of the products from the normal 1-10 times table are displayed.
There's a 50% chance that a row may be displayed in reverse order.
"""

import random

for row in range(1, 11):
    row_sequence = "" # initialize empty string, that will contain a row of products
    if random.random() > 0.5:
        for product in range(1, row + 1):
            # 50% chance that the row will be in normal order
            row_sequence += str(row * product) + "\t"
    else:
        for product in range(row, 0, -1):
            # 50% chance that row will be in reverse order
            row_sequence += str(row * product) + "\t"
    print(row_sequence)