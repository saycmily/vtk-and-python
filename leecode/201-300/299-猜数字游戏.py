class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret = list(secret)
        guess = list(guess)
        n = len(secret)
        A, B = 0, 0
        for i in range(n):
            if secret[i] == guess[i]:
                A += 1
                secret[i] = 'x'
                guess[i] = 'x'
        for i in range(n):
            if secret[i] == 'x':
                continue
            if secret[i] in guess:
                y = guess.index(secret[i])
                B += 1
                secret[i] = 'x'
                guess[y] = 'x'
        return str(A)+'A'+str(B)+'B'
