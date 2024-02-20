import datetime

first_date = datetime.date(2024, 4, 12)
second_date = datetime.date(2023, 4, 12)
between = first_date - second_date

print(between.days * 24 * 60 * 60)