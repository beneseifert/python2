rezept_ordner = "./rezepte/"

while True:
    print("Welche Pizza willst du machen?")
    pizza_name = input()

    if pizza_name == "":
        print("Guten Appetit!")
        break

    pizza_datei = rezept_ordner + pizza_name + ".txt"

    try:
        f = open(pizza_datei, "r")
        print("Zutaten für " + pizza_name + ":")
        print(f.read())
        f.close() 
    except FileNotFoundError:
        print("Die Pizza " + pizza_name + " kenne ich nicht.")
        print("Welche Zutaten hat diese Pizza?")
        zutaten = input()
        f = open(pizza_datei, "w")
        f.write(zutaten)
        f.close()
