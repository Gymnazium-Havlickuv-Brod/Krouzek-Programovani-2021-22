from random import randint
global guess_word
global final_word
guess_word = ""
final_word = ""
random_word = 0
started = False
words = ["Tepláky", "Pohřeb", "Koruna", "Voskovka", "Batman", "Beruška", "Doktor", "Policie", "Senior",
                      "Láska", "Lékárna", "Banka", "Hruška", "Účes", "Kámen", "Sešit", "Talíř", "Biologie", "Kostra",
                      "Film", "Akce", "Vesnice", "Slovo", "Bublina", "Batoh", "Šunka", "Cíl", "Pavouk", "Brusle",
                      "Potkan", "Pes", "Kočka", "Bagr", "Večer", "Lednice", "Led", "Sestra", "Láhev", "Barva", "Sůl",
                      "Rande", "Kouř", "Koště", "Plat", "Květ", "Mýdlo", "Skóre", "Letadlo", "Start", "Meč", "Seriál",
                      "Vrah", "Kmen", "Opice", "Smrt", "Lebka", "Kytka", "Ráno", "Páteř", "Třída", "Guláš", "Šatník",
                      "Obrázek", "Čeština", "Datum", "Kostka", "Propiska", "Nápověda", "Soubor", "Televizor",
                      "Programátor", "Jahoda", "Červená", "Tužkovník", "Lampička", "Němčina", "Rádio", "Stojan",
                      "Počítač", "Historie", "Učebnice", "Papírek", "Lišta", "Potůček", "Úmoří", "Seriál", "Knihovna",
                      "Písemka", "Vodník", "Ponožky", "Mikina", "Fixa", "Motýlek", "Plechovka", "Lepidlo", "Komiks",
                      "Skřipec", "Gumička", "Smyčec", "Žíně", "Břetislav", "Matematika", "Pomáda", "Pneumatika",
                      "Elektrika", "Žebřík", "Zahrada", "Pytlík", "Grafika", "Tablet", "Zornice", "Sklivec", "Lvice",
                      "Mládě", "Dárek", "Sluchátka", "Mikrofon", "Rohožka", "Sklovina", "Slonovina", "Užovka", "Světlo",
                      "Víčko", "Koumák", "Uklízečka", "Školník", "Skříňka", "Bonbón", "Pilník", "Ovladač", "Program",
                      "Kalendář", "Hora", "Cesta", "Silnice", "Autobus", "Kroužek", "Prsten", "Žebro", "Umyvadlo",
                      "Hřeben", "Nehet", "Tlačítko", "Pot", "Místo", "Alarm", "Budík", "Hodiny", "Stan", "Táborák",
                      "Mince", "Čepice", "Schody", "Sandále", "Kůže", "Princ", "Mobil", "Reproduktor", "Mast", "Fleška",
                      "Sova", "Zajíc", "Želva", "Mixér", "Pult", "Číšník", "Klíč", "Klišé", "Klasika", "Voda", "Citron",
                      "Večer", "Popelnice","Koš", "Kos", "Arkáda", "Kretén", "Displej", "Figurína", "Model", "Vana",
                      "Kocour", "Palec", "Ministr", "Hejkal", "Zobák", "Hřib", "Okov", "Tabák", "Dřevo", "Panelák",
                      "Díra", "Jamka", "Kvádr", "Krychle", "Hlasitost", "Upozornění", "Bod", "Hodinky", "Nota",
                      "Plusko", "Jupiter", "Venuše", "Thor", "Plot", "Šufle", "Čokoláda", "Zatáčka", "Slalom", "Zlom",
                      "Kočí", "Koně", "Náklad", "Židle", "Aplaus", "Potlesk", "Stín", "Skládka", "Třpytky", "Letopočet",
                      "Tisk", "Odraz", "Svátek", "Monokl", "Doupě", "Kapesník"]


def word():
        global guess_word
        global final_word
        random_word = randint(0, len(words) - 1)
        guess_word = words[random_word]
        number_of_letters = len(guess_word)
        order_of_letters = []
        final_word_list = []

        while len(order_of_letters) < number_of_letters:
            random_letter = randint(0, number_of_letters - 1)

            if len(order_of_letters) < 1:
                order_of_letters.append(random_letter)
                # print("První číslo: " + str(random_letter))
            else:
                is_there_letter = 0
                for letter in order_of_letters:
                    if int(letter) == int(random_letter):
                        pass
                    else:
                        is_there_letter += 1
                if is_there_letter == len(order_of_letters):
                    order_of_letters.append(random_letter)
                    # print("Nové číslo!" + " číslo: " + str(random_letter))

        for num_letter in order_of_letters:
            letter = words[random_word][num_letter]
            final_word_list.append(letter)

        final_word = "".join(final_word_list)

        #print("Pořadí slov: " + str(random_word) + " | Slovo: " +  words[random_word] + " | Počet písmen: " + str(number_of_letters) + " | Náhodné pořadí písmen: " + str(order_of_letters) + " | Výsledné slovo: " + final_word)
        # await channel.send(
        # await channel.send(len(words))
        #print("funguje ve word_game.py")

word()
answer = input("Uhádni slovo, jehož písmena byly přeházeny! Slovo: " + final_word + " --> ")
true_answer = (guess_word.lower() in answer.lower())
if true_answer == True:
    print("Správně!")
else: 
    print("Špatně!")