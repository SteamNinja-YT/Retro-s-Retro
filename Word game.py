import random
import time
copCoins = 0
silCoins = 0
golCoins = 0
userHealth = 10
arrows = 0
healthPotion = 0
spellAttack = 0
rCheck = False
cCheck = False
startItems = 0
firstLookChoice = 0
locations = ["Leahcim", "Schnee", "Sistema", "Crossroads", "Yrneh", "Tniat"]
items = ["Sword", "Shield", "Bow", "Arrows", "Staff", "Spellbook", "Guitar", "Hooded Cloak"]
possClass = ["Fighter", "Ranger", "Wizard"]
possRace = list(("Human", "Elf", "Dwarf", "Goblin", "Orc"))
userLoca = locations[1]
print ("Welcome to the realm of Bosch!")
userName = str(input("What is your characters name?"))
while rCheck == False:
    userRace = str(input("What is your characters race? (Human, Elf, Dwarf, Goblin, Orc)"))
    if userRace in possRace:
        print("Well done!")
        rCheck = True
    else:
        print("Please put in one of the specified races!")
while cCheck == False:
    userClass = str(input("What is your characters Class? (Fighter, Ranger, Wizard)"))
    if userClass in possClass:
        print("Well done!")
        cCheck = True  
    else:
        print("Please put in one of the specified classes!")
if userClass == "Fighter":
    startItems1 = items[0]
    startItems2 = items[1]
elif userClass == "Ranger":
    arrows = 15
    startItems1 = items[2]
    startItems2 = arrows, items[3]
elif userClass == "Wizard":
    startItems1 = items[4]
    startItems2 = items[5]
else:
    startItems1 = items[6]
    startItems2 = items[7]
startItems = [startItems1, startItems2]
attSpellCount = startItems.count("Spell (Attack)")
print("Welcome to Schneed, the capital of Bosch,", userName, "the", userRace, userClass)
time.sleep(0)
print("You awaken in the dirty, dusty bed of the local tavern, bleary-eyed and half-asleep. As you look around the room you spot your customary", startItems1, "and", startItems2)
time.sleep(0)
print("You step out of bed, throw on your dirty clothes from yesterday and look around the room")
time.sleep(0)
def firstLook():
    print("You can either look out of the window (click A), check the cupboard (click D), or grab your items and leave (click W).")
firstLook()
firstLookChoice = str(input())
while firstLookChoice != "W":
    if firstLookChoice == "A":
        print("You look out of the window and see a crowded street below, then after seeing nothing of interest, you turn back around")
        firstLook()
        firstLookChoice = str(input())
    elif firstLookChoice == "D":
        if copCoins < 50:
            print("You open the cupboard and find 5 silver coins and 50 copper coins, then after seeing nothing else of interest you turn back around")
            copCoins = copCoins + 50
            silCoins = silCoins + 5
            print("You now have", copCoins, "copper coins")
            firstLook()
            firstLookChoice = str(input())
        else:
            print("You have already found the coins.")
            firstLook()
            firstLookChoice = str(input())
    else:
        print("Choose one of the available options")
        firstLook()
        firstLookChoice = str(input())
print("You grab your gear and leave the room, heading down a narrow corridor until you hear the jovial cheers of the taverns bar.")
firstQuestChoice = str(input("Look around tavern bar (recommended for beginners)(click W), or leave tavern (click A)"))
while firstQuestChoice != "A":
    if firstQuestChoice =="W":
        print("You take a quick glance around the crowd before spotting of the familiarly rowdy face of your old friend Makaykel Selyts. He quickly spots you and calls you over, once you sit down next to him he informs you of 2 rogue barbarians terrorising the townsfolk.")
        time.sleep(0)
        print("He thens convinves you to take care of the situation for the prize of 10 silver coins and 100 copper coins")
        time.sleep(0)
        print("He tells you to head to the stables and speak to Thonny the stableboy if you wish to pursue the quest")
        firstQuestChoice = str(input("Leave tavern (click A)"))
    else:
        print("Choose one of the available options")
        firstQuestChoice = str(input("Look around tavern bar (recommended for beginners)(click W), or leave tavern (click A)"))
