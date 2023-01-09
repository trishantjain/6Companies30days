'''
    --> LeetCode 299.: --Bulls and Cows-- 

    Ques. You are playing the Bulls and Cows game with your friend.

          You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

            The number of "bulls", which are digits in the guess that are in the correct position.

            The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

        Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

        The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

'''

from typing import Optional, List
from collections import Counter

class Solution:

    def getHing(self, secret, guess):
        bulls, cows = 0, 0
        secret_count, guess_count = Counter(secret), Counter(guess)

        for idx in range(len(secret)):
            if secret[idx] == guess[idx]:
                secret_count[secret[idx]] -= 1
                guess_count[guess[id]] -= 1
                bulls += 1

        for char, freq in secret_count.items():
            if freq > 0:
                freq_guess = guess_count[char]

                if freq_guess > freq:
                    cows += freq
                else:
                    cows += freq_guess

        return str(bulls)+"A"+str(cows)+"B"
                    
