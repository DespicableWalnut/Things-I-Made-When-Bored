import random 
import subprocess

def party():
    words = ["transporation", "morning routine", "Jim Tiffen"]
    questions = ["Do you use or do this everyday?", "Would you eat this", "Would you keep this in a garage"]

    specialword = random.choice(words)
    playernum = 0
    playernum1 = 0

    playernames = {
        
    }
    playerVotes = {

    }
    # get player data
    specialword = random.choice(words)
    playernum = 0
    playernum = 0
    print("Hello! Welcome to [game].")
    print("3 players min")
    while True:
        playerAmount = int(input("How many players? "))
        if playerAmount >= 2:
            print("too little! try again")
        else:
            break
    badplayernum = random.randint(1, playerAmount)
    for i in range(playerAmount):
            playernum1 += 1
            name = input("type each player's name individualy: ")
            playernames[f"player{str(playernum1)}"] = name
    for i in range(playerAmount):
        playernum += 1
        passname = playernames[f"player{str(playernum)}"]
        print(f"Pass the device to {passname}")
        input("press enter to continue!")
        if playernum == badplayernum:
            badplayer = f"player{str(i)}"
            print("You are the bad player")
            input("press enter to continue")
            subprocess.run('clear')
        else:
            print(f"The special word is {specialword}!!!")
            input("press enter to continue")
            subprocess.run('clear')
    # Questions
    targets = list(playernames)
    random.shuffle(targets)
    askers = list(playernames)
    random.shuffle(askers)
    #plus one because it skipped a question for some reason
    for i in range(playerAmount):
        askernum = askers[i]
        asker = playernames[askernum]
        targetnum = targets[i]
        target = playernames[targetnum]
        while asker == target:
            random.shuffle(targets)
            targetnum = targets[i]
            target = playernames[targetnum]
        print(f"{asker} ask {target} {random.choice(questions)}")
        input("press enter to continue")
        subprocess.run('clear')

    #voting
    for i in range(playerAmount + 1):
        if i == 0:
            continue
        voter = f"player{i}"
        voternickname = playernames[voter]
        print(f"pass the device to {voternickname}")
        input("press enter to continue")
        availableplayers = playernames.copy()
        del availableplayers[voter]
        availableplayersnum = ', '.join(f"{b} ({value})" for b, value in availableplayers.items())
        print(f"players: {availableplayersnum}")
        print("type in there player key; EX. Player1")
        addvote = input("who would you like to vote for: ")
        if addvote in availableplayers:
            if addvote not in playerVotes:
                playerVotes[addvote] = 0
            playerVotes[addvote] += 1
            availableplayers = playernames.copy()
            subprocess.run('clear')
        else:
            print("invalid vote!!!")
            input("press enter to continue")
    #find loser
    max_votes = -1
    trueloser_key = ""

    for i in range(playerAmount):
        key = f"player{str(i + 1)}"
        try:
            votes = playerVotes[key]
        except:
            continue
        if votes > max_votes:
            max_votes = votes
            trueloser_key = key
    #the grand reveal
    print(f"{playernames[trueloser_key]}/{trueloser_key} recieved the most votes")
    print(f"The true bad player was {playernames[badplayer]}/{badplayer}")
    
if __name__ == '__main__':
    party()
            