firstMoveChoice = str(input("Click A to head to the shop, click D to head to the magic shop, and click W to head to the stables"))
while firstMoveChoice != "W":
    if firstMoveChoice == "A":
        firstMoneyChoice = str(input("You enter the shop, click A to buy a flute for 75 copper coins (can only be used by bard), click S to buy a dagger for 1 silver coin (can only be used by fighter), click D to buy 5 arrows for  25 copper coins(can only be used by ranger), or click W to exit the shop."))
        while firstMoneyChoice != "W":
            if firstMoneyChoice == "A":
                if copCoins > 74:
                    startItems.append("Flute")
                    copCoins = copCoins - 75
                    print("You have ", copCoins, "copper coins left")
                    firstMoneyChoice = str(input("You enter the shop, click A to buy a flute for 75 copper coins (can only be used by bard), click S to buy a dagger for 1 silver coin (can only be used by fighter), click D to buy 5 arrows for  25 copper coins (can only be used by ranger), or click W to exit the shop."))
                else:
                    print ("You cannot afford this item")
                    firstMoneyChoice = str(input("You enter the shop, click A to buy a flute for 75 copper coins (can only be used by bard), click S to buy a dagger for 1 silver coin (can only be used by fighter), click D to buy 5 arrows for  25 copper coins (can only be used by ranger), or click W to exit the shop."))
            elif firstMoneyChoice == "S":
                if silCoins > 0:
                    startItems.append("Dagger")
                    silCoins = silCoins - 1
                    print ("You have ", silCoins, "silver coins left")
                    firstMoneyChoice = str(input("You enter the shop, click A to buy a flute for 75 copper coins (can only be used by bard), click S to buy a dagger for 1 silver coin (can only be used by fighter), click D to buy 5 arrows for  25 copper coins (can only be used by ranger), or click W to exit the shop."))
                else:
                    print ("You cannot afford this item")
                    firstMoneyChoice = str(input("You enter the shop, click A to buy a flute for 75 copper coins (can only be used by bard), click S to buy a dagger for 1 silver coin (can only be used by fighter), click D to buy 5 arrows for  25 copper coins (can only be used by ranger), or click W to exit the shop."))
            elif firstMoneyChoice == "D":
                if copCoins > 24:
                    arrows = arrows + 5
                    copCoins = copCoins - 25
                    print ("You have ", copCoins, "copper coins left")
                    firstMoneyChoice = str(input("You enter the shop, click A to buy a flute for 75 copper coins (can only be used by bard), click S to buy a dagger for 1 silver coin (can only be used by fighter), click D to buy 5 arrows for  25 copper coins (can only be used by ranger), or click W to exit the shop."))
                else:
                    print("You cannot afford this item")
                    firstMoneyChoice = str(input("You enter the shop, click A to buy a flute for 75 copper coins (can only be used by bard), click S to buy a dagger for 1 silver coin (can only be used by fighter), click D to buy 5 arrows for  25 copper coins (can only be used by ranger), or click W to exit the shop."))
            else:
                print("Choose an available option")
                firstMoneyChoice = str(input("You enter the shop, click A to buy a flute for 75 copper coins (can only be used by bard), click S to buy a dagger for 1 silver coin (can only be used by fighter), click D to buy 5 arrows for  25 copper coins (can only be used by ranger), or click W to exit the shop."))
            print ("You have ", startItems)
            firstMoveChoice = str(input("Click A to head to the shop, click D to head to the magic shop, and click W to head to the stables"))
    elif firstMoveChoice == "D":
        secondMoneyChoice = str(input("You enter the magic shop, click A to buy a health potion for 50 copper coins, click D to buy a spell(attack) for 5 silver coins, or click W to leave the shop"))
        while secondMoneyChoice != "W":
            if secondMoneyChoice == "A":
                if copCoins > 49:
                    startItems.append("Health Potion")
                    healthPotion = healthPotion + 1
                    copCoins = copCoins - 50
                    print("You have ", copCoins, "copper coins left.")
                    secondMoneyChoice = str(input("You enter the magic shop, click A to buy a health potion for 50 copper coins, click D to buy a spell(attack) for 5 silver coins, or click W to leave the shop"))
                else:
                    print("You cannot afford this item")
                    secondMoneyChoice = str(input("You enter the magic shop, click A to buy a health potion for 50 copper coins, click D to buy a spell(attack) for 5 silver coins, or click W to leave the shop"))
            elif secondMoneyChoice == "D":
                if silCoins > 4:
                    startItems.append("Spell (Attack)")
                    spellAttack = spellAttack + 1
                    silCoins = silCoins - 5
                    print ("You have", silCoins, "silver coins left")
                    secondMoneyChoice = str(input("You enter the magic shop, click A to buy a health potion for 50 copper coins, click D to buy a spell(attack) for 5 silver coins, or click W to leave the shop"))
                else:
                    print("You cannot afford this item")
                    secondMoneyChoice = str(input("You enter the magic shop, click A to buy a health potion for 50 copper coins, click D to buy a spell(attack) for 5 silver coins, or click W to leave the shop"))
            else:
                print("Choose one of the available options.")
                secondMoneyChoice = str(input("You enter the magic shop, click A to buy a health potion for 50 copper coins, click D to buy a spell(attack) for 5 silver coins, or click W to leave the shop"))
        print ("You have ", startItems)
        print ("You have ", startItems)
        firstMoveChoice = str(input("Click A to head to the shop, click D to head to the magic shop, and click W to head to the stables"))
    else:
        print("Choose one of the available options.")
        firstMoveChoice = str(input("Click A to head to the shop, click D to head to the magic shop, and click W to head to the stables"))
