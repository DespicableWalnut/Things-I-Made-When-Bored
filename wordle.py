import random
import time
import subprocess

def wordle():
    words = ["apple", "brave", "crate", "dance", "eagle", "flame", "gloom", "house", "ideal", "joker", "knock", "lemon", "mirth", "night", "ocean", "prize", "queen", "rough", "shine", "tiger", "usual", "vived", "wheat", "xerox", "yield", "zebra", "amber", "blaze", "craft", "drill", "elbow", "flute", "grasp", "haste", "ivory", "jolly", "kneel", "latch", "mover", "nudge", "orbit", "pivot", "quilt", "ripple", "slate", "tower", "unzip", "valve", "worry", "yodel"]
    word = random.choice(words)
    incheck1 = True
    incheck2 = True
    incheck3 = True
    incheck4 = True
    incheck5 = True

    def chooseword(word):
        #this does not choose the word it just makes it look cooler
        for i in range(1):
            print("choosing word.")
            time.sleep(1)
            subprocess.run('clear')
            print("choosing word..")
            time.sleep(1)
            subprocess.run('clear')
            print("choosing word...")
            time.sleep(1)
            subprocess.run('clear')

        print("Word chosen!!!")
       
    
    def correctCheck(word, geuss):
                incheck1 = True
                incheck2 = True
                incheck3 = True
                incheck4 = True
                incheck5 = True

                if word[0:1] == geuss[0:1]:
                    print("First letter is correct!!!")
                    incheck1 = False
                    
                if word[1:2] == geuss[1:2]:
                    print("Second letter is correct!!!")
                    incheck2 = False
                if word[2:3] == geuss[2:3]:
                    print("Third letter is correct!!!")
                    incheck3 = False
                if word[3:4] == geuss[3:4]:
                    print("Fourth letter is correct!!!")
                    incheck4 = False
                if word[4:5] == geuss[4:5]:
                    print("Fifth letter is correct!!!")
                    incheck5 = False
                if geuss[0:1] in word:
                        if incheck1:
                            print("First letter is in answer!!!")
                if geuss[1:2] in word:
                        if incheck2:
                            print("Second letter is in answer!!!")
                if geuss[2:3] in word:
                        if incheck3:
                            print("Third letter is in answer!!!")
                if geuss[3:4] in word:
                        if incheck4:
                            print("Fourth letter is in answer!!!")
                if geuss[4:5] in word:
                        if incheck5:
                            print("Fifth letter is in answer!!!")
                else:
                    print("You are completely wrong!!!")
    def geuss():
        while True:
                geuss = input(": ")
                if geuss == word:
                    print("Correct")
                    break
                else:
                    correctCheck(word, geuss)
        
    chooseword(word)    
    geuss()

if __name__ == '__main__':
    wordle()


        
