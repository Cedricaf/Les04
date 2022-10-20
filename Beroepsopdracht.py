from multiprocessing.connection import answer_challenge
import time

while True:
    print("Je gaat een keuzeverhaal spelen.\nIn het verhaal kan je keuzes maken die het einde beïnvloeden.")
    answer = input("Wil je beginnen? (Ja/Ja) ")
    if answer == "Ja" or "ja":
        answer = input("Je bent bezig met het inpakken van je kleding in je hotelkamer.\nJe gaat op reis met het vliegtuig naar nederland waar er geen oorlog is.\nPlotseling hoor je voetstappen op de trap en besef je dat het de politie is die je zoekt.\nJe besluit om…\nA. Te verstoppen in de kast.\nB. Doorblijven gaan met inpakken.\nC. Jezelf te vermommen.")
    else:
        print("je moet het goede intypen!")
        break