secondQuestChoice = str(input("Click A to talk to Thonny or click W to get onto your horse and leave"))
while secondQuestChoice != "W":
    if secondQuestChoice == "A":
        print("You walk over to Thonny, upon spotting you he tells you of the barbarians in the woods who robbed him")
        print("He tells you they are in the forest between Schnee-where you are now- and Sistema(Follow this option if taking the quest from the tavern)")
        secondQuestChoice = str(input("Click W to get onto your horse and leave"))           
    else:
        print("Choose one of the available options")
        secondQuestChoice = str(input("Click A to talk to Thonny or click W to get onto your horse and leave"))
print("You get onto your horse and ride out of Schnee")
thirdQuestionChoice = str(input("Click A to go into the forest (Follow this option if taking the tavern quest), or click W to travel to Sistema"))
while thirdQuestionChoice != "W":
    if thirdQuestionChoice == "A":
        print("You ride into the forest, following a heavily trodden path until you spot light from a fire ahead. You have found the barbarian camp!")
        sneakChoice1 = str(input("If you want to sneak up on the 2 barbarians, click A (recommended for rangers and bards), if you want to attack one before the other one wakes up, click D (recommended for fighters and wizards)."))
#This is where you take out the sleeping barbarian first
        while sneakChoice1 != "A" and "D":
            print("Choose one of the available options")
            sneakChoice1 = str(input("If you want to sneak up on the 2 barbarians, click A (recommended for rangers and bards), if you want to attack one before the other one wakes up, click D (recommended for fighters and wizards)."))
        if sneakChoice1 == "A":
            print("You attempt to crouch around the edge of the camp to remain unspotted and take out the sleeping barbarian.")
            stealthRoll1 = random.randint(1,10)
            print("If this is random roll is higher than 3 then you succeed:", stealthRoll1)
            if stealthRoll1 > 3:
                if userClass == "Fighter":
                    print("You stab the sleeping barbarian with your sword.")
                elif userClass == "Ranger":
                    print("You stab the sleeping barbarian with an arrow")
                    arrows = arrows - 1
                elif userClass == "Wizard":
                    while True:
                        firstSpellCast = str(input("Click A to cast your basic spell to kill the sleeping barbarian, (You have unlimited basic spells and in this case it is just as effective as the attack spell), Click D to cast your attack spell to kill the sleeping barbarian, (You have limited attack spells)"))
                        if firstSpellCast == "A":
                            print("You eliminate the sleeping barbarian")
                            break
                        elif firstSpellCast == "D":
                            print("You vaporise the sleeping barbarian")
                            break
                        else:
                            print("Choose one of the available options")
                            firstSpellCast = str(input("Click A to cast your basic spell to kill the sleeping barbarian, (You have unlimited basic spells and in this case it is just as effective as the attack spell), Click D to cast your attack spell to kill the sleeping barbarian, (You have limited attack spells)"))
                else:
                    print("You put on your hooded cloak (gives you a stealth bonus) and eliminate the sleeping barbarian")
