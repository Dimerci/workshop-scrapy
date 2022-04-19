##
## EPITECH PROJECT, 2021
## hub
## File description:
## exercice_1.py
##

for i in range(1, 101):
    if (i % 3 == 0 and i % 5 == 0):
        print("ThreeFive")
        continue
    if (i % 3 == 0):
        print("Three")
    if (i % 5 == 0):
        print("Five")
    else:
        print(i)