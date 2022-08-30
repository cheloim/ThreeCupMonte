#!/usr/bin/env python3.10

from random import shuffle


mylist = [' ', ' ', 'O']


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():

    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number 0, 1, or 2: ")

    return int(guess)


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Congratulations, you guess it")
    else:
        print("Wrong answer, better luke next time")
        print(mylist)


mylist = shuffle_list(mylist)
guess = player_guess()
check_guess(mylist, guess)
