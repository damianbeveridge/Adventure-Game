import time
import random
weapons = []
troll_choice = [1, 2]
s = 'sword and shield'
b = 'bow and arrow'
m = 'two handed mace'


def print_pause(message, seconds):
    print(message)
    time.sleep(seconds)


def intro():
    print_pause("You awake to the sounds of bells ringing loudly.", 2.5)
    print_pause("Down the stairs you run from your room in the tower.", 2.5)
    print_pause("You burst though the two large doors leading to \
the Kings hall.", 2.5)
    print_pause("Inside the people are crying and acting hysterically.", 2.5)
    print_pause("You race up to the King where he tells you the Queen \
has been murdered!", 2.5)
    print_pause("He asks you to pursure her killer as all his other \
guards have to stay and protect him.", 2.5)
    print_pause("Will you accept this task?", 2)


def armory_intro():
    print_pause("Inside the armory most of the weapons have already been \
taken.", 2)
    print_pause("There are only three options left..", 2)
    print_pause("1. Sword and Shield", 1)
    print_pause("2. Bow and Arrows", 1)
    print_pause("3. Two handed Mace", 1)
    print_pause("Which will you choose?", 1)


def part2_intro():
    print_pause("Now that you have your weapon it's time to catch this \
assassin!", 2.5)
    print_pause("You sprint out of the castle dodging people as you \
go.", 2.5)
    print_pause("You rush into the stables where your trusted steed is \
waiting.", 2.5)
    print_pause("Galloping out of the castle the comotion behind you \
begins to fade.", 2.5)
    print_pause("In front of you only the dark forest awaits...", 2.5)
    print_pause("The forest trail begins to narrow quickly and you \
eventually come to a fork in the path.", 2.5)
    print_pause("At the fork you dismount your horse and begin to \
look for any trace of the assassin.", 2.5)
    print_pause("You discover hoof prints leading down the left \
path.", 2.5)
    print_pause("But there is also, boot tracks heading down the \
right path..", 2.5)
    print_pause("Which way would you like to go?", 2.5)


def right_path_intro():
    print_pause("You've decided to head to the right and follow \
the footprints.", 2.5)
    print_pause("After riding down the path for a while you start \
to see something in the distance.", 2)
    print_pause("A large shape begins to appear, It's a cabin!", 2)
    print_pause("The original path goes around the cabin and back \
into the forest.", 2)


def cabin(weapons):
    print_pause("You cautiously walk up to the cabin and slowly open \
the door.", 2)
    print_pause("The cabin is completely black. The moss covered \
windows don't let any light in.", 2.5)
    print_pause("As you move futher into the cabin, the door slams \
shut!", 2.5)
    print_pause("You spin around in time only to see a glimpse of a \
large figure coming towards you.", 2.5)
    print_pause("WHAM!", 2)
    print_pause("You wake up on the floor of the cabin, dazed and \
confused.", 2.5)
    print_pause("Your head is throbbing and beginning to swell from \
the hit you took.", 2.5)
    print_pause("Looking around, you discover your weapon is missing \
as well.", 2.5)
    weapons.clear()
    print_pause("Getting up and dusting yourself off, you head out of \
the cabin.", 2.5)
    print_pause("Deciding you cannot give up yet, you turn and follow \
the path around the cabin.", 2.5)


def cabin_path(weapons):
    print_pause("The path leads you back into the forest but it seems \
to be turning as you move along it.", 2.5)
    print_pause("The sound of rushing water is faint in the \
distance.", 2.5)
    print_pause("Soon a shallow river comes into view and with no \
where else to go, you decide to cross it.", 2.5)
    print_pause("On the other side you find a cave and you can see \
hoof prints all around it.", 2.5)


def left_path_intro(weapons):
    print_pause("To the left you go.", 2.5)
    print_pause("You follow the path going further and \
further into the dark forest.", 2.5)
    print_pause("The path ends suddenly and you find yourself on \
the bank of a river.", 2.5)
    print_pause("On your left is a small cave with hoof prints \
scattered all around.", 2.5)
    print_pause("After taking a moment to figure out what to \
do.", 2.5)
    print_pause("You realize there are only two options..", 2.5)
    print_pause("Go into the creepy cave or cross the shallow \
river and continue on.", 2.5)


