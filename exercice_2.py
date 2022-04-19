##
## EPITECH PROJECT, 2021
## hub
## File description:
## exercice_2.py
##

def calculate(string):
    value = []
    for i in range(len(string)):
        if (isinstance(string[i], int) or len(string) == 1):
            print("False")
            exit(84)
        else:
            value.append(string[i])
    result = 0
    for i in range(len(string)):
        if (string[i] <= '0' or string[i] >= '9'):
            continue
        result += int(string[i])
    print(result)

calculate(['nothing', '1', '2'])