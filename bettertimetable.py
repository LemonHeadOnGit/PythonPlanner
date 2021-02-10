#   BetterTimetable: Version 0.1.2
#   Change for your personal timetable, remove any components if necessary but do not remove Day 1.
#   Support for different configurations without modifying the code coming sometime later.
print("BetterTimetable - Alpha 1")
print()
config = open("config.txt", "w")
file = input("Would you like the Normal view (1) or [CONCEPT] Clear view. (0)\n")
config.write(file)
config.close()
open1 = open("config.txt", "r")
day1 = "[Day 1] (Unconfigured)"
day2 = "[Day 2] (Unconfigured)"
day3 = "[Day 3] (Unconfigured)"
day4 = "[Day 4] (Unconfigured)"
day5 = "[Day 5] (Unconfigured)"
day6 = "[Day 6] (Unconfigured)"
day0 = "[Day 0] (Unconfigured)"
if day1 == "[Day 1] (Unconfigured)":
    print("Status -- Unconfigured, please change code.")    #   If you're getting this error change Day 1 or configure your timetable.
else: print("Select the day and we'll show you your schedule.")
day = input()
day = int(day)
file = int(file)
if file == 0: 
    day1 = "[Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
    day2 = "[Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
    day3 = "[Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
    day4 = "[Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
    day5 = "[Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
    day6 = "[Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
    day0 = "[Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
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
