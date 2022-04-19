##
## EPITECH PROJECT, 2021
## hub
## File description:
## exercice_3.py
##

def anagrams(word, string):
    result = []
    for i in range(len(string)):
        if (len(word) == len(string[i])):
            result.append(string[i])
    for i in range(len(result)):
        for j in range(len(len(word)))

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])