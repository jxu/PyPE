# BIG MONEY BIG PRIZES

memo = dict()

def prizes(day, lates, last_absent):
    if lates < 0 or day < 0: return 0
    if day == 0: return 1

    if (day, lates, last_absent) in memo:
        return memo[(day, lates, last_absent)]

    strings =  prizes(day-1, lates, False)  # O
    strings += prizes(day-1, lates-1, False)  # L

    if not last_absent:  # Prevent runs of A longer than 2
        strings += prizes(day-1, lates, True)  # A
        strings += prizes(day-2, lates, True)  # AA

    memo[(day, lates, last_absent)] = strings
    return strings


print(prizes(30, 1, False))
