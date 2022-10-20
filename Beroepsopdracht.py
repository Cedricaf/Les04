import time


while True:
    print("Je gaat een keuzeverhaal spelen.\nIn het verhaal kan je keuzes maken die het einde beïnvloeden.")
    answer = input("Wil je beginnen? (Ja/Ja) ")
    if answer == "Ja" or "ja":
        time.sleep(1)
        answer = input("========================================================================\nJe bent bezig met het inpakken van je kleding in je hotelkamer.\nJe gaat op reis met het vliegtuig naar nederland waar er geen oorlog is.\nPlotseling hoor je voetstappen op de trap en besef je dat het de politie is die je zoekt.\nJe besluit om...\nA. Te verstoppen in de kast.\nB. Doorblijven gaan met inpakken.\nC. Jezelf te vermommen.")
        if answer == "A":
            time.sleep(1)
            print("========================================================================\nJe verstopt je in de kast en even later hoor je dat ze de deur inslaan.\nZe halen alles overhoop, maar de kast vergeten ze te controleren en even later hoor je ze weglopen.\nJe pakt zo snel mogelijk alles in.\nwat je nodig hebt en gaat naar het vliegveld.")
        elif answer == "B":
            time.sleep(1)
            print("========================================================================\nJe besluit om gewoon door te gaan met inpakken.\nEven later hoor je dat de deur kapot gaat.\nPolitie stormt naar binnen en je wordt geboeid en naar de gevangenis gebracht.\n[EINDE]")
            time.sleep(1)
            break
        elif answer == "C":
            time.sleep(1)
            answer = input("========================================================================\nJe vermomd je zo snel mogelijk en omdat jij een filmacteur was, werkt jouw vermomming zo goed dat de politie je niet herkend en weer vertrekt.\nJe pakt je spullen en gaat naar het vliegveld.\nDaar aangekomen zie je dat er politie staat bij de duane\nJe besluit om…\nA. Op de vermomming te rekenen. Dus niks en normaal gedragen.\nB. Proberen om te duane te ontwijken.")
            if answer == "A":
                time.sleep(1)
                answer = input("========================================================================\nJe denkt dat de vermomming goed werkt en je komt zonder problemen door de duane.\nNa 3uur wachten, vertrekt jouw vliegtuig naar Schiphol.\nAangekomen in schiphol kom je langs een café en je neemt…\nA.Niks.\nB. Koffie.\nThee.")
                if answer == "A":
                    time.sleep(1)
                    answer = input("========================================================================\n")
                elif answer == "B":
                    time.sleep(1)
                    answer == input("========================================================================\n")
                elif answer == "C":
                    time.sleep(1)
                    print("========================================================================\nJe neemt de thee, maar de thee blijkt vergiftigd te zijn.\nHelaas ben je niet in staat om verder te gaan en moet je naar het ziekenhuis.\n[EINDE]")
                    break
                else:
                    print("Dat is geen optie!")
                    break
            elif answer == "B":
                time.sleep(1)
                print("========================================================================\nJe probeert de duane te ontwijken, maar camera's zien dat je heel verdacht doet en de politie wordt ingelicht.\nJe wordt helaas opgepakt en naar de gevangenis gebracht.\n[Einde]")
                break
        else:
            print("Dat is geen optie!")
            break
    else:
        print("je moet het goede intypen!")
        break