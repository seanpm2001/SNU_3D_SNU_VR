# SunBlock (A test VR game for SNU)
# Start of script
import 
print ("SunBlock - VR game")
''' Lists '''
# Difficulty list
difficultyList = []
difficultyList.append("1 Difficulty") # Very easy
difficultyList.append("2 Difficulty") # Easy
difficultyList.append("3 Difficulty") # Slightly easy
difficultyList.append("4 Difficulty") # Barely easy
difficultyList.append("5 Difficulty") # Hardly easy
difficultyList.append("6 Difficulty") # Medium
difficultyList.append("7 Difficulty") # Intermediate
difficultyList.append("8 Difficulty") # Difficult
difficultyList.append("9 Difficulty") # Hard
difficultyList.append("10 Difficulty") # Pretty hard
difficultyList.append("11 Difficulty") # Very hard
difficultyList.append("12 Difficulty") # Hardcore
# Item list
itemList = []
itemList.append("Sunscreen")
itemList.append("Sunglasses")
# Score-counters
highScore1 = int(0)
highScore2 = int(0)
highScore3 = int(0)
highScore4 = int(0)
highScore5 = int(0)
curScore = int(0)
multiplier1 = int(1) # Goes up to 12
# Sun
sunSpeed = int(1)
time1 = int(0)
dayCounter = int(0)

''' Definitions '''
# Actions
def sleeping():
	print ("Sleeping...")

def bedTime():
	print ("Going to bed")

# Objects
def sunMove():
	# Sun
	
def playerBed():
	if (time1 == 12000):
		print ("It is time for bed")
		bedTime()
		time1 = int(0)
		dayCounter = dayCounter + 1
# Difficulties
def difficulty1():
	delay1 = int(12)
	
def difficulty2():
	delay2 = int(11)

def difficulty3():
	delay3 = int(10)

def difficulty4():
	delay4 = int(9)
	
def difficulty5():
	delay5 = int(8)
	
def difficulty6():
	delay6 = int(7)

def difficulty7():
	delay1 = int(6)
	
def difficulty8():
	delay2 = int(5)

def difficulty9():
	delay3 = int(4)

def difficulty10():
	delay4 = int(3)
	
def difficulty11():
	delay5 = int(2)
	
def difficulty12():
	delay6 = int(1)

# Object stats
def sunglassesDur():
	sunglassesDurability = int(300)

def sunScreenDur():
	sunscreenDurability = int(500)

def playerHealth():
	if (delay1 = 12):
		health1 = int(11000)
	if (delay2 = 11):
		health1 = int(10000)
	if (delay3 = 10):
		health1 = int(9000)
	if (delay4 = 9):
		health1 = int(8000)
	if (delay5 = 8):
		health1 = int(7000)
	if (delay6 = 7):
		health1 = int(6000)
	if (delay7 = 6):
		health1 = int(5000)
	if (delay8 = 5):
		health1 = int(4000)
	if (delay9 = 4):
		health1 = int(3000)
	if (delay10 = 3):
		health1 = int(2000)
	if (delay11 = 2):
		health1 = int(1000)
	if (delay12 = 1):
		health1 = int(500)
'''
Original concept
Test VR program: the sun
Difficulties:
Very easy (sun speed: 1) 1x score
Easy (sun speed: 2) 2x score
Medium (sun speed: 3) 3x score
Hard (sun speed: 4) 4x score
Very hard (sunspeed: 5) 5x score
Custom (sunspeed: 6 to 12) 6x to 12x score
Items:
Sunglasses - Durability depends on game mode |very easy: durability: 1200, custom 12: durability: 100)
Sunscreen - prevents sunburns, you only get 1 bottle per week, and you have to be careful applying it
Sun speed and health
Sun speed, 1 = 1 meters per second
Max = 12 meters per second
player health: 1000-12000 (depending on difficulty)
Day length: 1200 meters of sun movement (min: 100 seconds (1 minute 40 seconds) max 1200 seconds (20 minutes))
Objectives:
Walk around, collect coins
Gain a high score
Sleep at night
Survive and enjoy the sunrise with a friend
Look at art near the sun
Don't die from burning
Sunburns:
Does 1 damage per second
Effects of looking at the sun:
2 seconds: black circles
4 seconds: squiggly lines
10 seconds: greyscale vision
20 seconds: blind
When you go blind, it is game over
Sunglasses let you look at the sun partially, and it gives you an extra 2 seconds per second for effect damage
'''
# End of script