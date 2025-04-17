import os
import random
import subprocess
import time
from geussthepin import gtp
from madlibs import ml
from wordle import wordle
from wordgenerator import wd
from turtlescript import theturtle
from partygame import party

greet = "hi"
help = "ctrl c to quit\nactivities list: mad-libs!, russian-roulette!, geuss-the-pin!, party-game!, wordle!, word-generator!\nhelp_advanced for advanced help"
help_advanced = "say command to run a normal command\nsay forever and then your command to make it go on forever or say go'int' where int is a number to make something run that amount of times"

def name():
    while True:
            name = input("name: ")
            password = input("password: ")
            if len(name) > 10:
                print("name is over character limit")
            else:
                try:
                    profile = open("profile.txt", "r")
                    procontents = profile.read()
                    if f"{name}:{password}" in procontents:
                        print("login succesful")
                        break
                    else:
                        print("It appears that the password or name you wrote do not match or exist")
                        fileask = input("do you want to create a new profile? y/n:")
                        if "y" in fileask:
                            profile = open("profile.txt", "a")
                            profile.write(f"{name}:{password}")
                            profile.close()
                            print("Info has been written")
                            break
                        else:
                            print("You will now continue as a geust")
                            break
                except FileNotFoundError:
                    print("It appears that the file does not exist or a different error occured")
                    fileask = input("do you want to create a new file and write your info? y/n:")
                    if "y" in fileask:
                        profile = open("profile.txt", "x")
                        profile.write(f"{name}:{password}")
                        profile.close()
                        print("Info has been written")
                        break
                    else:
                        print("ok\nYou will now continue as a geust")
                        break
    
def activitieslist():
    print("Welcome to my coding practice area!\ntype help! for help")
    act = "none"
    while True: 
        try:
            uia = input("type: ")
            
            if "help!" in uia:
                print(help)
            elif "geuss-the-pin!" in uia:
                #April 2 2025
                gtp()
            elif "mad-libs!" in uia:
                #April 6 2025
                ml()
            elif "wordle!" in uia:
                #April 8 2025
                wordle()
            elif "word-generator" in uia:
                #April 10 2025
                wd()    
            elif "turtle" in uia:
                #April 13 2025
                theturtle()
            elif "party-game!" in uia:
                #April 15 2025
                party()
            elif "clear" in uia:
                subprocess.run('clear')
            else:
                print("'", uia, "'", " is not a valid command")
                    
        

        except KeyboardInterrupt:
            print("exiting")
            break
        

name()
activitieslist()
