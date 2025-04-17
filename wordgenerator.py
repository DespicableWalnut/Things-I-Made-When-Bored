import random
import subprocess

def wd():
    tries = input("How many tries do I get: ")
    tries = int(tries)
    x = 1
    b = "hi"
    vowels = ["a", "e", "i", "o", "u"] 
    weird = "y"
    consanents = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"] 

    def generateword():
        #generates a random assortment of consanents
        wordlength = random.randint(3, 9)
        word = ""
        a = -1
        b = 0
        for i in range(wordlength):
            letter = random.choice(consanents)
            word += letter

        word = list(word)

        for i in range(len(word)):
            replacechance = random.randint(2, 6)
            if replacechance == 2:
                word[i] = random.choice(vowels)
        word = ''.join(word)
        return word
    def ask():
        for i in range(tries):
            theword = generateword() 
            confirm = input(f"is {theword} a word? y/n: ")
            if "y" in confirm:
                print("hooray! I did it, and I am very proud of myself\nI will now say ", theword, " everywhere I go!!!")
                
            else:
                print("welp, atleast I tried. ):")
            subprocess.run('clear')
               
               
    ask()
if __name__ == '__main__':
    wd()
            

        
