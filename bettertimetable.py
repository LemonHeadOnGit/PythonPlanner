#   Version 0.1.1
print("Better Timetable")
print("What is the current day? Put 0 if it's a day outside of the 1-6 range.")  # Changing "Put 0 if it's Friday".
day = input()
day = int(day)
#   Change for your personal timetable, remove any components if necessary.
#   Support for different configurations without modifying the code coming sometime later.
day1 = "Day 1 (Unconfigured)"
day2 = "Day 2 (Unconfigured)"
day3 = "Day 3 (Unconfigured)"
day4 = "Day 4 (Unconfigured)"
day5 = "Day 5 (Unconfigured)"
day6 = "Day 6 (Unconfigured)"
day0 = "Day 0 (Unconfigured)"
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
    print(day0)
#   End.
