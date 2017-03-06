print("welcome to the dungon. You cannot go back through the same way you came because the door is bulted shut from the outside. Your welcome for that by the way. You must find a way to escape. The only tool you have is your axe, if you ever want to use your axe type -use axe-")
print("You start walking and find your self in a big room. The room has three doors. What door do you want to go through?")
door =raw_input("-first door- second door- or -third door-?")
while(door != "third door"):
    print("incorrect choose again")
    door =raw_input("-first door- second door- or -third door-?")
print(" Correct... You have picked the right door.. You start walking and find yourself in a dark hallway.")

secondchoice =raw_input("Do You -keep walking- or try to -find a light sorce-? Be carful you dont want to wake something up!")
if(secondchoice == "find a light sorce"):
    print("You crawl around and find nothing so you start to feel the wall. you found the light switch and you turn it on. The light woke up my guard. Congrats you got yourself killed. GAMEOVER")     
elif(secondchoice == "keep walking"):
    print("You keep walking carefully through the hallway and finally reach a wooden door but its locked. How do you open it?"),
    halldoor =raw_input("HINT; What chops wood?") 
    while(halldoor != "use axe"):
        print("Didnt work. Try again") 
        halldoor =raw_input("HINT; What chops wood?")
    print("Correct: you knocked down the door. YOu find yourself walking in a huge empty room. you keep walking and fin yourself in the middle of the room.WAIT whats that. My guard has found you.")
thirdchoice =raw_input("Do you fight or run?")
if(thirdchoice == "run"):
	print("you have escaped the guard. but when he was chacing you he fell in a hole and died. He was the only one with the keys to escape.CONGRATS GAME OVER")
elif(thirdchoice == "fight"):
	print("Ok. you want to fight. All you have is your axe. He has full armor on but not a helmet. You can try to hit him with the axe or throw the axe")
fight =raw_input("throw or hit him with the axe")
if(fight == "hit"):
	print("You hit him. He has armor and hits you back you died")
elif(fight == "throw"):
    print("where do you want to throw?")
throw =raw_input("Head- chest-?")
if(throw == "chest"):
    print("Nope you suck he has armor your dead")
elif(throw == "head"):
	print("wow you won. my guards head is split open like a water melon. You deside to search him. You find a key and a map. You read the map and find your way to a door. But its looked. you use the key and the door opens. Congrats you have escaped. YOU WON")

