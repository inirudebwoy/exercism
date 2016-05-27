def is_leap_year(year):
    even_by_4 = not year % 4
    even_by_100 = not year % 100
    even_by_400 = not year % 400
    if even_by_4:
        if even_by_100:
            if even_by_400:
                return True
            return False
        return True
    return False