#This is where you attack the barbarian on guard after killing the sleeping barbarian
                print("The barbarian keeping watch spots you and rushes at you, forcing you to attack")
                if userClass == "Fighter":
                    userAtt1 = str(input("Click A to attack (you need higher than a 4 to succeed)"))
                    while userAtt1 != "A":
                        userAtt1 = str(input("Click A to attack (you need higher than a 4 to succeed)"))
                    userAttRoll1 = random.randint(1,10)
                    print(userAttRoll1)
                    while userAttRoll1 < 5:
                        print("You raise your shield to defend yourself after missing your attack")
                        userAtt1 = str(input("Click A to attack (you need higher than a 4 to succeed)"))
                        while userAtt1 != "A":
                            userAtt1 = str(input("Click A to attack (you need higher than a 4 to succeed)"))
                        userAttRoll1 = random.randint(1,10)
                        print(userAttRoll1)
                    print("You stab the barbarian with you sword.")
                elif userClass == "Ranger":
                    print("You try to shoot the barbarian (If you get more than 3 then you succeed).")
                    arrows = arrows - 1
                    userAttRoll1 = random.randint(1,10)
                    print(userAttRoll1)
                    if userAttRoll1 < 4:
                        print("You miss and the barbarian hits you with his club")
                        userHealth = userHealth - 2
                        print("Your health is now:", userHealth)
                        print("You stab the barbarian with an arrow killing him")
                        arrows = arrows - 1
                elif userClass == "Wizard":
                    attSpellCount = startItems.count("Spell (Attack)")
                    while True:
                        firstSpellCast = str(input("Click A to cast your basic spell to kill the barbarian, (You have unlimited basic spells and in this case it is just as effective as the attack spell), Click D to cast your attack spell to kill the barbarian, (You have limited attack spells)"))
                        if firstSpellCast == "A":
                            print("If you get higher than 3 you succeed")
                            firstSpellCastRoll = random.randint(1,10)
                            while firstSpellCastRoll < 4:
                                print("You fail and the barbarian hits you with his club")
                                userHealth = userHealth - 2
                                print("Your health is now:", userHealth)
                                firstSpellCast = str(input("Click A to cast your basic spell to kill the barbarian, (You have unlimited basic spells and in this case it is just as effective as the attack spell), Click D to cast your attack spell to kill the barbarian, (You have limited attack spells)"))
                            print("You eliminate the barbarian")
                            break
                        elif firstSpellCast == "D":
                            startItems.remove("Spell (Attack)")
                            print("You vaporise the barbarian")
                            attSpellCount = startItems.count("Spell (Attack)")
                            break
                        else:
                            print("Choose one of the available options")
                            firstSpellCast = str(input("Click A to cast your basic spell to kill the barbarian, (You have unlimited basic spells and in this case it is just as effective as the attack spell), Click D to cast your attack spell to kill the barbarian, (You have limited attack spells)"))