def cave_intro():
    print_pause("You enter the cave, keeping your eyes peeled \
for any sign of danger.", 2.5)
    print_pause("You can hear a low repitious sound, almost like \
heavy breathing.", 2.5)
    print_pause("The sound gets louder as you walk deeper into the \
cave.", 2.5)
    print_pause("Your eyes have adjusted to the darkness and you \
can see where the noise was coming from.", 2.5)
    print_pause("It's a Cave Troll!", 2.5)
    print_pause("The troll sees you and begins to rush towards \
you.", 2.5)


def river_crossing(weapons):
    print_pause("You've crossed the river and found a path on \
the other side.", 2.5)
    print_pause("The path is a long curved one that leads you \
deep into the forest.", 2.5)
    print_pause("You emerge from the path.", 2.5)
    print_pause("Ahead it looks to you like the backside of an \
abandoned cabin.", 2.5)
    while True:
        choice4 = valid_input2("Do you enter the cabin?\n"
                               "y/n\n", 'y', 'n')
        if choice4 == 'y':
            cabin(weapons)
            cabin_path(weapons)
            cave(weapons)
            break
        if choice4 == 'n':
            print_pause(
                "You skip the cabin and keep following the path.", 2.5)
            print_pause(
                "The path leads you back to the original \
fork in the road.", 2.5)
            print_pause(
                "Which way would you like to go, right \
towards the cabin, or left towards the cave.", 2.5)
            choice2 = valid_input2("Left or Right\n", 'left', 'right')
            if choice2 == 'right':
                right_path(weapons)
                break
            elif choice2 == 'left':
                left_path(weapons)
                break


def cave2_intro():
    print_pause("Once passed the Troll you discover a chest.", 2.5)
    print_pause("You decide to open the chest and look inside.", 2.5)
    print_pause("Inside you find a sword and shield.", 2.5)


def end_game_intro():
    print_pause("The sun is blinding you when you get outside \
the cave.", 2.5)
    print_pause("It takes a moment till you can see again.", 2.5)
    print_pause("In the distance you can see a man running \
through the trees.", 2.5)
    print_pause("You give chase and are steady gaining on him.", 2.5)
    print_pause("Suddenly he stops and you realize why.", 2.5)
    print_pause(
        "He has come to the edge of a cliff and turns to face you.", 2.5)
    print_pause(
        "There is cloth over his face, you can't make out who he is", 2.5)
    print_pause(
        "'WHY!!' you yell at him, 'Why would you do such a thing!'", 2.5)
    print_pause("From behind the cloth a raspy voice calmly emerges.", 2.5)
    print_pause("'She wasn't who you think she was.'", 2.5)
    print_pause("'What do you mean?' you ask. 'You wouldn't \
understand..', he says.", 2.5)
    print_pause("The assassin takes one final look at you and \
steps back off the cliff.", 2.5)
    print_pause("You run to the edge and look over but all you can see \
is the raging river below.\n", 2.5)
    print_pause("To be continued...\n", 3)
    print_pause("Congrats you've made it to the end of the game!", 2.5)


def play_again():
    while True:
        print("Would you like to play again?")
        again = input("Y/N?\n").lower()
        if again == 'y':
            game()
        elif again == 'n':
            print("Thank you for playing.")
            exit()
        else:
            print_pause("Please enter Y for yes and N for no", 1)


def valid_input3(prompt, option1, option2, option3):
    while True:
        response = input(prompt).lower()
        if response == option1:
            break
        elif response == option2:
            break
        elif response == option3:
            break
        else:
            print_pause("Please stop wasting time! Choose from \
the options available.", 1)
    return response


