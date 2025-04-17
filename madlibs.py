import random
import subprocess
#Not complete activity

def ml():
    #need more stories
    
    storys = ["""Story1: Pizza was invented by a [adjective1] [nationality1] chef named [person1]. To make a pizza, you need to take a lump of [noun1], and make a thin [adjective2] [noun2].
    Then you cover it with [adjective3] sauce, [adjective cheese1], fresh chopped [plural noun1]. Next you have to bake it in a very hot [noun3]. when it is done cut it into [number1] [shapes1].
    Some kids like [food1] pizza the best, but my favorite is the [food2] pizza. If I could, I would eat pizza [number2] of times a day""", 

    """Story2: Today I went to the zoo. I saw a [adjective1] [noun1] jumping up and down in its tree. He [past tense verb1] [adverb1] through the large tunnel that led to its [adjective2]
    [noun2]. I got some peanuts and passed them through the cage to a gigantic gray [noun3] towering above my head. Feeding that animal made me hungry. I went to get a [adjective3] scoop of ice cream. It filled my stomach. Afterwards I had to
    [verb2] [adverb2] to catch our bus. When I got home I [past tense verb2] my mom for a [adjective4] day at the zoo."""
                ]
    story = random.choice(storys)
        
    def replacewords(story):
        count = story.count("[")
        count += 1
        iterations = 0
        for i in range(count):
            iterations += 1
            if iterations == count:
                print(story)
                break
            start = story.find("[")
            end = story.find("]")
            end += 1
            word = story[start:end]
            print(story[start:end])
            replacewrd = input(":")
            story = story.replace(word, replacewrd)
            subprocess.run('clear')
        return story
        
    
    replacewords(story)

if __name__ == '__main__':
    ml()
