# begonnen am: 14.4.2022
# von: Insane

import random

number1 = 1
number2 = 5

random_number = random.randint(number1, number2)

eingabe = input("Gebe eine Zahl zwischen 1 und 5 ein: ")


if(int(eingabe) == random_number):
    print("Richtig!")
elif(int(eingabe) > random_number):
    print("Zu hoch!")
elif(int(eingabe) < random_number):
    print("Zu niedrig!")

input("Guter Versuch! Drücke Enter um das Programm zu beenden.")