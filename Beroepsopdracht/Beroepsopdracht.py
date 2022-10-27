import time


def Start():
    print("Je gaat een keuzeverhaal spelen.\nIn het verhaal kan je keuzes maken die het einde beïnvloeden.")
    return

def error():
    print("Dat is geen optie!")
    return

def lines():
    print("========================================================================")

while True:
    Start()
    answer = input("Wil je beginnen? (Y/y) ")
    if answer == "Y" or "y":
        time.sleep(1)
        lines()
        answer = input("Je bent bezig met het inpakken van je kleding in je hotelkamer.\nJe gaat op reis met het vliegtuig naar nederland waar er geen oorlog is.\nPlotseling hoor je voetstappen op de trap en besef je dat het de politie is die je zoekt.\nJe besluit om...\n\nA. Doorblijven gaan met inpakken.\nB. Jezelf te vermommen.\n>>>")
        if answer == "A":
            time.sleep(1)
            lines()
            print("Je besluit om gewoon door te gaan met inpakken.\nEven later hoor je dat de deur kapot gaat.\nPolitie stormt naar binnen en je wordt geboeid en naar de gevangenis gebracht.\n[EINDE]")
            time.sleep(1)
            break
        elif answer == "B":
            time.sleep(1)
            lines()
            answer = input("Je vermomd je zo snel mogelijk en omdat jij een filmacteur was, werkt jouw vermomming zo goed dat de politie je niet herkend en weer vertrekt.\nJe pakt je spullen en gaat naar het vliegveld.\nDaar aangekomen zie je dat er politie staat bij de duane.\nJe besluit om…\nA. Op de vermomming te rekenen. Dus niks en normaal gedragen.\nB. Proberen om te duane te ontwijken.\n>>>")
            if answer == "A":
                time.sleep(1)
                lines()
                answer = input("Je denkt dat de vermomming goed werkt en je komt zonder problemen door de duane.\nNa 3uur wachten, vertrekt jouw vliegtuig naar Schiphol.\nAangekomen in schiphol kom je langs een café en je neemt…\nA. Niks.\nB. Koffie.\nC. Thee.\n>>>")
                if answer == "A":
                    time.sleep(1)
                    lines()
                    answer = input("Je neemt niks en je loopt verder.\nBij de uitgang wordt je verwelkomt door een vriend die in nederland woont en hij verteld dat je tijdelijk bij hem mag komen wonen.\nJullie besluiten om naar de nieuwe star wars film te gaan\nJe neemt…\nA. de bus.\nB. een Taxi.\n>>>")
                    if answer == "A":
                        time.sleep(1)
                        lines()
                        answer = input("Je neemt de bus en jullie worden afgezet dichtbij de bios.\nJullie kopen kaartjes en lopen naar binnen.\nAls snack kies je…\nA. Popcorn.\nB. Tortilla chips.\n>>>")
                        if answer == "A":
                            time.sleep(1)
                            lines()
                            answer = input("Je neemt de popcorn en je deelt wat met je vriend.\nNa de film besluit je om…\nA. naar de dam te gaan.\nB. nog even boodschappen te doen.\n>>>")
                            if answer == "A":
                                time.sleep(1)
                                lines()
                                answer = input("Je besluit om nog rond te gaan hangen op de dam waar straatartisten optreden.\nJe geeft de straatartiest…\nA. 10 euro.\nB. niks.\n>>>")
                                if answer == "A":
                                    time.sleep(1)
                                    lines()
                                    answer = input("De straatartiest zegt: “Thank you” en jij besluit om na het optreden…\nA. naar huis te gaan.\nB. naar de mcdonalds te gaan.")
                                    if answer == "A":
                                        time.sleep(1)
                                        lines()
                                        print("Eindelijk kom je thuis en je vindt het tijd om te gaan slapen.\nJe hebt de reis overleefd!\nGoed gedaan!\[EINDE]")
                                        break
                                    elif answer == "B":
                                        time.sleep(1)
                                        lines()
                                        answer = input("Bij de mcdonalds kies je een grote portie.\nNadat je het op hebt gegeten besluit je om…\nA. naar huis te gaan.\nB. naar huis te gaan.")
                                        if answer == "A":
                                            time.sleep(1)
                                            lines()
                                            print("Eindelijk kom je thuis en je vindt het tijd om te gaan slapen.\nJe hebt de reis overleefd!\nGoed gedaan![EINDE]")
                                            break
                                        elif answer == "B":
                                            time.sleep(1)
                                            lines()
                                            print("Eindelijk kom je thuis en je vindt het tijd om te gaan slapen.\nJe hebt de reis overleefd!\nGoed gedaan![EINDE]")
                                            break
                                        else:
                                            error()
                                            break
                                elif answer == "B":
                                    time.sleep(1)
                                else:
                                    error()
                                    break                                
                            elif answer == "B":
                                time.sleep(1)
                                lines()
                                answer = input("Je besluit om boodschappen te doen en je komt bij de diepvries afdeling.\nJe neemt…\nA. Lasagna.\nB. Vis.\n>>>")
                                if answer == "A":
                                    time.sleep(1)
                                    lines()
                                    print("Je neemt de lasanga en warmt deze thuis op.\nUiteindelijk val je in slaap op de bank.\nJe hebt de reis overleeft!\nGoed gedaan![EINDE]")
                                    break
                                elif answer == "B":
                                    time.sleep(1)
                                    lines()
                                    print("Je neemt de vis en warmt deze thuis op.\nUiteindelijk val je in slaap op de bank.\nJe hebt de reis overleeft!\nGoed gedaan![EINDE]")
                                    break
                                else:
                                    error()
                                    break
                            else:
                                error()
                                break
                        elif answer == "B":
                            time.sleep(1)
                            lines()
                            answer = input("Je neemt de tortilla chips en na de film besluit je om…\nA. naar de dam te gaan.\nB. nog even boodschappen te doen.\n>>>")
                            if answer == "A":
                                time.sleep(1)
                                lines()
                                answer = input("Je besluit om nog rond te gaan hangen op de dam waar straatartisten optreden.\nJe geeft de straatartiest…\nA. 10 euro.\nB. niks.\n>>>")
                            elif answer == "B":
                                time.sleep(1)
                                lines()
                                answer = input("Je wordt raar aangekeken en je besluit om…\nA. 10 euro te geven.\nB. naar huis te gaan.\n>>>")
                            if answer == "A":
                                time.sleep(1)
                                lines()
                                answer = input("De straatartiest zegt: “Thank you” en jij besluit om na het optreden…\nA. naar huis te gaan.\nB. naar de mcdonalds te gaan.\n>>>")
                                if answer == "A":
                                    time.sleep(1)
                                    lines()
                                    print("Eindelijk kom je thuis en je vindt het tijd om te gaan slapen.\nJe hebt de reis overleefd!\nGoed gedaan![EINDE]")
                                    break
                                elif answer == "B":
                                    time.sleep(1)
                                    lines()
                                    answer = input("Bij de mcdonalds kies je een grote portie.\nNadat je het op hebt gegeten besluit je om…\nA. naar huis te gaan.\nB. naar huis te gaan.\n>>>")
                                    if answer == "A":
                                        time.sleep(1)
                                        lines()
                                        print("Eindelijk kom je thuis en je vindt het tijd om te gaan slapen.\je hebt de reis overleefd\nGoed gedaan![EINDE]")
                                        break
                                    elif answer == "A":
                                        time.sleep(1)
                                        lines()
                                        print("Eindelijk kom je thuis en je vindt het tijd om te gaan slapen.\je hebt de reis overleefd\nGoed gedaan!")
                                        break
                                else:
                                    error()
                                    break
                            elif answer == "B":
                                time.sleep(1)
                                lines()
                                print("Eindelijk kom je thuis en je vindt het tijd om te gaan slapen.\nJe hebt de reis overleefd!\nGoed gedaan!")
                                break
                            else:
                                error()
                                break
                        else:
                            error()
                            break
                    elif answer == "B":
                        time.sleep(1)
                        lines()
                        answer = input("Je neemt de taxi en jullie worden afgezet dichtbij de bios.\nDaar kopen jullie kaartjes en lopen naar binnen.\nNa de film Wil je…\nA. naar huis.\nB. nog naar de kroeg.\n>>>")
                        if answer == "A":
                            time.sleep(1)
                            lines()
                            print("Eindelijk kom je thuis en je vindt het tijd om te gaan slapen.\nJe hebt de reis overleefd!\nGoed gedaan!")
                            break
                        elif answer == "B":
                            time.sleep()
                            lines()
                            answer = input("Je komt aan in de kroeg en je bestelt…\nA. een Bier met alcohol.\nB. een Bier zonder alcohol.\n>>>")
                            if answer == "A":
                                time.sleep(1)
                                lines()
                                print("Je neemt de bier met alcohol en de volgende dag wordt je wakker door je vriend die je naar huis heeft gebracht die nacht.\nJe hebt het overleeft.")
                                break
                            error()
                            break
                    else:
                        error()
                        break
                elif answer == "B":
                    time.sleep(1)
                    lines()
                    answer == input("Je neemt een koffie en je voelt je gelijk wat beter.\nBij de uitgang wordt je verwelkomt door een vriend die in nederland woont en mag je bij hem tijdelijk komen wonen.\nJe neemt de bus en jullie worden afgezet dichtbij de bios.\nJullie kopen kaartjes en lopen naar binnen.\nAls snack kies je…\nA. Popcorn.\nB. Tortilla chips.\n>>>")
                    if answer == "A":
                        time.sleep()
                        lines()
                        answer = input("Je neemt de popcorn en je deelt wat met je vriend.\nNa de film besluit je om…\nA. naar de dam te gaan.\nB. nog even boodschappen te doen.\n>>>")
                        if answer == "A":
                            time.sleep(1)
                            lines()
                            answer = input("Je besluit om nog rond te gaan hangen op de dam waar straatartisten optreden.\nJe geeft de straatartiest…\nA. 10 euro.\nB. niks.\n>>>")
                            if answer == "A":
                                time.sleep(1)

                        elif answer == "B":
                            time.sleep(1)
                            lines()
                            answer = input("Je wordt raar aangekeken en je besluit om…\nA. 10 euro te geven.\nB. naar huis te gaan.\n>>>")
                            if answer == "A":
                                time.sleep(1)
                                lines()
                                answer = input("De straatartiest zegt: “Thank you” en jij besluit om na het optreden…\nA. naar huis te gaan.\nB. naar de mcdonalds te gaan.\n>>>")
                                if answer == "A":
                                    time.sleep(1)
                                    lines()
                                    print("Eindelijk kom je thuis en je vindt het tijd om te gaan slapen.\nJe hebt de reis overleefd!\nGoed gedaan!")
                                    break
                                elif answer == "B":
                                    time.sleep(1)
                                    lines()
                                    answer = input("Bij de mcdonalds kies je een grote portie.\nNadat je het op hebt gegeten besluit je om…\nA. naar huis te gaan.\nB. naar huis te gaan.")
                                    if answer == "A":
                                        time.sleep(1)
                                        lines()
                                        print("Eindelijk kom je thuis en je vindt het tijd om te gaan slapen.\je hebt de reis overleefd\nGoed gedaan!")
                                        break
                            elif answer == "B":
                                time.sleep(1)
                                lines()
                                print("Eindelijk kom je thuis en je vindt het tijd om te gaan slapen.\nJe hebt de reis overleefd!\nGoed gedaan!")
                                break
                            else:
                                error()
                                break
                    elif answer == "B":
                        time.sleep(1)
                        lines()
                        answer = input("Je neemt de tortilla chips en na de film besluit je om…\nA. naar de dam te gaan.\nB. nog even boodschappen te doen.\n>>>")
                        if answer == "A":
                            time.sleep(1)
                            lines()
                        elif answer == "B":
                            time.sleep(1)
                            lines()
                            answer = input("")
                    else:
                        error()
                        break

                elif answer == "C":
                    time.sleep(1)
                    lines()
                    print("Je neemt de thee, maar de thee blijkt vergiftigd te zijn.\nHelaas ben je niet in staat om verder te gaan en moet je naar het ziekenhuis.\nhelaas heb je het niet overleeft.\n>>>")
                    break
                else:
                    error()
                    break
            elif answer == "B":
                time.sleep(1)
                lines()
                print("Je probeert de duane te ontwijken, maar camera's zien dat je heel verdacht doet en de politie wordt ingelicht.\nJe wordt helaas opgepakt en naar de gevangenis gebracht.\n[Einde]")
                break
        else:
            error()
            break
    else:
        error()
        break

