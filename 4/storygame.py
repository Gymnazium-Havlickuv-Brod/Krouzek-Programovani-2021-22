# items
# name
# hp
# money

player = {
    "name" : "Noone",
    "hp" : 100,
    "money" : 10,
    "items":[("sword",7),  ("candle", 1)],
    "bag_cap": 20
}

print(player)

def ask(question):
    res = input(question + " \n>>")
    return res


#pojmenujte hrace
player["name"] = ask("Who are u?")
print("Hello, " + player["name"] + "!!")


#nabidnete hraci jake itemy si chce zabalit 10 ale vybere jen 5
shelf = [("jojo", 1),
        ("apple", 2),
        ("beer", 4),
        ("banana", 2),
        ("rocketlauncher", 10),
        ("lighter",1)]


# vytiskni itemy na policce
print("On the shefl there are:")
for i in range(len(shelf)):
    print(f"{str(i+1)}. - {shelf[i][0]} ({shelf[i][1]} kg)")

ask("What do u want?")
# vyber jeden item podle cisla a pridej ho do batohu


#zkontroluj ale jestli se tam vejde



#pripravte prvni rozhodnuti kam se vyda - zaznacte ho do promene at ma vliv dal




