
import time

def won():
    print("GEFELICITEERD")

def gameover():
    time.sleep(1)
    answer = input("Je wordt wakker middernacht. \nJe hoort een hard getik in huis.\nvoor je ligt een pistol en een handgranaat\nkies een van de twee om verder te gaanJa\n(pistol/handgranaat) ")
    if answer == "pistol" or answer == "Pistol":
        answer = input("Je pakt het Pistol en doet de kamerdeur open... maar een beer komt op je af.\nwat doe je?\n(Schieten/Rennen) ")
        if answer.lower() == "schieten":
            print("Je schiet je pistol, maar er blijkt maar 1 kogel in te zitten.\nde beer valt je aan.\nJe hebt verloren.")
            gameover()
        elif answer.lower() == "rennen":
            answer = input("Je rent en de beer gaat niet achter je aan.\nJe komt nu op de gang, neem je de trap of ga je linksaf?\n(trap/links)")

            if answer == "trap" or answer == "Trap":
                answer = input("Je gaat de trap af, maar ziet dat een inbreker je beneden op staat te wachten.\nwat pak je van de grond?\n(steen/woordenboek/veer) ")
                if answer == "steen" or answer == "Steen":
                    print("Je pakt te steen en gooit het naar de inbreker.\nhij valt bewusteloos neer.\nJE HEBT GEWONNEN!")
                    time.sleep(1)
                    won()
                elif answer == "woordenboek" or answer == "Woordenboek":
                    print("Je probeert het woordenboek op te pakken, maar het is te zwaar om te gooien en de inbreker hoort je.\nHij komt naar boven en mept je knockout.\nJe hebt verloren.")
                    gameover()
                elif answer == "veer" or answer == "veer":
                    print("Je pakt de veer, maar hoezo heb je deze keuze gemaakt?\ndoor de tijd die je verspilt hebt ben je al knockout geklapt door de inbreker.\nJe hebt verloren.")
                    gameover()
                else:
                    print("Dat is geen optie!")
            elif answer == "links" or answer == "Links":
                answer = input("Je besluit om links te gaan en je komt een staal harnas, leren jas en mobiele telefoon tegen.\nwat kies je?\n(tijdbom/Vaas/Telefoon) ")
                if answer == "Bom" or answer == "bom":
                    print("Je pakt de bom, maar hij ontploft.\nJe hebt verloren.")
                    gameover()
                elif answer == "Telefoon" or answer == "telefoon":
                    print("Je pakt de telefoon en belt 112.\nde politie stormt binnen en neemt de inbreker gevangen.\nJE HEBT GEWONNEN!")
                    time.sleep(1)
                    won()
                elif answer == "vaas" or answer == "Vaas":
                    print("Je pakt de vaas maar je laat de vaas op de grond vallen en de beer vermoord je.\nJe hebt verloren.")
                    gameover()
                else:
                    ("Dat is geen optie!")
            else:
                print("Dat is geen optie!")
        else:
            print("Thats not an option!")
             
    elif answer == "handgranaat":
        print("Je pakt de granaat, maar opeens gaat hij af.\nje hebt verloren.")
        gameover()
    else:
        print("Dat is geen optie!")



answer = input("Wil je de game starten? (Ja/Nee) ")

if answer == "Ja" or answer == "ja":

    answer = input("Je wordt wakker middernacht. \nJe hoort een hard getik in huis.\nvoor je ligt een pistol en een handgranaat\nkies een van de twee om verder te gaanJa\n(pistol/handgranaat) ")
    if answer == "pistol" or answer == "Pistol":
        answer = input("Je pakt het Pistol en doet de kamerdeur open... maar een beer komt op je af.\nwat doe je?\n(Schieten/Rennen) ")
        if answer.lower() == "schieten" or answer == "Schieten":
            print("Je schiet je pistol, maar er blijkt maar 1 kogel in te zitten.\nde beer valt je aan.\nJe hebt verloren.")
            gameover()
        elif answer.lower() == "rennen" or answer == "Rennen":
            answer = input("Je rent en de beer gaat niet achter je aan.\nJe komt nu op de gang, neem je de trap of ga je linksaf?\n(trap/links)")

            if answer == "trap" or answer == "Trap":
                answer = input("Je gaat de trap af, maar ziet dat een inbreker je beneden op staat te wachten.\nwat pak je van de grond?\n(steen/woordenboek/veer) ")
                if answer == "steen" or answer == "Steen":
                    print("Je pakt te steen en gooit het naar de inbreker.\nhij valt bewusteloos neer.\nJE HEBT GEWONNEN!")
                    time.sleep(1)
                    won()
                elif answer == "woordenboek" or answer == "Woordenboek":
                    print("Je probeert het woordenboek op te pakken, maar het is te zwaar om te gooien en de inbreker hoort je.\nHij komt naar boven en mept je knockout.\nJe hebt verloren.")
                    gameover()
                elif answer == "veer" or answer == "veer":
                    print("Je pakt de veer, maar hoezo heb je deze keuze gemaakt?\ndoor de tijd die je verspilt hebt ben je al knockout geklapt door de inbreker.\nJe hebt verloren.")
                    gameover()
                else:
                    print("Dat is geen optie!")
            elif answer == "links" or answer == "Links":
                answer = input("Je besluit om links te gaan en je komt een staal harnas, leren jas en mobiele telefoon tegen.\nwat kies je?\n(tijdbom/Jas/Telefoon) ")
                if answer == "Bom" or answer == "bom":
                    print("Je pakt de bom, maar hij ontploft.\nJe hebt verloren.")
                    gameover()
                elif answer == "Telefoon" or answer == "telefoon":
                    print("Je pakt de telefoon en belt 112.\nde politie stormt binnen en neemt de inbreker gevangen.\nJE HEBT GEWONNEN!")
                    time.sleep(1)
                    won()
                elif answer == "vaas" or answer == "Vaas":
                    print("Je pakt de vaas maar je laat de vaas op de grond vallen en de beer vermoord je.\nJe hebt verloren.")
                    gameover()
                else:
                    ("Dat is geen optie!")
            else:
                print("Dat is geen optie!")
        else:
            print("Dat is geen optie!")
                


    
    elif answer == "handgranaat":
        print("Je pakt de granaat, maar opeens gaat hij af.\nje hebt verloren.")
        gameover()
    else:
        print("Dat is geen optie!")

else:
    print("Dat is geen optie!")

    