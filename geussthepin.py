import random

#mostly complete activity

def gtp():
	print("ctrl+c to quit")
	def makepin(pin):
		nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		pin = random.choice(nums), random.choice(nums), random.choice(nums), random.choice(nums)
		return str(pin)
	def removebad(pin):
		pin = pin.replace("(", "")
		pin = pin.replace(")", "")
		pin = pin.replace(",", "")
		if "T" in pin:
			ishint = True #This line means nothing it is just here so that I dont get an error
		else:
			pin = pin.replace(" ", "")
		pin = pin.replace("'", "")
		return pin
	def hint():
		hints = [["The first num is ", pin[0:1]], ["The second num is ", pin[1:2]], ["The third num is ", pin[2:3]], ["The fourth num is ", pin[3:4]]]
		hint = str(random.choice(hints))
		print(removebad(hint))
	def correctCheck(pin, geuss):
                if pin[0:1] == geuss[0:1]:
                    print("First digit is correct!!!")
                if pin[1:2] == geuss[1:2]:
                    print("Second digit is correct!!!")
                if pin[2:3] == geuss[2:3]:
                    print("Third digit is correct!!!")
                if pin[3:4] == geuss[3:4]:
                    print("Fourth digit is correct!!!")
                else:
                    print("You are completely wrong!!!")
                
                
	x = 1
	pin = removebad(makepin(x))
	trys = 0


	while True:
		try:
				if trys == 8:
					print("resetting pin...")
					pin = removebad(makepin(x))		
				geuss = input(": ")
							
				if geuss == pin:
					print("CORRECT!!!")
					break
				else:
					correctCheck(pin, geuss)
					ask = input("Try again? y/n: ")

					if "y" in ask:
						print("Ok")
					elif "hint" in ask:
						hint()
					else:
						break
					trys += 1
		except KeyboardInterrupt:
			print("It was ", pin)
			break


if __name__ == '__main__':
	print("ctrl+c to quit")
	gtp()

