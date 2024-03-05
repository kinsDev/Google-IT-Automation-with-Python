def find_total_days(years, months, days):
    my_days = (years * 365) + (months * 30) + days
    return my_days


print(find_total_days(2, 5, 23))
