souradnice = [[4, 0], [5, 0], [6, 0], [7, 0], [0, 1], [1, 1], [2, 1], [2, 2],
              [4, 2], [5, 2], [6, 2], [7, 2], [1, 3], [2, 3], [4, 3], [4, 4],
              [0, 5], [1, 5], [2, 5], [4, 5], [6, 5], [4, 6], [5, 6], [6, 6],
              [0, 7], [2, 7], [6, 4]]
mince = [[1, 2], [7, 1], [1, 7], [5, 5]]
hrac = [0, 0]

minka = len(mince)
zismince = 0
kek = [0, 0]
while zismince < 4:
    x = input()
    if x == "8":
        hrac = [hrac[0], hrac[1] + 1]
    elif x == "2":
        hrac = [hrac[0], hrac[1] - 1]
    elif x == "6":
        hrac = [hrac[0] + 1, hrac[1]]
    elif x == "4":
        hrac = [hrac[0] - 1, hrac[1]]

    if hrac[0] < 0:
        hrac[0] = kek[0]
    if hrac[1] < 0:
        hrac[1] = kek[1]
    if hrac[0] > 7:
        hrac[0] = kek[0]
    if hrac[1] > 7:
        hrac[1] = kek[1]
    if hrac in souradnice:
        hrac = kek
        print("zeď")
    if hrac in mince:
        zismince = zismince + 1
        mince.remove(hrac)
        print(str(zismince) + " mince / " + str(minka))
    print(hrac)
    kek = (hrac[0], hrac[1])
while zismince == 4:
    print("Výhra")