# Daniel Liers

# This program will be a close simulation of a baseball game you will be able to choose your own teams, jerseys, and how you want the game to play out
# You get to choose your pitches and even interact with throwing mechanics
# At the end of every inning you will be able to see to the statistics for that top or bottom of the inning
# As the code continues it will go more into detail and will be able to mess around you as a hitter
# Sources: w3schools


print("Welcome to Python Baseball Simulator 2022")

team = input("Choose your MLB Team:")
print("Good choice you have chosen the: " + team)

uniform = input("Now choose your uniform colors:")
print(uniform + " are some nice colors")

location = input("Would you like to be Home or Away")
print("Looks like you will be playing " + location)

print("Loading....")
begin = input("Press any button then ENTER to start")

print("Top of the 1st inning you are pitching")
pitchType = input("Please select a pitch: Fastball, Curveball, Slider")
print(pitchType + " inside the zone STRIKE 1!!!")
pitchType = input("Please select a pitch: Fastball, Curveball, Slider")
print(pitchType + " inside the zone STRIKE 2!!!")
pitchType = input("Please select a pitch: Fastball, Curveball, Slider")
print("The batter fouls off the ball, the count is now: 0-2")
pitchType = input("Please select a pitch: Fastball, Curveball, Slider")
print("STRIKE 3!!! You now have 1 out:")
pitchType = input("Please select a pitch: Fastball, Curveball, Slider")
print("Its going far and deep ANDDDDD OUT OF HERE HOME RUN!!!")
# simple input and print statements
batspeed1 = 80

print(float(batspeed1 * 1.5), end='')
# this statement will execute the 1.5 since it is a float statement and the end will combine the
# print statement below and on top onto one line
print(" mph exit velocity off the bat")

print("The rival team is winning 1-0")

pitchType = input("Please select a pitch: Fastball, Curveball, Slider")

throwingmechanic = input("Ground ball to second base: PRESS a then ENTER to throw!!!")
print("Sweet throw you now have 2 outs!")
armspeed1 = 92

print((armspeed1 - 6), end='')
print(" mph throw to first base")
# simple calculations done with the - operator and end parameter used to print all on one line.

pitchType = input("Please select a pitch: Fastball, Curveball, Slider")
print("Ball 1 outside!!!")
pitchType = input("Please select a pitch: Fastball, Curveball, Slider")
print("Swing and a Miss STRIKE 1: The count is now 1-1")
pitchType = input("Please select a pitch: Fastball, Curveball, Slider")
throwingmechanic2 = input("Ground ball to the shortstop: PRESS a then ENTER to throw!!!")
print("Oh no bad throw runner advances to second base: You have 2 OUTS with a runner on second base!")
pitchType = input("Please select a pitch and speed: Fastball, Curveball, Slider")
print("FLY ball to the third baseman for 3 OUTS!!!")

choiceString = input("Would you like to continue playing: Press 1 for YES or 2 for NO: ")
choice = int(choiceString)
if choice == 1:
    print("Ok awesome lets continue... Here are some statistics for the Top of the 1st inning!!")
else:
    print("Thanks for playing Python Baseball Simulator 2022 you did GREAT!!!")
    exit()
# The use of if else statements if user types 1 to keep playing it will print lets continue else will print thanks for playing

print("First batter OUT on strikes")
exitVelo2 = 120
timeTraveled = 3
print("Second batter Home Run 120.0 mph exit velocity...Projected distance ", end='')
print(exitVelo2 * timeTraveled, "feet to left field")
# variable exitVelo2 and timeTraveled are mulitplied uing the * operator
print("Third batter ground ball to second base for the 2nd out")
print("Fourth batter ground ball to shortstop... Error by shortstop runner advances to second")
print("Fifth batter fly ball to the third baseman to end the inning")
totalBases = 6
hits = 1
plateAppearances = 5
runs1 = 1
print("Opposing team stats: Total Bases: ", totalBases, end='')
print("  Batting Average ", hits / plateAppearances, end='')
print("  Total Hits: ", hits, end='')
print("  Runs Scored: ", runs1, sep=' A total of ')
print()


print("Now we will begin the bottom of the 1st your up to bat!")
batString = input("Which bat would you like to use bat 1 or 2? ")


bat = int(batString)
if bat == 1:
    print("Bat 1 is awesome for contact hitters!")
elif bat != 1:
    print("Nice you've picked bat 2 I heard this one hits BOMBS!")

print("Now up to bat the " + team)
print()
swing = input("Here comes the first pitch type 1 to swing the bat: ")
print("Base hit up the middle for a single to kick things off NICE!!!")

print()
swing = input("Ok you've got a runner on first and no outs here comes the first pitch type 1 to swing the bat: ")
print("AGHHH swing and a miss you have one strike")
swing = input("You have one strike on you here comes the second pitch type 1 to swing the bat: ")
print("That ball is going deep and deeper and OUTTA OF HERE HOME RUN!!!")
x = 1
while x <= 2:
    print(x)
    x+= 1
print("You scored 2 runs awesome they posted on the scoreboard above! You are now winning 2-1 ")
#while loops to post the amount of runs scored from the home run
crowdChant = ["Lets Go",team]
for x in crowdChant :
  print(x)
#for loops to express the crowd chanting
swing = input("The crowds cheering you on cmon lets keep this momentum going here comes the first pitch type 1 to swing")
print("Ground ball back to the pitcher he threw you out you have one out now")

str_1 = ("It seems like the opposing pitcher is a little startled  \nthey have called for a mound visit they got a minute on the clock")
print(str_1)
for y in range(0,70,10):
    print (y)
else:
    print("Ok times up get ready for your 4th batter")
swing = input("Ok here comes the first pitch type 1 to swing")
print("Ouch swing and a miss you got 1 strike on you")
swing = input("Ok here comes the second pitch type 1 to swing")
print("Ouch swing and a miss you got 2 strikes on you")
swing = input("Ok here comes the third pitch type 1 to swing")
print("Good morning, Good afternoon, Goodnight strike 3 you are out your team has 2 out on you...")
print()

def main():
    print("Alright you've gotta be smart you got 2 outs on you")

main()

swing = input("Ok here comes the first pitch lets take this pitch type 2: ")
print("Good eye that's ball 1 count is 1-0")

swing = input("Ok you got 1 ball on you your ahead of the count lets swing type 1 to swing: ")
print("Foul ball down the third baseline good swing though!")

swing = input("The counts 1-1 your team is relying for a hit here! type 1 to swing: ")
print()
print("Ground ball to the shortstop oh no he threw you out that concludes the first inning...")
print()
choiceString = input("Would you like to continue playing: Press 1 for YES or 2 for NO: ")
choice = int(choiceString)
if choice == 1:
    print("Ok awesome lets continue... Here are some statistics for the bottom of the 1st inning!!")
else:
    print("Thanks for playing Python Baseball Simulator 2022 you did GREAT!!!")
    exit()

runsScored = 2
print()
print("You put up two runs nice!:", runsScored > 1 and runsScored < 5)

atBats = 5
print("You had a total of 5 at bats!:", atBats > 3 or atBats < 4)

totalBases1 = 5
print("You had a total of 5 bases that included that one BOMB!!! and the single!:", not(totalBases1 > 5 and totalBases1 < 5))
#Simple boolean operators being used

print()
for x in range (27, 42, 3):
      print(x)
pitcherSelection = input("Next we will be starting the top of 2nd and you will be pitching \nPlease choose a pitcher from the selection of jersey numbers:")

print()
print("Ok awesome you've picked number " + pitcherSelection, "to pitch for you in the top of the second inning")




