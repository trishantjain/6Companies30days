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
                    
