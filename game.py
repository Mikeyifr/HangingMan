import random

def win(word1):
    for i in word1:
        if i == "_":
            return True
    return False

def display(word2):
    word2 = " ".join(word2)
    return word2

        
opt = ["deny", "smart", "random", "melon"]
word = list(opt[(random.randint(0, len(opt) - 1))])

hidden = []
for i in word:
    hidden.append("_")
print(display(hidden))

right = False
nog = 10 #number of guesses
while nog > 0 and win(hidden):
    guess = input("enter your guess: ")
    guess = guess.lower()
    for i in range(len(word)):
        if guess == word[i]:
            hidden[i] = guess
            right = True
    if right == False:
        nog -= 1
    right = False
    print(display(hidden))
    print(f"you have {nog} left")
if not win(hidden):
    print("Winner winner chicken dinner!")
elif nog == 0:
    print("Game Over! better luck next time")