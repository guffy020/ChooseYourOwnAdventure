print("Hey you, wake up...good.. I have kidnapped you from your home and brought you to my warehouse. Dont worry, im not going to kill you. You will do that to yourself.  You cannot go back through the same way you came because the door is bulted shut from the outside. Your welcome for that by the way. You must find a way to escape... if you do your free to go. Heres an axe you might need it, if you ever want to use your axe type -axe- GOOD LUCK")
print("You start walking and find yourself in a big room. The room has three doors. What door do you want to go through?")
door =raw_input("-first door- second door- or -third door-?")
while(door != "third door"):
    print("Door is locked choose again")
    door =raw_input("-first door- second door- or -third door-?")
print(" Correct... You have picked the right door.. You start walking and find yourself in a dark hallway. Do you hear that. It sounds like snoring.")

secondchoice =raw_input("Do You -keep walking- or try to -find a light source-? Be carful you dont want to wake something up!")
if(secondchoice == "find a light source"):
    print("You crawl around and find nothing so you start to feel the wall. you found the light switch and you turn it on. The light woke up my guard. Congrats you got yourself killed. GAMEOVER")     
elif(secondchoice == "keep walking"):
    print("You keep walking carefully through the hallway and finally reach a wooden door but its locked. How do you open it?"),
    halldoor =raw_input("HINT; What chops wood?---") 
    while(halldoor != "axe"):
        print("Didnt work. Try again") 
        halldoor =raw_input("HINT; What chops wood?")
    if(halldoor == "axe"):
        print("Correct: you knocked down the door. You find yourself walking in a huge empty room. You keep walking and find yourself in the middle of the room. WAIT whats that behind you. My guard has found you. As he approches you, you notice a key and a map on his belt.")
        thirdchoice =raw_input("Do you fight or run?")
        if(thirdchoice == "run"):
            print("you have escaped the guard. but when he was chacing you he fell in a hole and died. He was the only one with the keys to escape.CONGRATS GAME OVER")
        elif(thirdchoice == "fight"):
            print("Ok. you want to fight. All you have is your axe. He has full armor on but not a helmet. You can try to hit him with the axe or throw the axe")
            fight =raw_input("throw or hit--")
            if(fight == "hit"):
                print("You walked up to him to try and hit him. when you got close to him he hit you and you died")
            elif(fight == "throw"):
                print("where do you want to throw?")
                throw =raw_input("Head- chest-?")
                if(throw == "chest"):
                    print("Nope you suck he has armor your dead")
                elif(throw == "head"):
                    print("wow you won. my guards head is split open like a water melon. You deside to search him. You find a key and a map. You read the map and find your way to a door. But its looked. you use the key and the door opens. Congrats you have escaped. YOU WON")

