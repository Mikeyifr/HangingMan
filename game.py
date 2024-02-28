import random

def win(word1):
    for i in word1:
        if i == "_":
            return False
    return True

def display(word2):
    word2 = " ".join(word2)
    return word2

def notdup(c, li):
    for i in li:
        if c == i:
            return False
    return True

        
opt = ["deny", "smart", "random", "melon"]
word = list(opt[(random.randint(0, len(opt) - 1))])

log = [] #list of guesses
hidden = []
for i in word:
    hidden.append("_")
print(display(hidden))
right = False
nog = 10 #number of guesses
while nog > 0 and not win(hidden):
    guess = input("enter your guess: ")
    if guess.isalpha():
        if len(guess) == 1:
            guess = guess.lower()
            if notdup(guess, log):
                for i in range(len(word)):
                    if guess == word[i]:
                        hidden[i] = guess
                        right = True
                if right == False:
                    nog -= 1
                right = False
                print(display(hidden))
                print(f"you have {nog} left")
            else:
                print("you've tried that one already")
        else:
            print("you can only enter one letter")
    else:
        print("you can only enter letters")
    log.append(guess)
    
if win(hidden):
    print("Winner winner chicken dinner!")
elif nog == 0:
    print("Game Over! better luck next time")