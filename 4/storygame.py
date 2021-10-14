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
# player["name"] = ask("Who are u?")
player["name"] = "Adam"
print("Hello, " + player["name"] + "!!")


#nabidnete hraci jake itemy si chce zabalit 10 ale vybere jen 5
shelf = [("jojo", 1),
        ("apple", 2),
        ("beer", 4),
        ("banana", 2),
        ("rocketlauncher", 10),
        ("lighter",1)]

def print_item_list(item_list, phrase):
    print(phrase)
    print("------------------------------------")
    for i in range(len(item_list)):
        print(f"{str(i+1)}. - {item_list[i][0]} ({item_list[i][1]} kg)")
    print("------------------------------------")
    print("\n\n")

while True:
    # Moje itemy
    print_item_list(player["items"], "Your items are:")

    # vytiskni itemy na policce
    print_item_list(shelf, "On the shefl there are:")

    # vyber jeden item podle cisla a pridej ho do batohu
    wanted_index = ask("What do u want?")
    wanted_index = int(wanted_index) - 1

    wanted_item = shelf[wanted_index]

    weight = 0
    for item in player["items"]:
        weight += item[1]


    

    if weight + wanted_item[1] > player["bag_cap"]:
        print("This item is too heavy.")
        print("Capacity is over: " + str(weight + wanted_item[1]) + "/" +str(player["bag_cap"]))
        continue

    # p5esun itemu na policku
    shelf.remove(wanted_item)
    player["items"].append(wanted_item)
    print("Capacity: " + str(weight + wanted_item[1]) + "/" +str(player["bag_cap"]))

    

#zkontroluj ale jestli se tam vejde



#pripravte prvni rozhodnuti kam se vyda - zaznacte ho do promene at ma vliv dal