def valid_input2(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if response == option1:
            break
        elif response == option2:
            break
        else:
            print_pause("Please stop wasting time! Choose from \
the options available.", 1)
    return response


def start_game():
    while True:
        begin_game = input('Yes or No\n').lower()
        if begin_game == 'yes':
            print_pause("You tell the King your answer but you will \
need a weapon first...", 2)
            print_pause("Off to the armory you go!", 2)
            break
        elif begin_game == 'no':
            print_pause("The King is furious with you for not doing \
what he asks and sentences you to the dungeon", 2)
            print_pause("Game Over", 2)
            play_again()
            break
        else:
            print_pause("Please enter yes or no there is no time to waste!", 2)


def armory(weapons):
    armory_intro()
    response = valid_input3("Please select a number:\n", "1", "2", "3")
    if response == '1':
        weapons.append(s)
        print_pause("You have chosen the Sword and Shield.", 2)
    elif response == '2':
        weapons.append(b)
        print_pause("You have chosen the Bow and Arrows.", 2)
    elif response == '3':
        weapons.append(m)
        print_pause("You have chosen the large Two Handed Mace.", 2)


def right_path(weapons):
    right_path_intro()
    right_choice = valid_input2("Do you get off the path and \
investigate the cabin? y/n\n", 'y', 'n')
    if right_choice == 'y':
        cabin(weapons)
        cabin_path(weapons)
        cave(weapons)
    elif right_choice == 'n':
        cabin_path(weapons)
        cave(weapons)


def left_path(weapons):
    left_path_intro(weapons)
    choice3 = valid_input2("Do you A) cross the river or B) head \
into the cave\n", 'a', 'b')
    if choice3 == 'b':
        cave(weapons)
    elif choice3 == 'a':
        river_crossing(weapons)


def part2(weapons):
    part2_intro()
    choice2 = valid_input2("Left or Right\n", 'left', 'right')
    if choice2 == 'right':
        right_path(weapons)
    elif choice2 == 'left':
        left_path(weapons)


def cave(weapons):
    cave_intro()
    if weapons != []:
        print_pause("You dispatch the troll with ease and continue \
through the cave.", 2.5)
    else:
        troll_attack = random.choice(troll_choice)
        if troll_attack == 1:
            print_pause("The troll attacks but with no weapon you \
are easily defeated.", 2.5)
            print_pause("Game Over", 2.5)
            play_again()
        elif troll_attack == 2:
            print_pause(
                "The troll attacks but slips on the wet cave floor.", 2.5)
            print_pause(
                "He falls back and knocks himself out on a rock.", 2.5)
            print_pause(
                "You sneak past him and continue on down the cave.", 2.5)
        return


def cave_chest(weapons):
    if weapons[:] == []:
        weapons.append(s)
        print_pause("You pick up the sword and shield and continue \
on through the cave.", 2.5)
    elif weapons[0] == s:
        print_pause(
            "You already have a sword and shield so you leave the \
chest alone.", 2.5)
    else:
        if weapons[0] == b:
            print_pause("Would you like to exchange your bow and arrows \
for the sword and shield?", 2.5)
            weapon_change = valid_input2("Yes or No\n", 'yes', 'no')
            if weapon_change == 'yes':
                weapons.clear()
                weapons.append(s)
                print_pause("You have discarded your current weapon and \
picked up the Sword and Shield.", 2.5)
                return
            elif weapon_change == 'no':
                print_pause(
                    "You close the chest and keep your current weapon.", 2.5)
                return
        elif weapons[0] == m:
            print_pause("Would you like to exchange your mace for the \
sword and shield?", 2.5)
            weapon_change = valid_input2("Yes or No\n", 'yes', 'no')
            if weapon_change == 'yes':
                weapons.clear()
                weapons.append(s)
                print_pause("You have discarded your current weapon and \
picked up the Sword and Shield.", 2.5)
                return
            elif weapon_change == 'no':
                print_pause(
                    "You close the chest and keep your current weapon.", 2.5)
                return


def cave2(weapons):
    cave2_intro()
    cave_chest(weapons)


def end_cave(weapons):
    print_pause("You can see a faint glow in the distance.", 2.5)
    print_pause("The end of the cave is in sight!", 2.5)
    print_pause("You are about ten feet from the exit when \
you hear a loud 'click'.", 2.5)
    print_pause("The assassin set one final trap for you!", 2.5)
    print_pause("Rocks begin to fall from the ceiling.", 2.5)
    while True:
        if weapons[0] == s:
            print_pause("But your quick with your shield and lift \
it over your head as you run out of the cave.", 2.5)
            break
        elif weapons[0] != s:
            rock_fall = random.choice(troll_choice)
            if rock_fall == 1:
                print_pause("You dive forward and while only getting \
hit a few times you make it out of the cave safely.", 2.5)
                break
            elif rock_fall == 2:
                print_pause("The rocks are falling all around you.", 2.5)
                print_pause("With no shield to protect your head, you become \
trapped in the cave.", 2.5)
                print_pause("Game Over", 2.5)
                play_again()


def end_game(weapons):
    end_game_intro()
    play_again()


def game():
    intro()
    start_game()
    armory(weapons)
    part2(weapons)
    cave2(weapons)
    end_cave(weapons)
    end_game(weapons)


game()
