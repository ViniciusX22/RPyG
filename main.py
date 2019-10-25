from random import randint
from time import sleep
from classes import *

current_obj = None


def attack(obj):
    global current_obj
    if not current_obj:
        print("You need a character to attack. Create one using the 'create' command.")
    elif obj in GameObject.objects and obj != current_obj.name:
        foe = GameObject.objects[obj]
        print("You: " + current_obj.name + "\nFoe: " + foe.name + "\n")
        print(current_obj.attack(foe))
        if foe.health == 0:
            return
        if randint(1, 20) > 18:
            print('\n\t{} was faster and ran away from the battle!'.format(foe.name))
        else:
            print(
                "\n   You annoyed {} and now it's coming for an attack!\n\n".format(foe.name))
            descision = input(
                'Try to run away or stay and fight? Make your move!\n\n~> ')
            while descision.lower() not in ['fight', 'stay', 'run']:
                descision = input(
                    '\n\tSorry, but I didn\'t understand. \nTry to run away or stay and fight? Make your move!\n\n~> ')

            if descision.lower() == 'run':
                if randint(1, 20) > 15:
                    print(
                        "\n\tYou did it!\n\n {} was very angry, but you managed to make your way out. That was close!".format(foe.name))
                    return
                else:
                    print("\n\n\t{} is too fast! You can't leave now!".format(foe.name))
            else:
                print("\n\n\tAlright!")
            sleep(1)
            print("\n\n Wait!")
            sleep(.3)
            print(" Here comes the attack!")
            tries = 0
            while current_obj.health > 0 and foe.health > 0:
                tries += 1
                print('\n\n'+foe.attack(current_obj))
                if current_obj.health == 0:
                    print(
                        "\n\nOh no! It seems like you lost this battle... Now you have to try with another character.")
                    current_obj = None
                    break
                action = input(
                    '\n\nThat was hard! How about now: attack or run?\n\n~> ')
                while action.lower() not in ['attack', 'run']:
                    action = input(
                        '\nHmm... I think I didn\'t get it. How about now: attack or run?\n\n~> ')
                if action.lower() == 'attack':
                    print("\n  Let's go!")
                    print('\n\n'+current_obj.attack(foe))
                elif action.lower() == 'run':
                    if randint(1, 20) > 9 + tries:
                        print(
                            "\n\n\tYou did it!\n {} was very angry, but you managed to make your way out. That was close!".format(foe.name))
                        break
                    else:
                        print('\n\n\tThat didn\'t work...\n\n')
                if foe.health > 0:
                    sleep(2)
                    print("  Careful! Here it comes again!")
                    sleep(5)

    elif obj == current_obj.name:
        print("You can't attack yourself!")
    elif obj == "nothing":
        print("Sorry, who do you wanna attack?")
    else:
        print("\nDid you mean someone else? There isn't anybody called " + obj + " here :/")


def desc(obj):
    if obj == "nothing":
        if current_obj != None:
            print("You:\t\t{0}\n\n\tClass: {1}\n\tDescription: {2}\n\tStatus: {3}".format(
                current_obj.name, current_obj.class_name, current_obj.desc, str(current_obj.status)))
        else:
            print("Create or select a character first!")
    elif current_obj != None and current_obj.name == obj:
        print("You:\t\t{0}\n\n\tClass: {1}\n\tDescription: {2}\n\tStatus: {3}".format(
            current_obj.name, current_obj.class_name, current_obj.desc, str(current_obj.status)))
    else:
        if obj in GameObject.objects:
            obj = GameObject.objects[obj]
            print("\t\t{0}\n\n\tClass: {1}\n\tDescription: {2}\n\tStatus: {3}\n".format(
                obj.name, obj.class_name, obj.desc, obj.status))
        else:
            print(
                "\nDid you mean someone else? There isn't anybody called " + obj + " here :/")


def create_creature(type):
    global current_obj
    if type.lower() == "goblin":
        name = input("Name: ")
        if current_obj is None:
            current_obj = Goblin(name)
            print("\n\t" + name + " was created! That's your current character.")
        else:
            tmp = Goblin(name)
            print("\n\t" + name + " was created!")
    elif type.lower() == "wizard":
        name = input("Name: ")
        if current_obj is None:
            current_obj = Wizard(name)
            print("\n\t" + name + " was created! That's your current character.")
        else:
            tmp = Wizard(name)
            print("\n\t" + name + " was created!")
    elif type == "nothing":
        print("A class is needed!")
    else:
        print("Unknown class")


def help(cmd):
    if cmd == "nothing":
        print("Allowed commands:\n")
        for cmd in keywords:
            print("\t"+cmd)
        print("\nType 'help <command>' to more details")
    else:
        print("\n{}".format(desc_command[cmd]))


def select(obj):
    if obj == "nothing":
        print("Let me know who do you want!")
    else:
        global current_obj
        if obj == current_obj.name:
            print("Ops! It seems you already are {}!".format(obj))
        elif obj in GameObject.objects:
            current_obj = GameObject.objects[obj]
            print("Now you are {}!".format(obj))
        else:
            print(
                "Did you mean someone else? There isn't anybody called " + obj + " here :/")


def get_input():
    command = input("\n~> ").split(" ")
    verb_word = command[0].lower()
    if verb_word in keywords:
        verb = keywords[verb_word]
    else:
        print("Unknown command {}". format(verb_word))
        print("Type 'help' for more information")
        return

    if len(command) >= 2:
        noun_word = command[1]
        verb(noun_word)
    else:
        verb("nothing")


keywords = {
    "create": create_creature,
    "attack": attack,
    "select": select,
    "desc": desc,
    "help": help
}

desc_command = {
    "create": "Syntax: create <class_name>\n\nCreates a new character with the specified class." +
    "\n\n\tAvailable Classes\n" +
    "\nGoblin - a foul creature" +
    "\nWizard - the master of magic",
    "attack": "Syntax: attacks <name>\n\nAttacks a living character identified by its name.",
    "desc": "Syntax: desc <name>\n\nShows a description and the status of a specified character.\n\nObs: Let the field 'name' empty to describe the current character.",
    "select": "Syntax: select <character_name>\n\nSelects a character to control",
    "help": "Show a command description like this one :)"
}


while True:
    get_input()
