##
## EPITECH PROJECT, 2021
## hub
## File description:
## exercice_3.py
##

def anagrams(word, string):
    value = []

    for string in string:
        if sorted(string) == sorted(word):
            value.append(string)
    print(value)

anagrams('laser', ['lazing', 'lazy',  'lacer'])