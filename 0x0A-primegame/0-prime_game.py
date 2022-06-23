#!/usr/bin/python3
'''
Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a prime
number from the set and removing that number and its multiples from
the set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.

- Prototype: def isWinner(x, nums)
- where x is the number of rounds and nums is an array of n
- Return: name of the player that won the most rounds
- If the winner cannot be determined, return None
- You can assume n and x will not be larger than 10000
- You cannot import any packages in this task
'''


def isWinner(x, nums):
    '''
    Returns the name of the winner
    '''
    winner = []
    for num in nums:
        winner.append(roundWinner(x, num))
    if winner.count('Ben') > (len(winner)/2):
        return 'Ben'
    return 'Maria'


def roundWinner(x, num):
    '''
    Calculates who wons every round
    '''
    if num == 1:
        return 'Ben'
    if num == 2:
        return 'Maria'
    prime_numbers = 1
    for n in range(3, num + 1):
        i = 1
        not_prime = 0
        while (n - i) >= 2:
            if n % (n - i) == 0:
                not_prime += 1
            i += 1
        if not_prime == 0:
            prime_numbers += 1
    if prime_numbers % 2 == 0:
        return 'Ben'
    return 'Maria'
