
def valid_level(year):
    if year and year.isdigit():
        if int(year) in range(1, 7):
            return True
    return False