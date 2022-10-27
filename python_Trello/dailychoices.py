from operator import truediv
import time

choice = input()
print("Je gaat verschillende keuzes maken")
time.sleep(1)
choice = input("Je heb je verslapen, wat doe je?: \nA)Slaap B)Ontbijt C)Vertrek : ")
if choice == "A" or choice == "a":
    print("ZZzzzz")
elif choice == "B" or choice == "b":
    print("Eet smakelijk!")
elif choice == "C" or choice == "c":
    print("goede reis.")
choice == input("welk vervoer neem je?: \nA)de bus B)de trein C)de auto : ")
if choice == "A" or choice == "a":
    print("Je neemt de bus.")
elif choice == "B" or choice == "b":
    print("Je neemt de trein.")
elif choice == "C" or choice == "c":
    print("Je neemt de auto.")
choice == input("wat neem je mee?: \nA)tas B)laptop C)jas : ")
if choice == "A" or choice == "a":
    print("Je pakt je tas.")
elif choice == "B" or choice == "b":
    print("Je pakt je laptop.")
elif choice == "C" or choice == "c":
    print("Je trekt je jas aan.")
choice == input("ga je nog langs de winkel?: \nA)Nee B)Ja : ")
if choice == "A" or choice == "a":
    print("Je gaat niet de winkel in.")
elif choice == "B" or choice == "b":
    print("Je gaat nog even langs de winkel.")
choice == input("wat koop je bij de winkel?: \nA)een frikandelbroodje B)chips C)bier : ")
if choice == "A" or choice == "a":
    print("Je koopt een frikandelbroodje.")
elif choice == "B" or choice == "b":
    print("Je koopt chips.")
elif choice == "C" or choice == "c":
    print("Je koopt bier.")
choice == input("wil je dit programma stoppen? \n Y/N")
if choice == "Y" or choice == "y":
    print("afsluiten..")
elif choice == "N" or choice == "n":
    print("oke dan")

    