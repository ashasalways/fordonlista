import lastbil
import personbil


looping = True

opel_red= personbil.Personbil("Opel", "red", 69)
bmw_black= personbil.Personbil("BMW", "black", 898)

volvo_pink= lastbil.Lastbil("Volvo", "pink", 36000)
scania_blue= lastbil.Lastbil("Scania", "blue", 32000)

personbils_lista = [opel_red, bmw_black]
lastbils_lista = [volvo_pink, scania_blue]

def print_fordonslista(fordonslista):
    for ettfordon in fordonslista:
        ettfordon.print_fordon()

while looping:

    print("------------------------------------")
    print("\nKlasser och arv av fordon \n")

    val_fordon = input("Vilken fordonstyp vill du lista? 1=Lastbil 2=Personbil: ")

    if (val_fordon == "1"):
        print("\n-Lastbilar-\n")
        print("---------------------------------")
        print_fordonslista(lastbils_lista)

    elif (val_fordon == "2"):
        print("\n-Personbilar-\n")
        print("---------------------------------")
        print_fordonslista(personbils_lista)

    else:
        print("\nOgiltig inmatning!\n")

    go = input("\nVill ni lista fordonen igen? j/n\n")

    if (go == "n"):
        break