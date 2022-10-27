import os
import time 

score = 0

while True:
    answer = input("Wil je klikken?")
    if answer == "Ja" or "ja":
        score = score + 1
        print("je hebt nu", score, "punt")
        time.sleep(1)
        os.system("cls")
    elif answer == "Nee" or "nee":
        quit()
    else:
        print("Dat is geen optie!")
    
    answer = input("Wil je klikken?")
    if answer == "Ja" or "ja":
        score = score + 1
        print("je hebt nu", score, "punten")
        time.sleep(1)
        os.system("cls")
    elif answer == "Nee" or "nee":
        quit()
    
    answer = input("Wil je klikken?")
    if answer == "Ja" or "ja":
        score = score + 1
        print("je hebt nu", score, "punten")
        time.sleep(1)
        os.system("cls")
    elif answer == "Nee" or "nee":
        print("Game over")
        os.system("cls")
    answer = input("Wil je klikken?")
    if answer == "Ja" or "ja":
        score = score + 1
        print("je hebt nu", score, "punten")
        time.sleep(1)
        os.system("cls")
    elif answer == "Nee" or "nee":
        print("Game over")
        time.sleep(1)
        os.system("cls")
    answer = input("Wil je klikken?")
    if answer == "Ja" or "ja":
        print("je hebt nu", score, "punten")
        time.sleep(1)
        os.system("cls")
    elif answer == "Nee" or "nee":
        print("Game over")
        time.sleep(1)
        os.system("cls")
    answer = input("Wil je klikken?")
    if answer == "Ja" or "ja":
        score = score + 1
        print("je hebt nu", score, "punten")
        time.sleep(1)
        os.system("cls")
    elif answer == "Nee" or "nee":
        print("Game over")
        time.sleep(1)
        os.system("cls")
