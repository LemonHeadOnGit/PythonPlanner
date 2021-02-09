#   Version 0.1
print("Timetable Tracker")
print("What is the current day? Put 0 if its Friday.")
day = input()
day = int(day)  # This whole program doesn't work if I don't convert day into int.
#   Change for your personal timetable, remove any components if nessasary.
day1 = "Day 1 (Unconfigured)"
day2 = "Day 2 (Unconfigured)"
day3 = "Day 3 (Unconfigured)"
day4 = "Day 4 (Unconfigured)"
day5 = "Day 5 (Unconfigured)"
day6 = "Day 6 (Unconfigured)"
friday = "Friday (Unconfigured)"
#   And now some if statements.
if day == 1:
    print(day1)
if day == 2:
    print(day2)
if day == 3:
    print(day3)
if day == 4:
    print(day4)
if day == 5:
    print(day5)
if day == 6:
    print(day6)
if day == 0:
    print(friday)
#   End.

