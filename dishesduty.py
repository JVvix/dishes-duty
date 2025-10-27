#!/usr/bin/env python3
from datetime import date

start_date = date(2025, 10, 26)
current_date = date.today()

difference = start_date - current_date

day_difference = difference.days

if day_difference % 3 == 2:
    print("It's Faye's turn to do dishes today!")
elif day_difference % 3 == 0:
    print("It's Maxine's turn to do dishes today!")
else:
    print("It's Dad's turn to do dishes today!")