#This is where you fail the stealth roll and are forced to kill the barbarian on watch first
            else:
                if userClass == "Fighter":
                    userAtt1 = str(input("Click A to attack (you need higher than a 4 to succeed)"))
                    while userAtt1 != "A":
                        userAtt1 = str(input("Click A to attack (you need higher than a 4 to succeed)"))
                    userAttRoll1 = random.randint(1,10)
                    print(userAttRoll1)
                    while userAttRoll1 < 5:
                        print("You raise your shield to defend yourself after missing your attack")
                        userAtt1 = str(input("Click A to attack (you need higher than a 4 to succeed)"))
                        while userAtt1 != "A":
                            userAtt1 = str(input("Click A to attack (you need higher than a 4 to succeed)"))
                        userAttRoll1 = random.randint(1,10)
                        print(userAttRoll1)
                    print("You stab the barbarian with your sword then you walk over to the sleeping barbarian and slice off his head.")
                elif userClass == "Ranger":
                    print("You try to shoot the barbarian (If you get more than 3 then you succeed).")
                    arrows = arrows - 1
                    userAttRoll1 = random.randint(1,10)
                    print(userAttRoll1)
                    if userAttRoll1 < 4:
                        print("You miss and the barbarian hits you with his club")
                        userHealth = userHealth - 2
                        print("Your health is now:", userHealth)
                        print("You stab the barbarian with an arrow killing him, then you shoot the sleeping barbarian with an arrow through the heart, killing him too.")
                        arrows = arrows - 2
                    else:
                        print("You hit the barbarian through the heart then stab the sleeping barbarian with an arrow, killing them both.")
                        arrows = arrows - 1
                elif userClass == "Wizard":
                    attSpellCount = startItems.count("Spell (Attack)")
                    while True:
                        firstSpellCast = str(input("Click A to cast your basic spell to kill the barbarian, (You have unlimited basic spells and in this case it is just as effective as the attack spell), Click D to cast your attack spell to kill the barbarian, (You have limited attack spells)"))
                        if firstSpellCast == "A":
                            print("If you get higher than 3 you succeed")
                            firstSpellCastRoll = random.randint(1,10)
                            while firstSpellCastRoll < 4:
                                print("You fail and the barbarian hits you with his club")
                                userHealth = userHealth - 2
                                print("Your health is now:", userHealth)
                                firstSpellCast = str(input("Click A to cast your basic spell to kill the barbarian, (You have unlimited basic spells and in this case it is just as effective as the attack spell), Click D to cast your attack spell to kill the barbarian, (You have limited attack spells)"))
                            print("You eliminate the barbarian then you hit the sleeping barbarian with a basic spell, killing him.")
                            break
                        elif firstSpellCast == "D":
                            startItems.remove("Spell (Attack)")
                            print("You vaporise the barbarian then you hit the sleeping barbarian with a basic spell, killing him.")
                            attSpellCount = startItems.count("Spell (Attack)")
                            break
                        else:
                            print("Choose one of the available options")
                            firstSpellCast = str(input("Click A to cast your basic spell to kill the barbarian, (You have unlimited basic spells and in this case it is just as effective as the attack spell), Click D to cast your attack spell to kill the barbarian, (You have limited attack spells)"))
