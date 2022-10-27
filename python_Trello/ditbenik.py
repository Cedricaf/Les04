from asyncore import loop
from operator import truediv
from re import A
from turtle import clear


while True:
    print("Hello You")
    answer = input("Wie ben jij?")
    print("Hello: " + answer)

    answer = input("Hoe oud ben ik: \n A) 18. B)16. C)17. ? :")
    if answer == "A":
        print("Ja dat klopt")
    elif answer == "B":
        print("Nee dat is fout ik ben 18 jaar")
    elif answer == "C":
        print("Nee dat is fout ik ben 18 jaar")
    else:
        print("Je kan alleen met A/B/C antwoorden!")
    answer = input("Waar woon ik: \n A) Haarlem. B) Amsterdam. C)IJmuiden ? : ")
    if answer == "A":
        print("Nee dat is fout ik woon in IJmuiden.")
    elif answer == "B":
        print("Nee dat is fout ik woon in IJmuiden.")
    elif answer == "C":
        print("Ja dat klopt.")
    else:
        print("Je kan alleen met A/B/C antwoorden!")
    answer = input("Wat is mijn favoriete kleur: \n A) Rood B) Blauw. C)Zwart ? : ")
    if answer == "A":
        print("Nee dat is fout mijn favoriete kleur is blauw.")
    elif answer == "B":
        print("Ja dat klopt.")
    elif answer == "C":
        print("Nee dat is fout mijn favoriete kleur is blauw")
    else:
        print("Je kan alleen met A/B/C antwoorden!")
    answer = input("In welk land woon ik: \n A) Nederland B) Amerika. C)Hongarije ? : ")
    if answer == "A":
        print("Ja dat klopt.")
    elif answer == "B":
        print("Nee dat is fout ik woon in Nederland.")
    elif answer == "C":
        print("Nee dat is fout ik woon in Nederland")
    else:
        print("Je kan alleen met A/B/C antwoorden!")