#This is where you choose to kill the barbarian on watch first                         
        elif sneakChoice1 == "D":
            if userClass == "Fighter":
                userAtt1 = str(input("Click A to attack (you need higher than a 4 to succeed)"))
                while userAtt1 != "A":
                    userAtt1 = str(input("Click A to attack (you need higher than a 4 to succeed)"))
                userAttRoll1 = random.randint(1,10)
                print(userAttRoll1)
                while userAttRoll1 < 5:
                    print("You raise your shield to defend yourself after missing your attack")
                    userAtt1 = str(input("Click A to attack (you need higher than a 4 to succeed)"))
                    while userAtt1 != "A":
                        userAtt1 = str(input("Click A to attack (you need higher than a 4 to succeed)"))
                    userAttRoll1 = random.randint(1,10)
                    print(userAttRoll1)
                print("You stab the barbarian with you sword then you walk to the sleeping barbarian and stab him.")
            elif userClass == "Ranger":
                print("You try to shoot the barbarian (If you get more than 3 then you succeed).")
                arrows = arrows - 1
                userAttRoll1 = random.randint(1,10)
                print(userAttRoll1)
                if userAttRoll1 < 4:
                    print("You miss and the barbarian hits you with his club")
                    userHealth = userHealth - 2
                    print("Your health is now:", userHealth)
                    print("You stab the barbarian with an arrow killing him, then you walk over to the sleeping barbarian and stab him with an arrow")
                    arrows = arrows - 2
                else:
                    print("You hit the barbarian, killing him, then you walk over to the sleeping barbarian and stab him with an arrow")
                    arrows = arrows - 1
            elif userClass == "Wizard":
                attSpellCount = startItems.count("Spell (Attack)")
                while True:
                    firstSpellCast = str(input("Click A to cast your basic spell to kill the barbarian, (You have unlimited basic spells and in this case it is just as effective as the attack spell), Click D to cast your attack spell to kill the barbarian, (You have limited attack spells)"))
                    if firstSpellCast == "A":
                        print("If you get higher than 3 you succeed")
                        firstSpellCastRoll = random.randint(1,10)
                        while firstSpellCastRoll < 4:
                            print("You fail and the barbarian hits you with his club")
                            userHealth = userHealth - 2
                            print("Your health is now:", userHealth)
                            firstSpellCast = str(input("Click A to cast your basic spell to kill the barbarian, (You have unlimited basic spells and in this case it is just as effective as the attack spell), Click D to cast your attack spell to kill the barbarian, (You have limited attack spells)"))
                        print("You eliminate the barbarian then you shoot the sleeping barbarian with a basic spell, killing him.")
                        break
                    elif firstSpellCast == "D":
                        startItems.remove("Spell (Attack)")
                        print("You vaporise the barbarian then you shoot the sleeping barbarian with a basic spell, killing him.")
                        break
                    else:
                        print("Choose one of the available options")
                        firstSpellCast = str(input("Click A to cast your basic spell to kill the sleeping barbarian, (You have unlimited basic spells and in this case it is just as effective as the attack spell), Click D to cast your attack spell to kill the sleeping barbarian, (You have limited attack spells)"))    
        time.sleep(5)
        print("After successfully eradicating the barbarians, you return to the tavern to collect your reward from Makaykel")
        copCoins = copCoins + 100
        silCoins = silCoins + 10
        time.sleep(2)
        print("You now have", copCoins, "copper coins and ", silCoins, "silver coins")
        time.sleep(1)
        print("You travel back out of Schneed")
        break
    thirdQuestionChoice = str(input("Click W to travel to Sistema"))
print("You arrive at Sistema")
secondMoveChoice = str(input("Ahead of you is a bank, click W to enter it"))
while secondMoveChoice != "W":
    print("Choose one of the available options")
    secondMoveChoice = str(input("Ahead of you is a bank, click W to enter it"))
moneyChangeChoice = str(input("You can turn 100 copper coins into 1 silver coins by clicking A"))
while moneyChangeChoice != "A":
    print("Choose one of the available options")
    moneyChangeChoice = str(input("You can turn 100 copper coins into 1 silver coins by clicking A"))
if copCoins > 99:
    copCoins = copCoins - 100
    silCoins = silCoins + 1
    print("You now have ", copCoins, "copper coins and ", silCoins, "silver coins")
else:
    print("You skipped the quest and so do not have enough money to use the bank(Which is really annoying because i had a whole massive banking system set up for later in the game and you just skipped its intro)")
thirdMoveChoice = str(input("Click W to go outside the bank"))
while thirdMoveChoice != "W":
    print("Choose one of the available options")
    thirdMoveChoice = str(input("Click W to go outside the bank"))
print("As you step outside you spot the mayor of Schnee waiting for you outside")
finalQuestChoice = str(input("Click A to talk to her"))
while finalQuestChoice != "A":
    print("Choose one of the available options")
    finalQuestChoice = str(input("Click A to talk to her"))
print("Mayor Schnorldle-'You have done well adventurer, you have been introduced to the basics of questing then shopping and even banking, and you have created a name for yourself through your powerful combat skills")
time.sleep(5)
print("You are truly worthy of the name", userName, "the Great'")
print("GAME OVER - credits to SteamNinja, Makichael and Al Dente - coding streams available on the YT Channel SteamNinja - Thanks For Playing!")
    